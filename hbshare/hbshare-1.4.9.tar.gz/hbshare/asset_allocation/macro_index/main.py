import pandas as pd
from sqlalchemy import create_engine
from hbshare.rm_associated.config import engine_params
from datetime import datetime
import pyecharts.options as opts
from pyecharts.charts import Line, Bar
from pyecharts.globals import ThemeType
import pywt
import hbshare as hbs
import requests
import json


def series_denoising(data):
    db4 = pywt.Wavelet('db4')
    coeffs = pywt.wavedec(data, db4)
    coeffs[len(coeffs) - 1] *= 0
    coeffs[len(coeffs) - 2] *= 0
    meta = pywt.waverec(coeffs, db4)

    return meta[:-1]


"======================================================宏观经济类========================================================"


class CurrencyIndex:
    """
    货币类指标
    """
    def __init__(self, start_date='20050131', end_date='20210331'):
        self.start_date = start_date
        self.end_date = end_date
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_curr where TRADE_DATE >= {} and TRADE_DATE <= {}".format(
            self.start_date, self.end_date)
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))

        self.monthly_data = data.set_index(
            'trade_date')[['M1_yoy', 'M2_yoy', 'short_term_loan_balance', 'long_term_loan_balance',
                           'social_finance_yoy']].dropna(axis=0, how='all')
        self.daily_data = data.set_index(
            'trade_date')[['reverse_repo_7', 'LPR_1_year', 'LPR_5_year']].dropna(axis=0, how='all')

    def draw_picture_M1_M2(self):
        df = self.monthly_data[['M1_yoy', 'M2_yoy']]
        df['spread'] = df['M1_yoy'] - df['M2_yoy']
        # 小波去噪
        df['M1_de'] = series_denoising(df['M1_yoy'])
        df['M2_de'] = series_denoising(df['M2_yoy'])
        df['spread_de'] = series_denoising(df['spread'])

        df = df.round(2).reset_index()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观流动性"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='year-on-year (%)',
                name_location='middle',
                name_gap=45,
                min_=-20,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="M1",
            is_smooth=True,
            y_axis=df["M1_de"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="M2",
            is_smooth=True,
            y_axis=df["M2_de"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="M1-M2",
            is_smooth=True,
            y_axis=df["spread_de"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_loan(self):
        df = self.monthly_data[['short_term_loan_balance', 'long_term_loan_balance']]
        df = (100 * df.pct_change(periods=12).dropna()).round(2)
        df.reset_index(inplace=True)

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观流动性"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='year-on-year (%)',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="金融机构：短期贷款余额",
            is_smooth=True,
            y_axis=df["short_term_loan_balance"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="金融机构：长期贷款余额",
            is_smooth=True,
            y_axis=df["long_term_loan_balance"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_social_lending(self):
        df = self.monthly_data[['social_finance_yoy']].dropna().reset_index()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观流动性"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='year-on-year (%)',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="社会融资规模存量同比",
            is_smooth=True,
            y_axis=df["social_finance_yoy"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_daily_currency_pic(self):
        sql_script = "SELECT JYRQ, SFJJ, SFZM, SFYM FROM funddb.JYRL WHERE JYRQ >= {} and JYRQ <= {} and " \
                     "SFYM = 1".format(self.start_date, self.end_date)
        res = hbs.db_data_query('readonly', sql_script, page_size=5000)
        df = pd.DataFrame(res['data']).rename(
            columns={"JYRQ": 'calendarDate', "SFJJ": 'isOpen',
                     "SFZM": "isWeekEnd", "SFYM": "isMonthEnd"}).sort_values(by='calendarDate')
        month_end_list = df['calendarDate'].tolist()

        df = self.daily_data.fillna(method='ffill').reindex(month_end_list).dropna(how='all').reset_index()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观流动性"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="7日逆回购利率",
            y_axis=df["reverse_repo_7"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            is_step=True,
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="LPR：1年",
            y_axis=df["LPR_1_year"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            is_step=True,
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="LPR：5年",
            y_axis=df["LPR_5_year"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            is_step=True,
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line


class CreditIndex:
    """
    信用类指标
    """
    def __init__(self, frequency='week',  start_date='20050131', end_date='20210331'):
        self.frequency = frequency
        self.start_date = start_date
        self.end_date = end_date
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_credit where TRADE_DATE >= {} and TRADE_DATE <= {}".format(
            self.start_date, self.end_date)
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))
        # calendar
        sql_script = "SELECT JYRQ, SFJJ, SFZM, SFYM FROM funddb.JYRL WHERE JYRQ >= {} and JYRQ <= {} and " \
                     "SFJJ = 0".format(self.start_date, self.end_date)
        res = hbs.db_data_query('readonly', sql_script, page_size=5000)
        df = pd.DataFrame(res['data']).rename(
            columns={"JYRQ": 'calendarDate', "SFJJ": 'isOpen',
                     "SFZM": "isWeekEnd", "SFYM": "isMonthEnd"}).sort_values(by='calendarDate')
        if self.frequency == 'month':
            trading_day_list = df[df['isMonthEnd'] == '1']['calendarDate'].tolist()
        else:
            trading_day_list = df[df['isWeekEnd'] == '1']['calendarDate'].tolist()
        # 产业债信用利差数据
        self.credit_spread_indu = \
            data.set_index('trade_date')[[
                'credit_spread_indu_AAA', 'credit_spread_indu_AA_plus', 'credit_spread_indu_AA']].reindex(
                trading_day_list).dropna()
        # 城投债信用利差数据
        self.credit_spread_urban = \
            data.set_index('trade_date')[[
                'credit_spread_urban_AAA', 'credit_spread_urban_AA_plus', 'credit_spread_urban_AA']].reindex(
                trading_day_list).dropna()
        # 杠杆率数据
        self.leverage_data = data.set_index('trade_date')[[
            'leverage_1', 'leverage_2', 'leverage_3', 'leverage_4']].dropna(how='all')

    def draw_picture_indu(self):
        df = self.credit_spread_indu.reset_index()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="产业债信用利差"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='Credit Spread (bp)',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside")],
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="信用利差：产业债AAA",
            is_smooth=True,
            y_axis=df["credit_spread_indu_AAA"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="信用利差：产业债AA+",
            is_smooth=True,
            y_axis=df["credit_spread_indu_AA_plus"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="信用利差：产业债AA",
            is_smooth=True,
            y_axis=df["credit_spread_indu_AA"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_urban(self):
        df = self.credit_spread_urban.reset_index()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="城投债信用利差"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='Credit Spread (bp)',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside")],
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="信用利差：城投债AAA",
            is_smooth=True,
            y_axis=df["credit_spread_urban_AAA"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="信用利差：城投债AA+",
            is_smooth=True,
            y_axis=df["credit_spread_urban_AA_plus"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="信用利差：城投债AA",
            is_smooth=True,
            y_axis=df["credit_spread_urban_AA"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_leverage(self):
        df = self.leverage_data.reset_index()
        df['trade_date'] = df['trade_date'].apply(lambda x: x[:4] + '-' + x[4:6])
        df['ratio_pct'] = df['leverage_1'].pct_change()
        df = df[1:]
        df['ratio_pct'] = (100 * df['ratio_pct']).round(2)

        bar = (
            Bar(init_opts=opts.InitOpts(width='1200px', height='600px', theme=ThemeType.WESTEROS))
            .add_xaxis(
                xaxis_data=df['trade_date'].tolist())
            .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                    splitline_opts=opts.SplitLineOpts(is_show=False))
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="宏观杠杆率"),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                legend_opts=opts.LegendOpts(pos_top='5%'),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    axislabel_opts={"interval": "0", "rotate": 90},
                    axistick_opts=opts.AxisTickOpts(is_show=True)),
            ).add_yaxis(
                series_name='居民部门杠杆率',
                stack="stack1",
                y_axis=df['leverage_2'].tolist(),
                label_opts=opts.LabelOpts(is_show=False),
                bar_width="50%",
                z=0
            ).add_yaxis(
                series_name='非金融企业部门杠杆率',
                stack="stack1",
                y_axis=df['leverage_3'].tolist(),
                label_opts=opts.LabelOpts(is_show=False),
                bar_width="50%",
                z=0
            ).add_yaxis(
                series_name='政府部门杠杆率',
                stack="stack1",
                y_axis=df['leverage_3'].tolist(),
                label_opts=opts.LabelOpts(is_show=False),
                bar_width="50%",
                z=0
            )
        )

        line = (
            Line()
            .add_xaxis(
                xaxis_data=df['trade_date'].tolist())
            .add_yaxis(
                series_name="实体经济部门杠杆环比增速",
                is_smooth=True,
                y_axis=df["ratio_pct"].tolist(),
                is_symbol_show=True,
                linestyle_opts=opts.LineStyleOpts(width=1.8),
                label_opts=opts.LabelOpts(is_show=False),
                yaxis_index=1
            )
        )

        bar.overlap(line)

        return bar


class InflationIndex:
    """
    通胀类指标
    """
    def __init__(self, start_date='20050131', end_date='20210331'):
        self.start_date = start_date
        self.end_date = end_date
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_inflation where TRADE_DATE >= {} and TRADE_DATE <= {}".format(
            self.start_date, self.end_date)
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))

        self.data = data[['trade_date', 'CPI_yoy', 'PPI_yoy', 'LME']].dropna()

    def draw_picture(self):
        df = self.data.copy()

        line1 = (
            Line(init_opts=opts.InitOpts(width='1200px', height='600px', theme=ThemeType.WESTEROS))
            .add_xaxis(
                xaxis_data=df['trade_date'].tolist())
            .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=False))
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="通胀数据"),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    axistick_opts=opts.AxisTickOpts(is_show=True)),
            ).add_yaxis(
                series_name="CPI：当月同比",
                y_axis=df["CPI_yoy"].tolist(),
                is_symbol_show=False,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(width=1.8),
                label_opts=opts.LabelOpts(is_show=False)
            ).add_yaxis(
                series_name="PPI：当月同比",
                y_axis=df["PPI_yoy"].tolist(),
                is_symbol_show=False,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(width=1.8),
                label_opts=opts.LabelOpts(is_show=False)
            )
        )

        line2 = (
            Line()
            .add_xaxis(
                xaxis_data=df['trade_date'].tolist())
            .add_yaxis(
                series_name="LME铜",
                is_smooth=True,
                y_axis=df["LME"].tolist(),
                is_symbol_show=False,
                linestyle_opts=opts.LineStyleOpts(width=1.8),
                label_opts=opts.LabelOpts(is_show=False),
                yaxis_index=1
            )
        )
        line1.overlap(line2)

        return line1


