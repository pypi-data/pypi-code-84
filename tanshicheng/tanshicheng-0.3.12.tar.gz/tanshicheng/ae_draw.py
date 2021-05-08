import colorsys
import copy
import math
import os
import random

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.text import Text
from matplotlib.transforms import Affine2D
from mpl_toolkits.mplot3d import Axes3D


class Draw:
    def __init__(self, length=10, width=10, r=1, c=1, wspace=None, num=None):
        '''
        :param length: float; 图片的长度, 单位一般是100像素
        :param width: float; 图片的宽度/高度, 单位一般是100像素
        :param r: int; 几行
        :param c: int; 几列
        :param wspace: None or float; 子图之间的距离, 0.4表示为子图宽度的40%
        :param num: None or int or str; fig的名称, 防止有时重合
        :return:
        '''
        self.fig = plt.figure(num=num, figsize=(length, width))
        self.r = r
        self.c = c
        self.fig.subplots_adjust(wspace=wspace)
        self.markers_L = ['.', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                          '|', '']  # 点的形状

    def add_radar(self, x_labels, line_labels, line_data, sub_title='', ylim=(None, None), linewidth=1, markersize=4,
                  fix_marker='.', fix_linestyle='-.', sub_title_fs=None, n=1, set_legend=(0.95, .9), fill_alpha=0,
                  frame='polygon', radii=None, title_pad=None):
        """
        增加一个雷达图绘制
        :param x_labels: [标签名,..]
        :param line_labels: [第一个线的名称,..]
        :param line_data: [[第一个线的第一个值],..]
        :param sub_title: str; 这个子图的标题
        :param ylim: [最小值,最大值]; y轴范围, 如果是None则自动计算
        :param linewidth: float; 点间连线的宽度
        :param markersize: float; 点的大小
        :param fix_marker: None or str; 是否固定点的形状, None表示固定, str表示自己选择所有点的形状
        :param fix_linestyle: None or str; 是否固定点间连线的形状, None表示固定, str表示自己选择所有的形状
        :param sub_title_fs: None or int; 这个子图的标题的字体大小, None默认
        :param n: int; 第几个图, 从1开始, 先行后列
        :param set_legend: None, str or (float,float); 设置图例位置loc, None表示不绘制, 'best' 自动绘制可能重叠
        :param fill_alpha: None or float; 是否填充多边形, 如果在(0,1]之间便作为透明度填充, eps图片会失效透明度
        :param frame: 'circle' or 'polygon'; 雷达图形状, polygon 在 matplotlib==3.2.3 及之后无用
        :param radii: None or list; 是否手动绘制网格线, 比如 (0, 0.2, 0.4, 0.6, 0.8, 1), None表示使用自动的
        :param title_pad: None or int; 标题离图的距离
        :return:
        """
        # 初始化
        if frame == 'polygon':
            angles = self.radar_factory(len(x_labels), frame=frame)
            ax = self.fig.add_subplot(self.r, self.c, n, projection='radar')
            ax.set_varlabels(x_labels)
        else:
            ax = self.fig.add_subplot(self.r, self.c, n, projection='polar')
            # 角度, 理解为x轴
            angles = np.linspace(0, 2 * np.pi, len(x_labels), endpoint=False)
            ax.set_thetagrids(angles * 180 / np.pi, x_labels)  # 设置x轴, 放这兼容 matplotlib-3.4.1
            angles = np.hstack((angles, [angles[0]]))
            # 直线首位相连
            line_data = copy.deepcopy(line_data)
            for line in line_data:
                assert len(line) == len(x_labels), f'line_data和x_labels长度不符合! line:{line}, x_labels:{x_labels}'
                line.append(line[0])
        assert len(line_data) == len(line_labels), 'line_labels数量和line_data直线数量不符合!'
        # 每条直线默认参数
        if fix_marker:
            markers_L = [fix_marker] * len(line_labels)
        else:
            markers_L = self.markers_L * len(line_labels)
        if fix_linestyle:
            linestyles_L = [fix_linestyle] * len(line_labels)
        else:
            linestyles_L = ['--', '-.', ':'] * len(line_labels)
        nc_L = self.ncolors(len(line_labels))
        # 绘图
        for label, line, linestyle, c, marker in zip(line_labels, line_data, linestyles_L, nc_L, markers_L):
            ax.plot(angles, line, linewidth=linewidth, linestyle=linestyle, markersize=markersize, c=c, marker=marker,
                    mfc='None', label=label)
            if fill_alpha and 0 < fill_alpha <= 1:
                ax.fill(angles, line, facecolor=c, alpha=fill_alpha)
        # 设置y轴
        line_data_ = np.array(line_data)
        ylim = list(ylim)
        if ylim[0] is None:
            ylim[0] = line_data_.min()
        if ylim[1] is None:
            ylim[1] = line_data_.max()
        ylim.sort()
        ax.set_ylim(*ylim)
        # 设置网格
        if radii:
            ax.set_rgrids(radii)  # 网格间隔
        ax.grid(True, linestyle=':', which='major')
        # 设置标题
        ax.set_title(sub_title, fontsize=sub_title_fs, pad=title_pad)
        # 设置图例
        if set_legend is not None:
            ax.legend(loc=set_legend, labelspacing=0.)
        # ax.set_rasterized(True)  # 防止eps透明度不行, 但是光栅化不清晰

    def add_3d(self, xyz_L=None, x_num=None, y_num=None, xyz_scatter=None, scatter_labels=None, xlabel='X', ylabel='Y',
               zlabel='Z', cmap='rainbow', sub_title='', sub_title_fs=None, x_multiple=None, y_multiple=None,
               interp_kind='cubic', scatter_ms=4, scatter_marker=None, n=1, colorbar_pad=0.05, surf_alpha=0.95,
               scatter_c='black', elev=None, azim=None, stretch=(1, 1, 1, 1), colorbar=True):
        """
        增加一个3d透视图, 可以包括曲面和散点
        :param xyz_L: None or [(x,y,z),..]; 曲面上的点, None则不绘制曲面
        :param x_num: None or int; 曲面的x采样数量, None则自动计算, 尽量接近x更长正方形
        :param y_num: None or int; 曲面的y采样数量, None则自动计算, 尽量接近x更长正方形
        :param xyz_scatter: None or [[(x,y,z),..],..]; 要绘制的散点, 一个标签对应一个点列表
        :param scatter_labels: None or ['标签名',..]; 散点的标签名, 顺序与xyz_scatter一致
        :param xlabel: str or None; x轴名, None表示无
        :param ylabel: str or None; y轴名, None表示无
        :param zlabel: str or None; z轴名, None表示无
        :param cmap: str; 曲面渐变色种类, 比如 rainbow/coolwarm
        :param sub_title: str; 这个子图的标题
        :param sub_title_fs: None or int; 这个子图的标题的字体大小, None默认
        :param x_multiple: None or int; 曲面采样数的插值扩充倍数, x横向变细腻, 最终采样数量=2^(x_multiple-1)*(x_num-1)-1
            None 表示一个边最终采样数量大约限制在200次以上, 1表示不扩充
        :param y_multiple:  None or int; 曲面采样数的插值扩充倍数, y纵向变细腻, 最终采样数量=2^(x_multiple-1)*(x_num-1)-1
            None 表示一个边最终采样数量大约限制在200次以上, 1表示不扩充
        :param interp_kind: str; Z轴插值扩充方式, 比如 cubic/linear/nearest
        :param scatter_ms: int; 散点的大小
        :param scatter_marker: None or str; 是否固定散点的形状, None表示固定, str表示自己选择所有散点的形状
        :param n: int; 第几个图, 从1开始, 先行后列
        :param colorbar_pad: float; 曲面颜色条离Z轴名左侧的距离比例
        :param surf_alpha: float; 曲面透明度
        :param scatter_c: None or str; 是否固定散点的颜色, None表示自动选择不同的颜色, str表示自己选择所有散点固定的颜色
        :param elev: None or float; 视角, z轴仰角, None是默认, 一般可能是30度
        :param azim: None or float; 视角, xy平面旋转角度, None是默认, 45度可以把z轴标记放在左边
        :param stretch: (float,float,float,float); (x轴,y轴,z轴,总体)的拉伸程度, 值是1表示不拉伸
        :param colorbar: bool; 是否绘制颜色条
        :return:
        """
        ax = self.fig.add_subplot(self.r, self.c, n, projection='3d')
        if xyz_L:
            # 设置 x_num 和 y_num
            if x_num is None and y_num is None:
                def crack(integer):  # 把一个数分解为最接近的两个整数的乘积
                    start = int(integer ** 0.5)
                    factor = integer / start
                    while int(factor) != factor:
                        start += 1
                        factor = integer / start
                    return int(factor), start

                x_num, y_num = crack(len(xyz_L))
                assert x_num != 1 and y_num != 1, f'点的数量不能构成长方形! {x_num} == 1 or {y_num} == 1'
            if x_num is None:
                x_num = int(len(xyz_L) / y_num)
            if y_num is None:
                y_num = int(len(xyz_L) / x_num)
            assert len(xyz_L) == x_num * y_num, f'三元组数量和矩阵不同! {len(xyz_L)} != {x_num} * {y_num}'
            # 构建曲面点
            xyz_L = sorted(xyz_L)  # 按x排序, 不同的x分段不会相交
            xyz_L_L = np.array([  # [[(x,y,z),..],..]; 每列x中的y进行排序, 不同的x对应的y可能相交
                sorted(xyz_L[i * y_num: (i + 1) * y_num], key=lambda t: t[1:]) for i in range(x_num)
            ])
            X = xyz_L_L[:, :, 0]
            Y = xyz_L_L[:, :, 1]
            Z = xyz_L_L[:, :, 2]
            # 默认放大倍率
            if x_multiple is None:
                x_multiple = int(math.log2(200 / (x_num - 1))) + 1
            if y_multiple is None:
                y_multiple = int(math.log2(200 / (y_num - 1))) + 1
            # 放大倍率
            for i in range(1, x_multiple):  # x横向变细腻
                # x坐标
                X = X.repeat(2, 0)  # 每个x重复
                X = (X[1:, :] + X[:-1, :]) / 2  # 错位相加平均
                # y坐标
                Y = Y.repeat(2, 0)
                Y = (Y[1:, :] + Y[:-1, :]) / 2
            for i in range(1, y_multiple):  # y纵向变细腻
                X = X.repeat(2, 1)
                X = (X[:, 1:] + X[:, :-1]) / 2
                Y = Y.repeat(2, 1)
                Y = (Y[:, 1:] + Y[:, :-1]) / 2
            # 插值Z
            if X.shape != Z.shape:
                xyz_L_numpy = np.array(xyz_L)
                Z = griddata(xyz_L_numpy[:, 0:2], xyz_L_numpy[:, 2], (X, Y), method=interp_kind)
                Z_isnan = np.isnan(Z)
                if Z_isnan.sum() > 0:
                    print(f'add_3d({n}): Z存在nan被替换')
                    Z_nonan = griddata(xyz_L_numpy[:, 0:2], xyz_L_numpy[:, 2], (X, Y), method='nearest')
                    Z[Z_isnan] = Z_nonan[np.where(Z_isnan)]  # nan替换为nearest
            # 绘制曲面
            surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap(cmap), alpha=surf_alpha)
            # 绘制颜色条
            if colorbar:
                self.fig.colorbar(surf, shrink=0.5, aspect=30, pad=colorbar_pad, use_gridspec=True)
        # 构建散点图
        if xyz_scatter and scatter_labels:
            assert len(xyz_scatter) == len(scatter_labels), \
                f'3D散点图的种数和标签数量不匹配! {len(xyz_scatter)} != {len(scatter_labels)}'
            # 每个点默认参数
            if scatter_marker:
                markers_L = [scatter_marker] * len(xyz_scatter)
            else:
                markers_L = self.markers_L * len(xyz_scatter)
            if scatter_c:
                nc_L = [scatter_c] * len(xyz_scatter)
            else:
                nc_L = self.ncolors(len(xyz_scatter))
            # 绘图
            for xyz, label, c, marker in zip(xyz_scatter, scatter_labels, nc_L, markers_L):
                xyz = np.array(xyz)
                ax.scatter3D(xyz[:, 0], xyz[:, 1], xyz[:, 2], c=c, s=scatter_ms, label=label, marker=marker)
            # 图例
            ax.legend(loc='best', labelspacing=0.)
        # 设置标题
        ax.set_title(sub_title, fontsize=sub_title_fs, pad=20)
        # 设置坐标轴标签
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        # 视角
        ax.view_init(elev=elev, azim=azim)
        # 轴长度拉伸, [x,y,z,总体]
        ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag(stretch))

    def add_violin(self, all_data, xaxis_name, xlabel_name=None, ylabel_name=None, ygrid_alpha=0.4, title=None,
                   diff_color=True, violin_width=0.7, violin_alpha=0.2, n=1, x_rotation=None):
        '''
        增加一个小提琴图绘制
        :param all_data: [[数据1值1,..],..]; 二维列表, 每行一个数据
        :param xaxis_name: [名称1,..]; 每个数据的名称
        :param xlabel_name: str or None; x轴坐标名称
        :param ylabel_name: str or None; y轴坐标名称
        :param ygrid_alpha: float; y轴网格的不透明度
        :param title: str or None; 标题
        :param diff_color: bool; 是否每个violin不同颜色
        :param violin_width: float; 每个violin的宽度, 百分比
        :param violin_alpha: float; violin的不透明度
        :param n: int; 第几个图, 从1开始, 先行后列
        :param x_rotation: None or float; x轴标签名称逆时针旋转度数, None表示不旋转
        :return:
        '''
        # 初始化
        axes = self.fig.add_subplot(self.r, self.c, n)
        violin_parts = axes.violinplot(all_data, showmeans=True, showmedians=True, widths=violin_width)
        # 每个图设置不同颜色
        nc = self.ncolors(len(all_data))
        for i, pc in enumerate(violin_parts['bodies']):
            if diff_color:
                pc.set_facecolor(nc[i])  # 中间颜色
                pc.set_edgecolor('black')  # 边界颜色
            pc.set_alpha(violin_alpha)  # 透明度
        # violinplot 横线颜色
        violin_parts['cmeans'].set_color(['red'] * len(all_data))
        violin_parts['cmins'].set_color(['green'] * len(all_data))
        violin_parts['cmaxes'].set_color(['black'] * len(all_data))
        violin_parts['cmedians'].set_color(['blue'] * len(all_data))
        # violinplot 图例
        violin_parts['cmeans'].set_label('Mean')
        violin_parts['cmins'].set_label('Min')
        violin_parts['cmaxes'].set_label('Max')
        violin_parts['cmedians'].set_label('Median')
        # 参数设置
        if title:  # 标题
            axes.set_title(title)
        if 0 < ygrid_alpha <= 1:  # 网格设置
            axes.yaxis.grid(True, alpha=ygrid_alpha)
        if xlabel_name:  # 横坐标设置
            axes.set_xlabel(xlabel_name)
        if ylabel_name:  # 纵坐标设置
            axes.set_ylabel(ylabel_name)
        plt.setp(axes, xticks=range(1, len(all_data) + 1), xticklabels=xaxis_name)  # 横坐标图名称
        if x_rotation:
            plt.setp(axes.get_xticklabels(), rotation=x_rotation, horizontalalignment='right')
        if diff_color:
            [t.set_color(i) for (i, t) in zip(nc, axes.xaxis.get_ticklabels())]
        axes.legend(loc='best', labelspacing=0.)  # 图例

    def add_line(self, x, xticks=None, xaxis: str = None, xlim: list = None, title: str = None, ylabel_display=True,
                 y_left: list = None, yaxis_left: str = None, ylim_left: list = None, ylabel_left: list = None,
                 y_right: list = None, yaxis_right: str = None, ylim_right: list = None,
                 ylabel_right: list = None,
                 y_left_ls='-', y_right_ls='--',
                 grid_ls_x='', grid_axis_yl=False, grid_axis_yr=False, grid_alpha=0.4,
                 annotate=True, annotate_in_left=True, annotate_color=True, legend_right=True,
                 xl_text_margin=0.1, xl_arrow_len=0.3, xr_text_margin=0.05, xr_arrow_len=0.3, custom_dpi=90,
                 length=10, width=10, lw=1, ytext_min_gap=0.25, markersize=4, n=1, x_rotation=None):
        '''
        增加一个折线图, 可以标记/双y轴, 所有折线共用x轴.
        代码修改建议:
            - 点的中心颜色可以修改
            - annotate 箭头默认颜色可修改
            - 空出图例的位置 可能需要修改 标签的长度/label_len
        :param x: [float,..]; x轴坐标, 一维列表, 所有折线共用, 必选
        :param xticks: ['x第一个标记',..] or None; x轴每个值用str替换, None表示不替换
        :param xaxis: str or None; x轴的名字
        :param xlim: [left,right] or None; x轴的左右限制
        :param title:  str or None; 标题
        :param x_rotation: None or float; x轴标签名称逆时针旋转度数, None表示不旋转

        :param y_left: [[..],..] or None; 左y轴坐标, 二维列表, 必选
        :param yaxis_left: str or None; 左y轴的名字
        :param ylim_left: [left,right] or None; 左y轴的左右限制. left,right 可为None自动限制y最大值. 设置太小会自动放大
        :param ylabel_left: [str,..] or None; 左y轴每条折线的标签
        :param y_right: [[..],..] or None; 右y轴坐标, 二维列表
        :param yaxis_right: str or None; 右y轴的名字
        :param ylim_right: [left,right] or None; 右y轴的左右限制. left,right 可为None自动限制y最大值. 设置太小会自动放大
        :param ylabel_right: [str,..] or None; 右y轴每条折线的标签
        :param y_left_ls: str; 左y轴/左标记箭头/左y轴网格 的折线风格 ['-','--','-.',':']
        :param y_right_ls: str; 右y轴/右标记箭头/右y轴网格 的折线风格
        :param ylabel_display: bool, 是否显示每条折线的标签(图例,legend)

        :param grid_ls_x: str or None; 网格x轴的折线风格, 空则不绘制x轴网格
        :param grid_axis_yl: bool; 是否绘制左y轴的网格
        :param grid_axis_yr: bool; 是否绘制右y轴的网格
        :param grid_alpha: float; 网格的不透明度

        :param annotate: bool; 是否标记. 标记则 xlim 无效
        :param annotate_in_left: bool; 左y轴是否标记在左侧, 否则右y轴标记在左侧
        :param annotate_color: bool; 标记是否使用折线标签的颜色
        :param legend_right: bool; 是否在右侧自动空出图例的位置, 需要 annotate,ylabel_display=True. 可通过调 xr_text_margin=1 替代

        和字体大小有关, 字体大以下值可能也要大:
        :param xl_text_margin: float; 左侧标记离左y轴的距离, 单位基本与 length 相同
        :param xl_arrow_len: float; 左标记箭头长度, 单位基本与 length 相同
        :param xr_text_margin: float; 右侧标记离右y轴的距离, 单位基本与 length 相同, 小心和 legend_right 重复拉大边距
        :param xr_arrow_len: float; 右标记箭头长度, 基本与 length 相同
        :param custom_dpi: float; 基本与 length 相同的单位, 稍稀疏一些. 如果标记文本过长则可以适当减小这个数值
        :param ytext_min_gap: float; 上下标记之间的最小中心(非边缘)距离, 单位基本与 length 相同

        :param length: float; 图片的长度, 单位一般是100像素
        :param width: float; 图片的宽度/高度, 单位一般是100像素
        :param lw: float; 折线的线条宽度
        :param markersize: float; 点大小
        :param n: int; 第几个图, 从1开始, 先行后列
        :return:
        '''
        assert (y_left is not None) and (len(y_left) > 0), 'y_left 不能为空!'
        assert len(x) == len(y_left[0]), 'x 与 y_left[0] 长度不相等! %d!=%d' % (len(x), len(y_left[0]))
        assert len(y_left[0]) == sum([len(i) for i in y_left]) / len(y_left), 'y_left 每行长度不相等!'
        assert not isinstance(y_left[0][0], list), 'y_left 必须是二维矩阵! ' + str(y_left)
        # 允许的点的形状, 按顺序取的, 可修改
        markers = self.markers_L * 10
        mfc = ['None'] * len(markers)  # 点的中间颜色, 数量与markers相等
        # 全图配置
        text_obj = Text()
        get_text_w = lambda t: self.get_text_width(t, self.fig, text_obj)  # 获取字符像素宽度
        ax_left = self.fig.add_subplot(self.r, self.c, n)
        all_polt = []  # 所有图, 用于绘制图例
        # 左右坐标 配置信息
        colors = self.ncolors((len(y_left) if y_left else 0) + (len(y_right) if y_right else 0))  # 颜色
        colors_left = colors[:len(y_left) if y_left else 0]  # 左 颜色
        colors_right = colors[len(colors_left):]  # 右 颜色
        assert len(colors) <= len(markers), '线条数量(%d)不能超过点的形状数量(%d)!' % (len(colors), len(markers))
        markers_left = markers[:len(colors_left)]  # 左 点形状
        mfc_left = mfc[:len(colors_left)]
        markers_right = markers[len(colors_left): len(colors)]  # 右 点形状
        mfc_right = mfc[len(colors_left): len(colors)]
        # y_left 绘制
        if ylabel_left is not None and len(ylabel_left) > 0:  # 处理标签
            assert len(ylabel_left) == len(y_left), 'ylabel_left 和 y_left 长度不相等! %d!=%d' % (
                len(ylabel_left), len(y_left))
        else:
            ylabel_left = None
        for i, y in enumerate(y_left):  # 开始绘制
            if ylabel_left:
                label = ylabel_left[i]
            else:
                label = None
            lns = ax_left.plot(x, y, c=colors_left[i], label=label, markersize=markersize,
                               marker=markers_left[i], mfc=mfc_left[i], lw=lw, ls=y_left_ls)
            if label:  # 如果有标签
                all_polt += lns
        if yaxis_left:  # 坐标轴名称
            ax_left.set_ylabel(yaxis_left)
        if ylim_left:  # 坐标轴约束
            assert len(ylim_left) == 2, 'ylim_left 数量错误! %s' % str(ylim_left)
            yy = sum(y_left, [])
            y_min, y_max = min(yy), max(yy)
            if ylim_left[0] is None or ylim_left[0] > y_min:
                ylim_left[0] = y_min
            if ylim_left[1] is None or ylim_left[1] < y_max:
                ylim_left[1] = y_max
            assert ylim_left[0] < ylim_left[1], 'ylim_left 大小错误! %s' % str(ylim_left)
            ax_left.set_ylim(*ylim_left)
        # y_right 绘制
        ax_right = None
        if y_right is not None and len(y_right) > 0:
            assert len(x) == len(y_right[0]), 'x 与 y_right[0] 长度不相等! %d!=%d' % (len(x), len(y_right[0]))
            assert len(y_right[0]) == sum([len(i) for i in y_right]) / len(y_right), 'y_right 每行长度不相等!'
            assert not isinstance(y_right[0][0], list), 'y_right 必须是二维矩阵! ' + str(y_right)
            if ylabel_right is not None and len(ylabel_right) > 0:  # 处理标签
                assert len(ylabel_right) == len(y_right), \
                    'ylabel_right 和 y_right 长度不相等! %d!=%d' % (len(ylabel_right), len(y_right))
            else:
                ylabel_right = None
            ax_right = ax_left.twinx()
            for i, y in enumerate(y_right):  # 开始绘制
                if ylabel_right:
                    label = ylabel_right[i]
                else:
                    label = None
                lns = ax_right.plot(x, y, c=colors_right[i], label=label, markersize=markersize,
                                    marker=markers_right[i], mfc=mfc_right[i], lw=lw, ls=y_right_ls)
                if label:  # 如果有标签
                    all_polt += lns
            if yaxis_right:  # 坐标轴名称
                ax_right.set_ylabel(yaxis_right)
            if ylim_right:  # 坐标轴约束
                assert len(ylim_right) == 2, 'ylim_right 数量错误! %s' % str(ylim_right)
                yy = sum(y_right, [])
                y_min, y_max = min(yy), max(yy)
                if ylim_right[0] is None or ylim_right[0] > y_min:
                    ylim_right[0] = y_min
                if ylim_right[1] is None or ylim_right[1] < y_max:
                    ylim_right[1] = y_max
                assert ylim_right[0] < ylim_right[1], 'ylim_right 大小错误! %s' % str(ylim_right)
                ax_right.set_ylim(*ylim_right)
        # 标记
        if annotate:
            if annotate_in_left:
                yl_annotate_left = True  # y_left 是否标记在左边
                yl_annotate_right = False  # y_left 是否标记在右边
                yr_annotate_left = False  # y_right 是否标记在左边
                yr_annotate_right = True  # y_right 是否标记在右边
            else:  # 不可能两边都有同一条线的标记
                yl_annotate_left = False
                yl_annotate_right = True
                yr_annotate_left = True
                yr_annotate_right = False
        else:
            yl_annotate_left = yl_annotate_right = yr_annotate_left = yr_annotate_right = False
        if yl_annotate_left or yl_annotate_right:
            assert r'\n' not in str(ylabel_left), '标记时 ylabel_left 不允许存在换行符号!'  # 防止字体宽度和间隔判断错误
        if yr_annotate_left or yr_annotate_right:
            assert r'\n' not in str(ylabel_right), '标记时 ylabel_right 不允许存在换行符号!'
        # 计算左右标记和双y轴的关系
        if (yl_annotate_left and ylabel_left) or (yr_annotate_left and y_right and ylabel_right):
            annotate_left = True  # 左侧标记
        else:
            annotate_left = False
        if (yl_annotate_right and ylabel_left) or (yr_annotate_right and y_right and ylabel_right):
            annotate_right = True  # 右侧标记
        else:
            annotate_right = False
        x_min, x_max = min(x), max(x)
        # 计算y轴标记目标点位置/颜色
        name_y_left = []  # [[标记名称,目标点y轴坐标,标记文本位置,颜色],..], 左侧标记
        name_y_right = []  # [[标记名称,目标点y轴坐标,标记文本位置,颜色],..], 右侧标记
        i_min = x.index(x_min)  # x轴最左边
        i_max = x.index(x_max)  # x轴最右边
        ltext_min_gap = rtext_min_gap = ltext_top = ltext_bottom = rtext_top = rtext_bottom = 0  # 左右文本的最小间隙和ylim, 单位与坐标轴相同
        ax_annotate_left, ax_annotate_right = None, None  # 左右标记对应的坐标轴
        if annotate_left:  # 如果左侧有标记
            if yl_annotate_left:
                y, ylabel, yc, ylim = y_left, ylabel_left, colors_left, ylim_left
                ax_annotate_left = ax_left
            else:
                y, ylabel, yc, ylim = y_right, ylabel_right, colors_right, ylim_right
                ax_annotate_left = ax_right
            # 计算y轴约束
            yy = sum(y, [])
            ltext_bottom = min(yy + ([ylim[0]] if ylim else []))
            ltext_top = max(yy + ([ylim[1]] if ylim else []))
            if ylim:
                ltext_min_gap = ytext_min_gap / (width / (ylim[1] - ylim[0]))
            else:
                ltext_min_gap = ytext_min_gap / (width / (ltext_top - ltext_bottom))
            # 开始赋值
            for v, name, c in zip(y, ylabel, yc):
                v = v[i_min]
                name_y_left.append([name, v, v, c])
        if annotate_right:  # 如果右侧有标记
            if yl_annotate_right:
                ax_annotate_right = ax_left
                y, ylabel, yc, ylim = y_left, ylabel_left, colors_left, ylim_left
            else:
                ax_annotate_right = ax_right
                y, ylabel, yc, ylim = y_right, ylabel_right, colors_right, ylim_right
            # 计算y轴约束
            yy = sum(y, [])
            rtext_bottom = min(yy + ([ylim[0]] if ylim else []))
            rtext_top = max(yy + ([ylim[1]] if ylim else []))
            if ylim:
                rtext_min_gap = ytext_min_gap / (width / (ylim[1] - ylim[0]))
            else:
                rtext_min_gap = ytext_min_gap / (width / (rtext_top - rtext_bottom))
            # 开始赋值
            for v, name, c in zip(y, ylabel, yc):
                v = v[i_max]
                name_y_right.append([name, v, v, c])
        # 计算y轴标记文本位置
        all = []
        if name_y_left:
            all.append([name_y_left, ltext_top, ltext_bottom, ltext_min_gap])
        if name_y_right:
            all.append([name_y_right, rtext_top, rtext_bottom, rtext_min_gap])
        for name_y_, text_top, text_bottom, text_min_gap in all:
            # 正序排序, (目标点y轴坐标,标记名称)
            name_y_ = sorted(name_y_, key=lambda t: (t[1], t[0]))
            # 均匀分割
            gap = (text_top - text_bottom) / (len(name_y_) + 1)
            p_L = [text_bottom + i * gap for i in range(1, len(name_y_) + 1)]
            for i, p in enumerate(p_L):
                name_y_[i][2] = p
            # 从下到上移动规范文本位置, 从上到下移动规范文本位置, 该算法可能有 直角三角形/梯形形式 聚集
            for range_ in [range(len(name_y_)), range(len(name_y_) - 1, -1, -1)]:
                for i in range_:
                    y = name_y_[i]
                    bottom = text_bottom + text_min_gap  # 不能比边界低
                    if i > 0:
                        bottom = max(bottom, name_y_[i - 1][2] + text_min_gap)  # 不能比下一个点低
                    top = text_top - text_min_gap  # 不能比边界高
                    if i < len(name_y_) - 1:
                        top = min(top, name_y_[i + 1][2] - text_min_gap)  # 不能比上一个点高
                    # 因为均匀分割, 故不可能发生. 受精度影响, 比如超15位后 1.9516675497853828<1.9516675497853830
                    assert top / (abs(int(top)) + 1) >= bottom / (abs(int(top)) + 1) - 10 ** -14, \
                        'top < bottom ! %.19f<%.19f, %s' % (top, bottom, str(range_))
                    yp = y[1]  # 目标点y轴坐标
                    if bottom <= yp <= top:
                        y[2] = yp
                    elif bottom > yp:
                        y[2] = bottom
                    else:
                        y[2] = top
        # 计算标记宽度
        ml, mr = xl_text_margin, xr_text_margin  # 左右标记文本离y轴的距离, 单位基本与 length 相同
        text_len_max = -1  # 总体最大字体宽度
        if annotate_left:
            xl_text_len = max([get_text_w(i[0]) for i in name_y_left]) / custom_dpi  # 文本最大长度, 单位基本与 length 相同
            tl, al = xl_text_len, xl_arrow_len
            text_len_max = max(text_len_max, xl_text_len)
        else:  # 如果左边没有标记
            tl, al = 0, 0
        if annotate_right:
            xr_text_len = max([get_text_w(i[0]) for i in name_y_right]) / custom_dpi  # 文本最大长度, 单位基本与 length 相同
            tr, ar = xr_text_len, xr_arrow_len
            text_len_max = max(text_len_max, xr_text_len)
        else:  # 如果右边没有标记
            tr, ar = 0, 0
        if text_len_max > 0 and legend_right and ylabel_display:  # 空出图例
            label_len = 0.6  # 标签的长度, 单位基本与 length 相同
            mr += text_len_max + label_len
        # 计算x轴标记位置 和 x轴范围
        if annotate_left or annotate_right:
            ''' 根据 4元1次9参数方程组 解析解 计算
            from sympy import *
            leng, ll, lr, xl, xr, ml, tl, al, mr, tr, ar, yl, yr = symbols(
                'length xlim_left xlim_right x_min x_max ml tl al mr tr ar xtext_left xtext_right'
            )
            for i, j in solve([
                (ml + tl + al) * (lr - ll) / leng - (xl - ll),
                (mr + tr + ar) * (lr - ll) / leng - (lr - xr),
            ], [ll, lr]).items():
                print(i, '=', j)
            for i, j in solve([
                xl - (tl + al) * (lr - ll) / leng - yl,
                xr + ar * (lr - ll) / leng - yr,
            ], [yl, yr]).items():
                print(i, '=', j)
            '''
            xlim_left = (al * x_max + ar * x_min - length * x_min + ml * x_max + mr * x_min + tl * x_max + tr * x_min) \
                        / (al + ar - length + ml + mr + tl + tr)
            xlim_right = (al * x_max + ar * x_min - length * x_max + ml * x_max + mr * x_min + tl * x_max + tr * x_min) \
                         / (al + ar - length + ml + mr + tl + tr)
            xtext_right = (-ar * xlim_left + ar * xlim_right + length * x_max) / length
            xtext_left = (al * xlim_left - al * xlim_right + length * x_min + tl * xlim_left - tl * xlim_right) / length
            xlim = [xlim_left, xlim_right]  # x轴约束
        else:
            xtext_right = xtext_left = None  # 左侧标记 和 右侧标记 的x轴坐标
        # 绘制标记
        all = []
        if name_y_left:
            all.append([name_y_left, ax_annotate_left, x_min, xtext_left, y_left_ls])
        if name_y_right:
            all.append([name_y_right, ax_annotate_right, x_max, xtext_right, y_right_ls])
        for name_y_, ax_annotate_, x_m, xtext_, y__ls in all:
            for name, ya, yt, c in name_y_:
                if not annotate_color:
                    c = 'black'
                ax_annotate_.annotate(s=name, c=c, xy=(x_m, ya), xytext=(xtext_, yt),
                                      arrowprops={'arrowstyle': '->', 'linestyle': y__ls})
        # 配置
        if xaxis:  # x轴名称
            ax_left.set_xlabel(xaxis)
        if xlim:  # x轴约束
            assert len(xlim) == 2, 'xlim 数量错误! %s' % str(xlim)
            if xlim[0] is None or xlim[0] > x_min:
                xlim[0] = x_min
            if xlim[1] is None or xlim[1] < x_max:
                xlim[1] = x_max
            assert xlim[0] < xlim[1], 'xlim 大小错误! %s' % str(xlim)
            ax_left.set_xlim(*xlim)
        if title:  # 标题
            plt.title(title)
        if all_polt and ylabel_display:  # 图例
            labs = [l.get_label() for l in all_polt]
            ax_left.legend(all_polt, labs, loc='best', labelspacing=0.)
        # 刻度
        if xticks:
            plt.setp(ax_left, xticks=x, xticklabels=xticks)
        else:
            ax_left.set_xticks(x)  # 每个刻度都显示
        if x_rotation:
            plt.setp(ax_left.get_xticklabels(), rotation=x_rotation, horizontalalignment='right')
        # 网格
        if grid_axis_yl:
            ax_left.grid(linestyle=y_left_ls, alpha=grid_alpha, axis='y')
        if grid_axis_yr and ax_right is not None:
            ax_right.grid(linestyle=y_right_ls, alpha=grid_alpha, axis='y')
        if grid_ls_x:
            ax_left.grid(linestyle=grid_ls_x, alpha=grid_alpha, axis='x')

    def add_heatmap(self, mat, xticks, yticks, mat_text=None, text_c='black', text_fs=None, colorbar_pad=0.05,
                    cmap='coolwarm', sub_title='', sub_title_fs=None, xlabel=None, ylabel=None, x_rotation=None,
                    n=1):
        """
        增加一个热力图绘制
        :param mat: [[热力图中的第一行第一个数值,..],..]
        :param xticks: ['第一列第一个标记',..]; x轴标记
        :param yticks: ['第一行第一个标记',..]; y轴标记
        :param mat_text: None or int or [['热力图中的第一行第一个方格标记',..],..]; None表示图中每个方格无标记
            int表示将mat中每个数值放在方格标记时保留的小数点位数, 二维列表表示用str替换mat中的数值
        :param text_c: str; 方格字体颜色
        :param text_fs: None or float; 方格字体大小
        :param colorbar_pad: float; 颜色条左侧的距离比例
        :param cmap: str; 渐变色种类, 比如 rainbow/coolwarm
        :param sub_title: str; 这个子图的标题
        :param sub_title_fs: None or int; 这个子图的标题的字体大小, None默认
        :param xlabel: str or None; x轴名, None表示无
        :param ylabel: str or None; y轴名, None表示无
        :param x_rotation: None or float; x轴标签名称逆时针旋转度数, None表示不旋转
        :param n: int; 第几个图, 从1开始, 先行后列
        :return:
        """
        ax = self.fig.add_subplot(self.r, self.c, n)
        heatmap = ax.imshow(mat, cmap=plt.get_cmap(cmap), aspect='auto')
        # 绘制坐标轴标记
        plt.setp(ax, xticks=np.arange(len(xticks)), xticklabels=xticks)
        plt.setp(ax, yticks=np.arange(len(yticks)), yticklabels=yticks)
        if x_rotation:
            plt.setp(ax.get_xticklabels(), rotation=x_rotation, horizontalalignment='right')
        # 绘制⽂本
        if mat_text is not None:
            for i in range(len(xticks)):
                for j in range(len(yticks)):
                    if isinstance(mat_text, int):
                        ax.text(i, j, round(mat[j][i], mat_text), ha="center", va="center", color=text_c,
                                fontsize=text_fs)
                    else:
                        ax.text(i, j, mat_text[j][i], ha="center", va="center", color=text_c, fontsize=text_fs)
        # 绘制颜色条
        self.fig.colorbar(heatmap, shrink=0.99, aspect=30, use_gridspec=True, pad=colorbar_pad)
        # 设置标题
        ax.set_title(sub_title, fontsize=sub_title_fs)
        # 设置坐标轴标签
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

    def draw(self, save_path=None):
        '''
        :param save_path: str or None; 图片保存路径
        :return:
        '''
        if save_path:
            fname, fextension = os.path.splitext(save_path)
            plt.tight_layout()
            plt.savefig(save_path, format=fextension[1:])
        plt.show()  # 绘制
        plt.close()

    @staticmethod
    def ncolors(n=1, rand=False):
        '''
        生成区分度比较大的几个颜色
        :param n: 生成几个颜色
        :param rand: 是否随机
        :return:
        '''
        if n < 1:
            return []
        if n == 1:
            return ['#1E78B3']
        rgb_colors = []
        # get_n_hls_colors
        hls_colors = []
        i = 0
        step = 360.0 / n
        while i < 360:
            h = i
            if rand:
                s = 90 + random.random() * 10
                l = 50 + random.random() * 10
            else:
                s = 95
                l = 55
            _hlsc = [h / 360.0, l / 100.0, s / 100.0]
            hls_colors.append(_hlsc)
            i += step
        # hlsc to rgb
        for hlsc in hls_colors:
            _r, _g, _b = colorsys.hls_to_rgb(hlsc[0], hlsc[1], hlsc[2])
            rgb = [int(x * 255.0) for x in (_r, _g, _b)]
            rgb = [('0' + hex(i)[2:])[-2:] for i in rgb]
            rgb_colors.append('#' + ''.join(rgb))
        return rgb_colors

    @staticmethod
    def get_text_width(text, fig_obj=None, text_obj=None):
        '''
        获取一个字符串的绘制宽度
        :param text: str, 要计算宽度的字符
        :param fig_obj: matplotlib.figure.Figure, 没有可能导致宽度获取不准确
        :param text_obj: matplotlib.text.Text, 用于输入字体信息, 没有的话每次默认可能实例化效率低
        :return: float, 像素
        '''
        if text_obj is None:
            from matplotlib.text import Text
            text_obj = Text()
        clean_line, ismath = text_obj._preprocess_math(text)
        if fig_obj is None:
            from matplotlib.backend_bases import RendererBase
            renderer = RendererBase()
        else:
            renderer = fig_obj.canvas.get_renderer()
        w = renderer.get_text_width_height_descent(s=clean_line, prop=text_obj.get_fontproperties(), ismath=ismath)[0]
        # 还有一种获取长度的方法需要绘制出来并隐藏
        # lambda t: fig.text(0.15, 0.5, t, alpha=0).get_window_extent(fig.canvas.get_renderer()).bounds[2]
        return w

    @staticmethod
    def radar_factory(num_vars, frame='polygon'):
        """Create a radar chart with `num_vars` axes.

        This function creates a RadarAxes projection and registers it.
        from: https://stackoverflow.com/questions/52910187/how-to-make-a-polygon-radar-spider-chart-in-python
        https://stackoverflow.com/questions/65514398/how-to-make-radar-spider-chart-with-pentagon-grid-using-matplotlib-and-python

        Parameters
        ----------
        num_vars : int
            Number of variables for radar chart.
        frame : {'circle' | 'polygon'}
            Shape of frame surrounding axes.
        """
        # calculate evenly-spaced axis angles
        theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

        class RadarAxes(PolarAxes):
            name = 'radar'

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # rotate plot such that the first axis is at the top
                self.set_theta_zero_location('N')

            def fill(self, *args, closed=True, **kwargs):
                """Override fill so that line is closed by default"""
                return super().fill(closed=closed, *args, **kwargs)

            def plot(self, *args, **kwargs):
                """Override plot so that line is closed by default"""
                lines = super().plot(*args, **kwargs)
                for line in lines:
                    self._close_line(line)

            def _close_line(self, line):
                x, y = line.get_data()
                # FIXME: markers at x[0], y[0] get doubled-up
                if x[0] != x[-1]:
                    x = np.concatenate((x, [x[0]]))
                    y = np.concatenate((y, [y[0]]))
                    line.set_data(x, y)

            def set_varlabels(self, labels):
                self.set_thetagrids(np.degrees(theta), labels)

            def _gen_axes_patch(self):
                # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
                # in axes coordinates.
                if frame == 'circle':
                    return Circle((0.5, 0.5), 0.5)
                elif frame == 'polygon':
                    return RegularPolygon((0.5, 0.5), num_vars, radius=.5, edgecolor="k")
                else:
                    raise ValueError("unknown value for 'frame': %s" % frame)

            def draw(self, renderer):
                """ Draw. If frame is polygon, make gridlines polygon-shaped """
                if frame == 'polygon':
                    gridlines = self.yaxis.get_gridlines()
                    for gl in gridlines:
                        gl.get_path()._interpolation_steps = num_vars
                super().draw(renderer)

            def _gen_axes_spines(self):
                if frame == 'circle':
                    return super()._gen_axes_spines()
                elif frame == 'polygon':
                    # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                    spine = Spine(axes=self, spine_type='circle', path=Path.unit_regular_polygon(num_vars))
                    # unit_regular_polygon gives a polygon of radius 1 centered at
                    # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                    # 0.5) in axes coordinates.
                    spine.set_transform(Affine2D().scale(.5).translate(.5, .5) + self.transAxes)
                    return {'polar': spine}
                else:
                    raise ValueError("unknown value for 'frame': %s" % frame)

        register_projection(RadarAxes)
        return theta


