"""
@author  : MG
@Time    : 2020/11/16 10:20
@File    : template.py
@contact : mmmaaaggg@163.com
@desc    : 用于
"""
import json
import threading
from datetime import datetime
from typing import List, Dict, Optional

import numpy as np
import pandas as pd
from ibats_utils.mess import datetime_2_str
from vnpy.app.portfolio_strategy import StrategyTemplate as StrategyTemplateBase
from vnpy.trader.constant import Direction, Offset
from vnpy.trader.object import BarData, TickData, TradeData

from vnpy_extra.backtest import STOP_OPENING_POS_PARAM, ENABLE_COLLECT_DATA_PARAM, StopOpeningPos, \
    check_datetime_trade_available, generate_mock_load_bar_data
from vnpy_extra.backtest import check_datetime_available
from vnpy_extra.config import logging
from vnpy_extra.constants import GeneralPeriodEnum
from vnpy_extra.db.orm import AccountStrategyStatusEnum
from vnpy_extra.report.collector import trade_data_collector, order_data_collector, latest_price_collector
from vnpy_extra.report.monitor import AccountStrategyStatusMonitor
from vnpy_extra.utils.enhancement import BarGenerator


class StrategyTemplate(StrategyTemplateBase):
    # 该标识位默认为0（关闭状态）。为1时开启，程序一旦平仓后则停止后续交易。该标识位用于在切换合约时使用
    stop_opening_pos = StopOpeningPos.open_available.value
    # 考虑到六、周日、节假日等非交易日因素，保险起见，建议初始化日期 * 2 + 7
    init_load_days = 30
    # 加载主连连续合约作为合约历史行情数据（默认为False)
    load_main_continuous_md = False
    # 对应周期类型
    period_enum = GeneralPeriodEnum.m1.name

    def __init__(self, strategy_engine, strategy_name, vt_symbols, setting):
        super().__init__(strategy_engine, strategy_name, vt_symbols, setting)
        # setting 不包含 stop_opening_pos key
        self.setting = {k: v for k, v in setting.items() if k in self.parameters}
        self.parameters.append(STOP_OPENING_POS_PARAM)  # 增加 stop_opening_pos 用于合约切换是关闭当前线程
        self.logger = logging.getLogger(f'strategies.portfolio.{strategy_name}')
        # 写日志
        self.logger.info(f"{strategy_name} on {vt_symbols} setting=\n{json.dumps(setting, indent=4)}")
        # 仅用于 on_order 函数记录上一个 order 使用，解决vnpy框架重复发送order的问题
        self._last_order = {}
        self.received_trade_list = []  # 记录所有成交数据
        # 1分钟 bar 对象字典及bar数量
        self.current_bars: Optional[Dict[str, BarData]] = None
        self.bar_count = 0
        # 生成指定周期 bar 对象字典及 win bar 数量
        self.current_win_bars: Optional[Dict[str, BarData]] = None
        self.win_bar_count = 0
        # 是否实盘环境
        self._is_realtime_mode = self.strategy_name is not None and self.strategy_name != self.__class__.__name__
        self._strategy_status = AccountStrategyStatusEnum.Created
        # 是否收集申请单以及交易单记录
        self.enable_collect_data = ENABLE_COLLECT_DATA_PARAM in setting and setting[ENABLE_COLLECT_DATA_PARAM]
        self._strategy_status_monitor: Optional[AccountStrategyStatusMonitor] = None
        self._lock: Optional[threading.Lock] = None

        # 最近一个tick的时间
        self.last_tick_time: Optional[datetime] = None
        # 最近一次下单的时间
        self.last_order_dt: Dict[str, datetime] = {}
        # 最近一条提示信息
        self._last_msg = ''

        def on_bar(bar: BarData):
            """"""
            pass

        self.bgs: Dict[str, BarGenerator] = {}
        period_enum: GeneralPeriodEnum = GeneralPeriodEnum[self.period_enum]
        window, interval = period_enum.value
        self._win_bars = {}
        for vt_symbols in self.vt_symbols:
            self.bgs[vt_symbols] = BarGenerator(
                on_bar, window=window, interval=interval, on_window_bar=self._on_win_bar)
            self._win_bars[vt_symbols] = None

    def set_is_realtime_mode(self, is_realtime_mode):
        self._is_realtime_mode = is_realtime_mode

    def get_id_name(self):
        """获取 id_name"""
        param_str = '_'.join([
            str(self.setting[key]) for key in self.parameters
            if key in self.setting and key != STOP_OPENING_POS_PARAM])
        id_name = f"{self.__class__.__name__}_{param_str}" if param_str != "" else f"{self.__class__.__name__}"
        return id_name

    def _set_strategy_status(self, status: AccountStrategyStatusEnum):
        if not self._is_realtime_mode:
            # 仅针对实时交易是使用
            return
        if self._strategy_status == status:
            return

        if status == AccountStrategyStatusEnum.RunPending and self._strategy_status not in (
                AccountStrategyStatusEnum.Created, AccountStrategyStatusEnum.Running
        ):
            # AccountStrategyStatusEnum.RunPending 状态只从数据库端发起
            if self._lock is not None:
                self._lock.acquire()

            try:
                # 保险起见，为防止出现死循环调用，在 on_start 先把状态调整过来
                self._strategy_status = status
                self.write_log(f"策略 {self.strategy_name} {self.vt_symbols} 状态 "
                               f"{self._strategy_status.name} -> {status.name} 被远程启动")
            finally:
                if self._lock is not None:
                    self._lock.release()

            self.on_start()

        elif status == AccountStrategyStatusEnum.StopPending and self._strategy_status == AccountStrategyStatusEnum.Running:
            # AccountStrategyStatusEnum.StopPending 状态只从数据库端发起
            if self._lock is not None:
                self._lock.acquire()

            try:
                # 保险起见，为防止出现死循环调用，在 on_stop 先把状态调整过来
                self._strategy_status = status
                self.write_log(f"策略 {self.strategy_name} {self.vt_symbols} 状态 "
                               f"{self._strategy_status.name} -> {status.name} 被远程停止")
            finally:
                if self._lock is not None:
                    self._lock.release()

            self.on_stop()
        else:
            self.write_log(f"策略 {self.strategy_name} {self.vt_symbols} 状态 "
                           f"{self._strategy_status.name} -> {status.name}")
            self._strategy_status = status

    def _get_strategy_status(self) -> AccountStrategyStatusEnum:
        return self._strategy_status

    def on_init(self) -> None:
        super().on_init()
        self.bar_count = 0
        if self._is_realtime_mode:
            self._set_strategy_status(AccountStrategyStatusEnum.Initialized)

        if self._is_realtime_mode and self._strategy_status_monitor is None:
            # 该语句一定不能放在 __init__ 中
            # 因为 strategy_name 在回测阶段模块中，在 __init__ 后可能会被重写赋值
            self._strategy_status_monitor = AccountStrategyStatusMonitor(
                self.strategy_name,
                self._get_strategy_status,
                self._set_strategy_status,
                self.vt_symbols,
                self.setting
            )
            self._lock = self._strategy_status_monitor.lock

        if self._strategy_status_monitor is not None and not self._strategy_status_monitor.is_alive():
            self._strategy_status_monitor.start()

        self.enable_collect_data |= self._is_realtime_mode
        if self.enable_collect_data:
            trade_data_collector.queue_timeout = 90 if self._is_realtime_mode else 1
            order_data_collector.queue_timeout = 90 if self._is_realtime_mode else 1

        if self._is_realtime_mode and self.load_main_continuous_md:
            with generate_mock_load_bar_data(self.write_log):
                self.load_bars(self.init_load_days)
        else:
            self.load_bars(self.init_load_days)

        self.write_log(f"策略初始化完成. 加载{self.init_load_days}天数据")

    def on_start(self) -> None:
        super().on_start()
        if self._is_realtime_mode:
            self._set_strategy_status(AccountStrategyStatusEnum.Running)
        # 整理持仓信息
        if len(self.pos) == 0:
            self.write_log(f"策略启动，当前初始持仓：(无)")
        else:
            pos_str = '\t'.join([f"{k}: {v}" for k, v in self.pos.items()])
            self.write_log(f"策略启动，当前初始持仓：\n{pos_str}")

        self.put_event()

        # 初始化相关数据,可以在重启策略时清空历史订单对当前策略的影响.
        # 仅用于 on_order 函数记录上一个 order 使用，解决vnpy框架重复发送order的问题
        self._last_order = {}
        self.received_trade_list = []  # 记录所有成交数据
        # 最近一次下单的时间
        self.last_order_dt: Dict[str, datetime] = {}
        # if self._is_realtime_mode:
        #     start_strategy_position_monitor()

    def on_tick(self, tick: TickData) -> bool:
        """判断当前tick数据是否有效,如果无效数据直接返回 False,否则更新相应bar数据"""
        super().on_tick(tick)
        is_available = check_datetime_available(tick.datetime)
        if not is_available:
            return is_available

        if (
                self.last_tick_time
                and self.last_tick_time.minute != tick.datetime.minute
        ):
            bars = {}
            for vt_symbol, bg in self.bgs.items():
                bars[vt_symbol] = bg.generate()
            self.on_bars(bars)

        bg: BarGenerator = self.bgs[tick.vt_symbol]
        bg.update_tick(tick)
        latest_price_collector.put_nowait(tick)
        self.last_tick_time = tick.datetime.replace(tzinfo=None)
        return is_available

    def on_bars(self, bars: Dict[str, BarData]) -> None:
        super().on_bars(bars)
        self.current_bars: Dict[str, BarData] = bars
        self.bar_count += 1
        for vt_symbol, bar in bars.items():
            self.bgs[vt_symbol].update_bar(bar)

    def _on_win_bar(self, bar: BarData):
        """
        激活 on_win_bars 函数
        逻辑:
        通过 bg 生成对应 vt_symbol 的 win bar,当全部 vt_symbol 的 win bar 均生成完毕后,触发 on_win_bars 函数
        由于 on_tick 阶段 通过 gb.generate() 强行在同一时刻生成了所有 bar,因此可以保证,当生成对应 win bar 时,也会是同时生成,
        因此,此处不考虑部分生成的情况
        """
        self._win_bars[bar.vt_symbol] = bar
        for _ in list(self._win_bars.values()):
            if _ is None:
                break
        else:
            self.on_win_bars(self._win_bars)
            self._win_bars = {_: None for _ in self._win_bars.keys()}

    def on_win_bars(self, bars: Dict[str, BarData]) -> None:
        self.current_win_bars: Dict[str, BarData] = bars
        self.win_bar_count += 1

    def send_order(self,
                   vt_symbol: str,
                   direction: Direction,
                   offset: Offset,
                   price: float,
                   volume: float,
                   lock: bool = False
                   ) -> List[str]:
        current_pos = int(self.get_pos(vt_symbol))
        order_datetime = self.current_bars[vt_symbol].datetime if (
                self.current_bars is not None
                and vt_symbol in self.current_bars
                and self.current_bars[vt_symbol] is not None) else None
        ignore_order = False
        if price <= 0.0:
            log_level = 'error'
            msg = '【价格无效】'
            ignore_order = True
        elif order_datetime is not None and not check_datetime_trade_available(order_datetime):
            # 回测模式下提示此类信息
            log_level = 'warning' if self._is_realtime_mode else 'debug'
            msg = '【非交易时段】'
            ignore_order = True
        elif self.stop_opening_pos != StopOpeningPos.open_available.value and offset == Offset.OPEN:
            log_level = 'warning'
            msg = '【禁止开仓】'
            ignore_order = True
        else:
            log_level = 'debug'
            msg = ''

        if offset == Offset.OPEN:
            if self.stop_opening_pos != StopOpeningPos.stop_opening_and_nolog.value:
                self.write_log(
                    f"{vt_symbol:>11s} {direction.value} {offset.value:4s} {price:.1f} "
                    f"{current_pos:+d} {volume:+.0f} "
                    if order_datetime is None else
                    f"{datetime_2_str(order_datetime)} {vt_symbol} {direction.value} {offset.value:4s} {price:.1f} "
                    f"{current_pos:+d} {volume:+.0f}{msg}",
                    log_level
                )

            if self.stop_opening_pos != StopOpeningPos.open_available.value:
                self.write_log(f"当前策略 stop_opening_pos="
                               f"{self.stop_opening_pos}<{StopOpeningPos(self.stop_opening_pos).name}>，"
                               f"所有开仓操作将被屏蔽（用于主力合约切换,或关闭失效策略使用）", log_level)
                self.stop_opening_pos = StopOpeningPos.stop_opening_and_nolog.value

        else:
            self.write_log(
                f"{vt_symbol:>11s} {direction.value} {offset.value:4s} {price:.1f} "
                f"      {current_pos:+d} {-volume:+.0f} "
                if order_datetime is None else
                f"{datetime_2_str(order_datetime)} {vt_symbol} {direction.value} {offset.value:4s} {price:.1f} "
                f"      {current_pos:+d} {-volume:+.0f}{msg}",
                log_level
            )

        if order_datetime is None:
            order_datetime = datetime.now()

        if ignore_order:
            return []

        if vt_symbol in self._last_order:
            # 记录订单情况，跳过重复订单
            last_order = self._last_order[vt_symbol]
            if last_order['direction'] != direction.value \
                    or last_order['offset'] != offset.value \
                    or last_order['price'] != price \
                    or last_order['volume'] != volume:
                is_not_duplicate_order = True
            else:
                is_not_duplicate_order = False
        else:
            is_not_duplicate_order = True

        if is_not_duplicate_order:
            symbol, exchange = vt_symbol.split('.')
            order = {
                "datetime": order_datetime,
                "symbol": symbol,
                "exchange": exchange,
                "direction": direction.value,
                "offset": offset.value,
                "price": price,
                "volume": volume,
            }
            if self.enable_collect_data:
                order_data_collector.put_nowait(self.strategy_name, order)

            self._last_order[vt_symbol] = order

        self.last_order_dt[vt_symbol] = datetime.now()
        return super().send_order(vt_symbol, direction, offset, price, volume, lock)

    def on_stop(self):
        super().on_stop()
        if self._is_realtime_mode:
            self._set_strategy_status(AccountStrategyStatusEnum.Stopped)
        self.put_event()

    def update_trade(self, trade: TradeData):
        super().update_trade(trade)
        self.received_trade_list.append(trade)
        if self.enable_collect_data:
            trade_data_collector.put_nowait(self.strategy_name, trade)

    def write_log(self, msg: str, logger_method='info'):
        if self._last_msg == msg:
            return
        msg = f"{self.strategy_name} {msg}"
        super().write_log(msg)
        getattr(self.logger, logger_method)(msg)
        self._last_msg = msg

    def is_available(self, stats: dict, df: pd.DataFrame) -> bool:
        balance_s = df["balance"]
        is_available = not (
                stats['total_net_pnl'] <= 0
                or stats['daily_trade_count'] < 0.2  # 1/0.2 每一次交易平仓再开仓需要2次交易，因此相当于10天交易一次
                or stats['return_drawdown_ratio'] < 1.5
                or stats['max_new_higher_duration'] >= 180  # 最长不创新高周期<180
                or stats['max_new_higher_duration'] / stats['total_days'] > 0.5  # 最长不创新高周期超过一半的总回测天数
                or balance_s is None  # 没有交易
                or np.sum((balance_s - stats['capital']) <= 0) / stats['total_days'] > 0.5  # 50%以上交易日处于亏损状态
                or np.all(df["drawdown"][df["drawdown"].idxmin():] < 0)  # 最大回撤到最后一个交易日需要出现新高
        )
        return is_available


if __name__ == "__main__":
    pass