class EconomyIncreaseIndex:
    """
    经济增长类指标
    """
    def __init__(self, start_date='20050131', end_date='20210331'):
        self.start_date = start_date
        self.end_date = end_date
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_eco_increase where TRADE_DATE >= {} and TRADE_DATE <= {}".format(
            self.start_date, self.end_date)
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))

        self.data = data[['trade_date', 'GDP', 'PMI', 'generating_cap_yoy', 'Consumer_Index', 'house_price_yoy']]

    def draw_picture_gdp(self):
        df = self.data[['trade_date', 'GDP']].dropna()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观经济增长"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='year-on-year (%)',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="GDP:不变价:当季同比",
            is_smooth=True,
            y_axis=df["GDP"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=2),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_PMI(self):
        df = self.data[['trade_date', 'PMI']].dropna()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观经济增长"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='PMI Index',
                name_location='middle',
                name_gap=45,
                min_=30,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="制造业PMI",
            is_smooth=True,
            y_axis=df["PMI"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=2),
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(y=50, name="枯荣线")])
        )

        return line

    def draw_picture_elec(self):
        df = self.data[['trade_date', 'generating_cap_yoy']].dropna()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观经济增长"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='Generating Capacity (%)',
                name_location='middle',
                name_gap=45,
                # min_=30,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="发电量：当月同比",
            is_smooth=True,
            y_axis=df["generating_cap_yoy"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=2),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_consumer_index(self):
        df = self.data[['trade_date', 'Consumer_Index']].dropna()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观经济增长"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='Consumer Index',
                name_location='middle',
                name_gap=45,
                min_=80,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="消费者信心指数",
            is_smooth=True,
            y_axis=df["Consumer_Index"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=2),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_house_price_index(self):
        df = self.data[['trade_date', 'house_price_yoy']].dropna()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="宏观经济增长"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='House Price Index',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="70个大中城市新建商品住宅价格指数:环比",
            is_smooth=True,
            y_axis=df["house_price_yoy"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=2),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line