if __name__ == '__main__':
    draw = Draw(length=15, width=10, r=2, c=3)
    # 字体宽度测试
    print('计算字体宽度...')
    t = ['A', 'a', '1', '-', '#', '.', '%', '(', '$A$']
    w = [draw.get_text_width(i) for i in t]
    print({i: j for i, j in zip(t, w)})
    # 雷达图
    labels = np.array(['abc', 'bbb', 'ddd', 'eee', 'ccc', 'fff'])
    data = np.random.rand(4, 6).tolist()
    draw.add_radar(labels, [f'{i}{i}' for i in range(4)], data, 'radar', n=1, radii=(0, 0.2, 0.4, 0.6, 0.8, 1),
                   fill_alpha=0.1, title_pad=20)
    # 三维透视图
    x_num = 8
    y_num = 6
    xyz_L = (np.hstack([np.dstack(np.where(np.ones([x_num, y_num])))[0], np.ones([x_num * y_num, 1])]) / 2).tolist()
    xyz_L[14][1] += 0.5
    xyz_L[14][2] = 1
    xyz_L[7][2] = 1.5
    xyz_L[19][2] = 0
    draw.add_3d(xyz_L, n=2, sub_title='3d', xyz_scatter=(np.random.rand(4, 11, 3) * 2).tolist(),
                scatter_labels=['11', '22', '33', '44'], scatter_marker=None)
    # 小提琴图
    all_data1 = np.random.normal(-1, 1, size=[7, 6]).tolist()
    xaxis_name = [f'x{i}' for i in range(7)]
    draw.add_violin(all_data1, xaxis_name, n=3, title='violin', x_rotation=45)
    # 双轴标记折线图
    x = [i * 20 for i in range(5)][::-1]
    y = lambda n, m: [[random.uniform(400, m) for i in x] for j in range(n)]
    y_left = y(4, m=2)
    y_right = y(1, m=40)
    draw.add_line(
        x=x, xaxis='x', xlim=None, title='line', y_left=y_left, yaxis_left='$y_1$', ylim_left=[100, None],
        ylabel_left=['$yl_{%d}$' % i for i in range(len(y_left))],
        y_right=y_right,
        yaxis_right='$y_2$', ylim_right=[100, None],
        ylabel_right=['$yr_{%d}$' % i for i in range(len(y_right))],
        length=12, width=6, lw=1, ytext_min_gap=0.25,
        ylabel_display=True,
        y_left_ls='-', y_right_ls='--', grid_ls_x=':', grid_axis_yl=True, grid_axis_yr=True, grid_alpha=0.2,
        annotate=True,
        annotate_in_left=True, annotate_color=True, legend_right=True,
        xl_text_margin=0.1, xl_arrow_len=0.9, xr_text_margin=0.05, xr_arrow_len=0.5, custom_dpi=90,
        n=4, x_rotation=90, xticks=[f'x{i}' for i in x]
    )
    # 热力图
    vegetables = ["cucumber", "tomato", "lettuce", "asparagus", "potato", "wheat", "barley"]
    farmers = list('ABCDEFGH')
    harvest = np.random.rand(7, 8)
    draw.add_heatmap(harvest, farmers, vegetables, mat_text=2, sub_title='heatmap', x_rotation=90, n=5)
    draw.draw('test_draw_utils.pdf')