"=====================================================股票市场宏微观======================================================"


class StockMarketPE:
    """
    股票市场估值分位
    """
    def __init__(self, window, index_list, start_date='20050131', end_date='20210331'):
        self.window = window
        self.index_list = index_list
        self.start_date = start_date
        self.end_date = end_date
        self._load_data()

    def _load_data(self):
        pre_date = str(int(self.start_date[:4]) - self.window) + self.start_date[4:]

        sql_script = "SELECT * FROM mac_stock_pe_ttm where TRADE_DATE >= {} and TRADE_DATE <= {}".format(
            pre_date, self.end_date)
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))
        # calendar
        sql_script = "SELECT JYRQ, SFJJ, SFZM, SFYM FROM funddb.JYRL WHERE JYRQ >= {} and JYRQ <= {} and " \
                     "SFJJ = 0".format(pre_date, self.end_date)
        res = hbs.db_data_query('readonly', sql_script, page_size=5000)
        df = pd.DataFrame(res['data']).rename(
            columns={"JYRQ": 'calendarDate', "SFJJ": 'isOpen',
                     "SFZM": "isWeekEnd", "SFYM": "isMonthEnd"}).sort_values(by='calendarDate')
        trading_day_list = df[df['isWeekEnd'] == '1']['calendarDate'].tolist()

        self.data = data.set_index(
            'trade_date').reindex(trading_day_list)[
            ['SZZS', 'SZ50', 'HS300', 'ZZ500', 'ZZ1000']].dropna(axis=0, how='all')

    def draw_picture_pe_ttm(self):
        index_pe = self.data.copy()
        func = lambda x: pd.Series(x).rank(pct=True).iloc[-1]
        n = self.window * 52

        rolling_pct = index_pe.rolling(window=n, center=False, min_periods=n).apply(func)
        df = rolling_pct[rolling_pct.index >= self.start_date].dropna(how='all').reset_index()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场宏观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='Market Valuation Quantile (%)',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside")
            ],
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        )

        index_name = {"SZ50": "上证50",
                      "HS300": "沪深300",
                      "ZZ500": "中证500",
                      "ZZ1000": "中证1000",
                      "SZZS": "上证指数"}

        for name in self.index_list:
            line.add_yaxis(
                series_name=index_name[name],
                y_axis=(100 * df[name]).round(1).tolist(),
                is_symbol_show=False,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(width=1.5),
                label_opts=opts.LabelOpts(is_show=False)
            )

        return line


class StockBondRotation:
    def __init__(self, index_name, start_date='20080101'):
        self.index_name = index_name
        self.start_date = start_date
        self._load_data()

    def _load_data(self):
        # 宽基指数PE数据(TTM)
        sql_script = "SELECT trade_date, {} FROM mac_stock_pe_ttm where trade_date >= {}".format(
            self.index_name, self.start_date)
        engine = create_engine(engine_params)
        pe_data = pd.read_sql(sql_script, engine)
        # 国债收益率数据
        sql_script = "SELECT trade_date, ytm_10y FROM mac_treasury_yield where trade_date >= {}".format(self.start_date)
        treasury_data = pd.read_sql(sql_script, engine)

        data = pd.merge(pe_data, treasury_data, on='trade_date').dropna()
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))
        data['premium'] = 1.0 / data[self.index_name] - 0.01 * data['ytm_10y']

        self.data = data

    def draw_picture_premium(self):
        df = self.data.copy()

        df_mean, df_std = round(df['premium'].mean(), 4), round(df['premium'].std(), 4)

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WALDEN
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场宏观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='Stock Premium',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="指数估值风险溢价",
            is_smooth=True,
            y_axis=df["premium"].round(4).tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='溢价均值+STD',
            y_axis=[round(df_mean + df_std, 4)] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='溢价均值',
            y_axis=[df_mean] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='溢价均值-STD',
            y_axis=[round(df_mean - df_std, 4)] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line


class StockIndexDiff:
    def __init__(self, start_date='20080101'):
        self.start_date = start_date
        self._init_api_params()
        self._load_data()

    def _init_api_params(self):
        self.url = 'http://fdc-query.intelnal.howbuy.com/query/data/commonapi?dataTrack=xxxxx'
        self.headers = {'Content-Type': 'application/json'}
        self.post_body = {"database": "readonly", "sql": None}

    def fetch_data_batch(self, sql_script):
        post_body = self.post_body.copy()
        post_body['sql'] = sql_script
        post_body["ifByPage"] = False
        res = requests.post(url=self.url, data=json.dumps(post_body), headers=self.headers).json()
        n = res['pages']
        all_data = []
        for i in range(1, n + 1):
            post_body["ifByPage"] = True
            post_body['pageNum'] = i
            res = requests.post(url=self.url, data=json.dumps(post_body), headers=self.headers).json()
            all_data.append(pd.DataFrame(res['data']))
        all_data = pd.concat(all_data)

        return all_data

    def _load_data(self):
        sql_script = "SELECT JYRQ, ZQDM, SPJG FROM funddb.ZSJY where " \
                     "ZQDM in ('000300', '000852') and JYRQ >= {}".format(self.start_date)
        index_data = self.fetch_data_batch(sql_script)
        index_data = pd.pivot_table(
            index_data, index='JYRQ', columns='ZQDM', values='SPJG').sort_index().pct_change().dropna()
        index_data.rename(columns={"000300": "HS300", "000852": "ZZ1000"}, inplace=True)

        index_data['HS300'] = (1 + index_data['HS300']).cumprod()
        index_data['ZZ1000'] = (1 + index_data['ZZ1000']).cumprod()
        index_data['diff'] = index_data['HS300'] - index_data['ZZ1000']

        self.index_data = index_data

    def draw_picture_index_diff(self):
        df = self.index_data.copy().reset_index()

        max_range_1 = int(df[['HS300', 'ZZ1000']].max().max()) + 1
        max_range_2 = int(df['diff'].abs().max()) + 1

        line1 = (
            Line(init_opts=opts.InitOpts(width='1200px', height='600px', theme=ThemeType.WESTEROS))
            .add_xaxis(
                xaxis_data=df['JYRQ'].tolist())
            .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    min_=-max_range_2,
                    max_=max_range_2,
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=False))
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="股票市场宏观"),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    min_=2 - max_range_1,
                    max_=max_range_1,
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    axistick_opts=opts.AxisTickOpts(is_show=True)),
            ).add_yaxis(
                series_name="沪深300",
                y_axis=df["HS300"].round(3).tolist(),
                is_symbol_show=False,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(width=1.8),
                label_opts=opts.LabelOpts(is_show=False)
            ).add_yaxis(
                series_name="中证1000",
                y_axis=df["ZZ1000"].round(3).tolist(),
                is_symbol_show=False,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(width=1.8),
                label_opts=opts.LabelOpts(is_show=False)
            )
        )

        line2 = (
            Line()
            .add_xaxis(
                xaxis_data=df['JYRQ'].tolist())
            .add_yaxis(
                series_name="大小盘剪刀差",
                is_smooth=True,
                y_axis=df["diff"].round(3).tolist(),
                is_symbol_show=False,
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
                yaxis_index=1
            )
        )
        line1.overlap(line2)

        return line1


class StockCashFlowIndex:
    def __init__(self, start_date='20200101'):
        self.start_date = start_date
        self._init_api_params()
        self._load_data()

    def _init_api_params(self):
        self.url = 'http://fdc-query.intelnal.howbuy.com/query/data/commonapi?dataTrack=xxxxx'
        self.headers = {'Content-Type': 'application/json'}
        self.post_body = {"database": "readonly", "sql": None}

    def fetch_data_batch(self, sql_script):
        post_body = self.post_body.copy()
        post_body['sql'] = sql_script
        post_body["ifByPage"] = False
        res = requests.post(url=self.url, data=json.dumps(post_body), headers=self.headers).json()
        n = res['pages']
        all_data = []
        for i in range(1, n + 1):
            post_body["ifByPage"] = True
            post_body['pageNum'] = i
            res = requests.post(url=self.url, data=json.dumps(post_body), headers=self.headers).json()
            all_data.append(pd.DataFrame(res['data']))
        all_data = pd.concat(all_data)

        return all_data

    def _load_data(self):
        sql_script = "SELECT * FROM mac_stock_cash_flow where TRADE_DATE >= {}".format(self.start_date)
        engine = create_engine(engine_params)
        cash_flow_df = pd.read_sql(sql_script, engine)
        cash_flow_df['trade_date'] = cash_flow_df['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))
        cash_flow_df['net_purchases'] = cash_flow_df['sh_net_purchases'] + cash_flow_df['sz_net_purchases']
        cash_flow_df = cash_flow_df[['trade_date', 'margin', 'net_purchases']]

        sql_script = "SELECT JYRQ, SFJJ, SFZM, SFYM FROM funddb.JYRL WHERE JYRQ >= {} and " \
                     "SFZM = 1".format(self.start_date)
        res = hbs.db_data_query('readonly', sql_script, page_size=5000)
        df = pd.DataFrame(res['data']).rename(
            columns={"JYRQ": 'calendarDate', "SFJJ": 'isOpen',
                     "SFZM": "isWeekEnd", "SFYM": "isMonthEnd"}).sort_values(by='calendarDate')
        trading_day_list = df['calendarDate'].tolist()

        sql_script = "SELECT JYRQ, ZQDM, SPJG FROM funddb.ZSJY where " \
                     "ZQDM = '000001' and JYRQ >= {}".format(self.start_date)
        index_data = self.fetch_data_batch(sql_script)
        index_data.rename(columns={"JYRQ": "trade_date"}, inplace=True)

        data = pd.merge(cash_flow_df, index_data[['trade_date', 'SPJG']], on='trade_date').fillna(0.)
        data['cum_purchases'] = data['net_purchases'].cumsum()
        data = data[data['trade_date'].isin(trading_day_list)]
        data['margin_diff'] = data['margin'].diff()
        data['hk_diff'] = data['cum_purchases'].diff()

        self.data = data.dropna()

    def draw_picture_cash_flow(self):
        df = self.data.copy()

        max_point = (int(df['SPJG'].max() / 500) + 1) * 500
        min_point = (int(df['SPJG'].min() / 500) - 1) * 500

        line1 = (
            Line(init_opts=opts.InitOpts(width='1200px', height='600px', theme=ThemeType.WALDEN))
            .add_xaxis(
                xaxis_data=df['trade_date'].tolist())
            .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    name="上证综指",
                    min_=min_point,
                    max_=max_point,
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=False))
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="股票市场宏观"),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%'),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    name="资金流向：(单位：亿元)",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    axistick_opts=opts.AxisTickOpts(is_show=True)),
            ).add_yaxis(
                series_name="北向资金",
                y_axis=df["hk_diff"].round(2).tolist(),
                is_symbol_show=True,
                symbol='rect',
                symbol_size=6,
                linestyle_opts=opts.LineStyleOpts(width=1.5),
                label_opts=opts.LabelOpts(is_show=False)
            ).add_yaxis(
                series_name="两融资金",
                y_axis=df["margin_diff"].round(2).tolist(),
                is_symbol_show=False,
                linestyle_opts=opts.LineStyleOpts(width=1.5, type_='dashed'),
                label_opts=opts.LabelOpts(is_show=False)
            )
        )

        line2 = (
            Line()
            .add_xaxis(
                xaxis_data=df['trade_date'].tolist())
            .add_yaxis(
                series_name="上证综指",
                y_axis=df["SPJG"].round(2).tolist(),
                is_symbol_show=False,
                linestyle_opts=opts.LineStyleOpts(width=1.5),
                label_opts=opts.LabelOpts(is_show=False),
                yaxis_index=1)
        )
        line1.overlap(line2)

        return line1


class StockTradingIndex:
    def __init__(self, window=3):
        self.window = window
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_stock_trading"
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))
        self.vix_data = data[['trade_date', 'VIX']].dropna()

        amt_data = data[['trade_date', 'amt_sh', 'amt_sz', 'amt_300', 'amt_500', 'amt_1000', 'amt_other']]
        amt_data['amt_all'] = amt_data['amt_sh'] + amt_data['amt_sz']
        end_date = amt_data['trade_date'].max()
        pre_date = str(int(end_date[:4]) - self.window) + end_date[4:6] + '01'
        amt_data = amt_data[amt_data['trade_date'] >= pre_date]
        self.amt_data = amt_data.dropna()

        turn_data = data[['trade_date', 'turn_sh', 'turn_sz', 'turn_300', 'turn_500', 'turn_1000']]
        end_date = turn_data['trade_date'].max()
        pre_date = str(int(end_date[:4]) - self.window) + end_date[4:6] + '01'
        turn_data = turn_data[turn_data['trade_date'] >= pre_date]
        self.turn_data = turn_data

    def draw_picture_vix(self):
        df = self.vix_data.copy()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场微观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='VIX Index (%)',
                name_location='middle',
                name_gap=45,
                name_textstyle_opts=opts.TextStyleOpts(color='grey', font_size=16),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside")]
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="VIX指数",
            is_smooth=True,
            y_axis=df["VIX"].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=2),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_amt(self, index_name):
        df = self.amt_data[['trade_date', 'amt_' + index_name]].copy()

        q1, med, q3 = df['amt_' + index_name].quantile(0.25), \
            df['amt_' + index_name].quantile(0.5), df['amt_' + index_name].quantile(0.75)

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场微观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='单位（亿元）',
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="成交额",
            is_smooth=True,
            y_axis=df["amt_" + index_name].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='25%分位',
            y_axis=[q1] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='中位数',
            y_axis=[med] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='75%分位',
            y_axis=[q3] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_picture_turn(self, index_name):
        df = self.turn_data[['trade_date', 'turn_' + index_name]].copy()

        q1, med, q3 = df['turn_' + index_name].quantile(0.25), \
            df['turn_' + index_name].quantile(0.5), df['turn_' + index_name].quantile(0.75)

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场微观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='单位：%',
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="换手率",
            is_smooth=True,
            y_axis=df["turn_" + index_name].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='25%分位',
            y_axis=[q1] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='中位数',
            y_axis=[med] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='75%分位',
            y_axis=[q3] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line


class StockCrossSectionVolIndex:
    def __init__(self, window=3):
        self.window = window
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_stock_cross_section_vol"
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))
        end_date = data['trade_date'].max()
        pre_date = str(int(end_date[:4]) - self.window) + end_date[4:6] + '01'
        data = data[data['trade_date'] >= pre_date]

        self.data = data

    def draw_picture_vol(self, index_name):
        df = self.data[['trade_date', index_name]].copy()
        df[index_name] = (df[index_name] * 100).round(2)

        q1, med, q3 = df[index_name].quantile(0.25), \
            df[index_name].quantile(0.5), df[index_name].quantile(0.75)

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场微观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='单位：%',
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name="截面波动率",
            is_smooth=True,
            y_axis=df[index_name].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='25%分位',
            y_axis=[q1] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='中位数',
            y_axis=[med] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='75%分位',
            y_axis=[q3] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line


class StockTimeSeriesVolIndex:
    def __init__(self, window=3, days=20):
        self.window = window
        self.days = days
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_stock_time_series_vol"
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))
        end_date = data['trade_date'].max()
        pre_date = str(int(end_date[:4]) - self.window) + end_date[4:6] + '01'
        data = data[data['trade_date'] >= pre_date]

        if self.days == 20:
            data = data.set_index('trade_date').filter(regex="_20d").reset_index()
        else:
            data = data.set_index('trade_date').filter(regex='_5d').reset_index()

        self.data = data

    def draw_picture_vol(self, index_name):
        df = self.data[['trade_date', index_name + '_' + str(self.days) + 'd']].copy()
        df.rename(columns={index_name + '_' + str(self.days) + 'd': index_name}, inplace=True)
        df[index_name] = (df[index_name] * 100).round(2)

        q1, med, q3 = df[index_name].quantile(0.25), \
            df[index_name].quantile(0.5), df[index_name].quantile(0.75)

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场微观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name='单位：%',
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()
        ).add_yaxis(
            series_name=str(self.days) + "日时序波动率",
            is_smooth=True,
            y_axis=df[index_name].tolist(),
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='25%分位',
            y_axis=[q1] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='中位数',
            y_axis=[med] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name='75%分位',
            y_axis=[q3] * df.shape[0],
            is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(type_='dashed', width=1.8),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line


class StockTradingCrIndex:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_stock_trading_cr WHERE TRADE_DATE >= {} and TRADE_DATE <= {}".format(
            self.start_date, self.end_date)
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))

        self.data = data[['trade_date', 'cr5', 'cr10', 'avg_mkt', 'close']]

    def draw_cr_picture(self):
        df = self.data.copy()
        df['cr5'] *= 100
        df['cr10'] *= 100

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WESTEROS
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场微观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                is_inverse=True,
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                min_='dataMin',
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(formatter="{value} %"),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside")
            ],
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()[::-1]
        ).add_yaxis(
            series_name="前5%个股成交额集中度",
            y_axis=df["cr5"].round(1).tolist()[::-1],
            is_symbol_show=False,
            is_smooth=True,
            linestyle_opts=opts.LineStyleOpts(width=1.5),
            label_opts=opts.LabelOpts(is_show=False)
        ).add_yaxis(
            series_name="前10%个股成交额集中度",
            y_axis=df["cr10"].round(1).tolist()[::-1],
            is_symbol_show=False,
            is_smooth=True,
            linestyle_opts=opts.LineStyleOpts(width=1.5),
            label_opts=opts.LabelOpts(is_show=False)
        )

        return line

    def draw_avg_picture(self):
        df = self.data.copy()

        line = Line(
            init_opts=opts.InitOpts(
                width='1200px',
                height='600px',
                theme=ThemeType.WALDEN
            )
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="股票市场微观"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
            xaxis_opts=opts.AxisOpts(
                type_='category',
                is_inverse=True,
                axistick_opts=opts.AxisTickOpts(is_show=True, is_align_with_label=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axisline_opts=opts.AxisLineOpts(on_zero_axis_index=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                min_='dataMin',
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(formatter="{value} 亿")
            ),
            datazoom_opts=[
                opts.DataZoomOpts(range_start=0, range_end=100),
                opts.DataZoomOpts(type_="inside")
            ],
        ).add_xaxis(
            xaxis_data=df['trade_date'].tolist()[::-1]
        ).add_yaxis(
            series_name="成交额加权市值",
            y_axis=df["avg_mkt"].round(1).tolist()[::-1],
            is_symbol_show=False,
            is_smooth=True,
            linestyle_opts=opts.LineStyleOpts(width=1.5),
            label_opts=opts.LabelOpts(is_show=False)
        ).extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                min_='dataMin',
                axistick_opts=opts.AxisTickOpts(is_show=True))
        )

        line2 = (
            Line()
            .add_xaxis(xaxis_data=df['trade_date'].tolist())
            .add_yaxis(
                series_name="上证综指",
                yaxis_index=1,
                y_axis=df["close"].round(1).tolist(),
                is_symbol_show=False,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(width=1.5),
                label_opts=opts.LabelOpts(is_show=False))
        )

        return line.overlap(line2)


"=====================================================债券市场宏微观======================================================"


class TreasurySpreadIndex:
    def __init__(self, start_date='20080104', end_date='20300101'):
        self.start_date = start_date
        self.end_date = end_date
        self._load_data()

    def _load_data(self):
        sql_script = "SELECT * FROM mac_treasury_yield WHERE TRADE_DATE >= {} and TRADE_DATE <= {}".format(
            self.start_date, self.end_date)
        engine = create_engine(engine_params)
        data = pd.read_sql(sql_script, engine)
        data['trade_date'] = data['trade_date'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))

        self.data = data

    def draw_picture_treasury_spread(self):
        df = self.data[['trade_date', 'ytm_10y', 'usa_ytm_10y']].dropna()
        df['diff'] = df['ytm_10y'] - df['usa_ytm_10y']

        line = (
            Line(init_opts=opts.InitOpts(width='1200px', height='600px', theme=ThemeType.WESTEROS))
            .add_xaxis(
                xaxis_data=df['trade_date'].tolist())
            .set_global_opts(
                title_opts=opts.TitleOpts(title="债券市场宏观"),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    name="单位：%",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    axistick_opts=opts.AxisTickOpts(is_show=True)),
            ).add_yaxis(
                series_name="中国国债收益率：10年",
                y_axis=df["ytm_10y"].round(3).tolist(),
                is_symbol_show=False,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(width=1.8),
                label_opts=opts.LabelOpts(is_show=False)
            ).add_yaxis(
                series_name="美国国债收益率：10年",
                y_axis=df["usa_ytm_10y"].round(3).tolist(),
                is_symbol_show=False,
                is_smooth=True,
                linestyle_opts=opts.LineStyleOpts(width=1.8),
                label_opts=opts.LabelOpts(is_show=False)
            ).add_yaxis(
                series_name="中美国债利差：中国-美国",
                is_smooth=True,
                y_axis=df["diff"].round(3).tolist(),
                is_symbol_show=False,
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False)
            )
        )

        return line

    def draw_picture_treasury_yield(self, date, compare_date=None):
        df = self.data[['trade_date', 'ytm_6m', 'ytm_1y', 'ytm_2y', 'ytm_3y', 'ytm_5y', 'ytm_7y',
                        'ytm_10y', 'ytm_15y', 'ytm_20y', 'ytm_30y']].set_index('trade_date')
        if compare_date is None:
            df = df.loc[date]
            df.index.name = 'duration'
            df = df.to_frame('yield').reset_index()
            df['duration'] = df['duration'].replace('ytm_6m', 'ytm_0.5y').apply(
                lambda x: float(x.split('_')[-1][:-1]))

            line = (
                Line(init_opts=opts.InitOpts(width='1200px', height='600px', theme=ThemeType.WESTEROS))
                .add_xaxis(
                    xaxis_data=df['duration'].tolist())
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="债券市场微观"),
                    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                    legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
                    yaxis_opts=opts.AxisOpts(
                        type_="value",
                        name="单位：%",
                        min_=1,
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    ),
                    xaxis_opts=opts.AxisOpts(
                        type_="value",
                        axistick_opts=opts.AxisTickOpts(is_show=True)),
                ).add_yaxis(
                    series_name="国债到期收益率",
                    y_axis=df['yield'].tolist(),
                    # is_symbol_show=False,
                    # is_smooth=True,
                    linestyle_opts=opts.LineStyleOpts(width=1.8),
                    label_opts=opts.LabelOpts(is_show=False)
                )
            )
        else:
            df = df.loc[[date, compare_date]].T.reset_index()
            df.rename(columns={"index": "duration"}, inplace=True)
            df['duration'] = df['duration'].replace('ytm_6m', 'ytm_0.5y').apply(
                lambda x: float(x.split('_')[-1][:-1]))

            line = (
                Line(init_opts=opts.InitOpts(width='1200px', height='600px', theme=ThemeType.WESTEROS))
                .add_xaxis(
                    xaxis_data=df['duration'].tolist())
                .set_global_opts(
                    title_opts=opts.TitleOpts(title="债券市场微观"),
                    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                    legend_opts=opts.LegendOpts(pos_right="center", pos_top='5%', legend_icon='circle'),
                    yaxis_opts=opts.AxisOpts(
                        type_="value",
                        name="单位：%",
                        min_=1,
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    ),
                    xaxis_opts=opts.AxisOpts(
                        type_="value",
                        name="单位：年",
                        axistick_opts=opts.AxisTickOpts(is_show=True)),
                ).add_yaxis(
                    series_name="国债到期收益率: {}".format(date),
                    y_axis=df[date].tolist(),
                    # is_symbol_show=False,
                    # is_smooth=True,
                    linestyle_opts=opts.LineStyleOpts(width=1.8),
                    label_opts=opts.LabelOpts(is_show=False)
                ).add_yaxis(
                    series_name="国债到期收益率: {}".format(compare_date),
                    y_axis=df[compare_date].tolist(),
                    # is_symbol_show=False,
                    # is_smooth=True,
                    linestyle_opts=opts.LineStyleOpts(width=1.8),
                    label_opts=opts.LabelOpts(is_show=False)
                )
            )

        return line


if __name__ == '__main__':
    # CurrencyIndex().draw_picture_M1_M2()
    # CreditIndex(frequency='week').draw_picture_indu()
    # InflationIndex().draw_picture()
    # EconomyIncreaseIndex().draw_picture_gdp()
    # StockMarketPE(window=5, index_list=['HS300', 'ZZ500'], start_date='20140101').draw_picture_pe_ttm()
    # StockBondRotation(index_name='HS300', start_date='20150101').draw_picture_premium()
    # StockIndexDiff(start_date='20190101').draw_picture_index_diff()
    # StockCashFlowIndex(start_date='20200101').draw_picture_cash_flow()
    # StockTradingIndex().draw_picture_amt('all')
    # StockCrossSectionVolIndex().draw_picture_vol('HS300')
    # StockTimeSeriesVolIndex().draw_picture_vol('HS300')
    # StockTradingCrIndex('20190101', '20210423')
    TreasurySpreadIndex().draw_picture_treasury_yield('20210423', '20210416')
