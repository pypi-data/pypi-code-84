# -*- coding: utf-8 -*-

"""
Module latticeadaptor.utils 
=================================================================

A module containg some helper functions.

"""

import os
from typing import List

import pandas as pd


def is_number(s):
    """Method to check if a value is a number or not.

    :param str s: string to test
    :returns: True or False
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def filter_family(df, fam):
    """Filter dataframe by family name.

    :param pd.DataFrame df: original dataframe to filter
    :param str fam: family string to filter on
    :returns: filtered pd.DataFrame
    """
    _filter = df.family == fam
    return df.loc[_filter].copy().reset_index(drop=True)


def rotate(l, n):
    """
    Method to rotate a list.

                                                                    :param list l: list to rotate
                                                                    :param int  n: number of elements to rotate over
                                                                    :returns: rotated list
    """
    return l[-n:] + l[:-n]


def delete_first_line(file):
    """
    Method to delete first line in a file.
    Used to delete first line of SAVE SEQUENCE output of madx.

                                                                    :param str file: file of which to delete first line
    """
    with open(file, "r") as fin:
        data = fin.read().splitlines(True)
    with open(file, "w") as fout:
        fout.writelines(data[1:])


def highlight_cells(data, _list=[], color="yellow"):
    """Highlight cells in a dataframe with a given color.

    :param pd.DataFrame data: dataframe to highlight
    :param list _list: list of values to highlight
    :param str color: color to use for highlighting [yellow]
    :returns: a styled pd.DataFrame
    """
    attr = "background-color: {}".format(color)
    if data.ndim == 1:
        is_sel = data.isin(_list)
        return [attr if v else "" for v in is_sel]
    else:
        is_sel = data.isin(_list)
        return pd.DataFrame(np.where(is_sel, attr, ""), index=data.index, columns=data.columns)


def highlight_row(data, _list, column, color="yellow"):
    """Highlight rows in a dataframe with a given color.

    :param pd.DataFrame data: dataframe to highlight
    :param list _list: list of values to highlight
    :param list column: column to look for the values
    :param str color: color to use for highlighting [yellow]
    :returns: a styled pd.DataFrame
    """
    attr = "background-color: {}".format(color)
    is_sel = pd.Series(data=False, index=data.index)
    is_sel[column] = data.loc[column].isin(_list)
    return [attr if is_sel.any() else "" for v in is_sel]


def display_more(df, maxrows=300, maxcols=100):
    """
    Show more rows and columns of a dataframe.
    """
    with pd.option_context("display.max_rows", maxrows, "display.max_columns", maxcols):
        display(df)


# ==============================================================================
# Lattice tools
# ==============================================================================
def dipole_split_angles_to_dict(
    dipole_name, dipole_len, dipole_bend_angle_rad, angle_list, verbose=True
):
    """
    Method to generate a dictionary that is used by the split_dipoles method
    to split the dipoles over the angle list given in angle_list.
    Verbose allows to print the output for debugging.

    IMPORTANT NOTE:
    ---------------
    Auto adds half angle split and final angle for full magnet.

    :param str dipole_name: name of the dipole - same as name in dataframe used in split_dipoles as input - becomes key
    :param float dipole_len: length of the dipole
    :param float dipole_bend_angle_rad: bending angle of the dipole in rad
    :param List[float] angle_list: list of splitting angles - from start of dipole -in deg
    :param bool verbose: flag to print processing output
    :returns: Dict containing split angles in rad and split lengths. Main key is dipole name, sub keys are "length" and "angles".
    """
    _dict = {dipole_name: dict()}

    dipole_bend_angle_deg = np.rad2deg(dipole_bend_angle_rad)
    dipole_bend_radius = dipole_len / dipole_bend_angle_rad

    if verbose:
        print("Dipole length [m]       : {:12.6f}".format(dipole_len))
        print("Dipole Bend Angle [rad] : {:12.6f}".format(dipole_bend_angle_rad))
        print("Dipole Bend Angle [deg] : {:12.6f}".format(dipole_bend_angle_deg))
        print("Dipole Bend Radius [m]  : {:12.6f}".format(dipole_bend_radius))
        print()
        print()

    split_angles_BM_deg = np.array(
        sorted(angle_list + [dipole_bend_angle_deg / 2, dipole_bend_angle_deg])
    )
    split_angles_BM_cum_rad = np.deg2rad(split_angles_BM_deg)
    split_angles_BM_rad = np.r_[split_angles_BM_cum_rad[0], np.diff(split_angles_BM_cum_rad)]
    split_lengths_cum_BM = split_angles_BM_cum_rad * dipole_bend_radius
    split_lengths_BM = np.r_[split_lengths_cum_BM[0], np.diff(split_lengths_cum_BM)]

    if verbose:
        print(
            "BM splitting angles               [deg] : {}".format(
                "".join(["{:12.6f}".format(a) for a in split_angles_BM_deg])
            )
        )
        print(
            "BM splitting angles  - cumulative [rad] : {}".format(
                "".join(["{:12.6f}".format(a) for a in split_angles_BM_cum_rad])
            )
        )
        print(
            "BM splitting angles  - individual [rad] : {}".format(
                "".join(["{:12.6f}".format(a) for a in split_angles_BM_rad])
            )
        )
        print(
            "BM splitting lengths - cumulative [m]   : {}".format(
                "".join(["{:12.6f}".format(a) for a in split_lengths_cum_BM])
            )
        )
        print(
            "BM splitting lengths - individual [m]   : {}".format(
                "".join(["{:12.6f}".format(a) for a in split_lengths_BM])
            )
        )
        print()

    _dict[dipole_name] = {"lengths": split_lengths_BM, "angles": split_angles_BM_rad}

    return _dict


def split_dipoles(df, _dict, halfbendangle):
    """
    Method to split the dipole given in the
    dataframe according the data given in _dict.

                                    :params pd.DataFrme df: seq table reduced to dipoles to split
                                    :params dict _dict: output of dipole_split_angles_to_dict joined as dict for all dipoles in df
                                    :params float halfbendangle: half bending angle for the dipoles
                                    :returns: updated table with dipolse split
    """
    # init output
    newdf = pd.DataFrame()

    # loop over the dipoles
    for j, row in df.iterrows():
        lengths = _dict[row["name"]]["lengths"]
        angles = _dict[row["name"]]["angles"]

        # calculate the center positions of the splits
        end_pos = lengths.cumsum() + row.pos - row.L / 2
        center_pos = end_pos - (lengths / 2)

        # count splits per magnet
        aports = 1
        bports = 1
        cum_angle = 0

        # loop over the splitting angles for this specific dipole
        for i, (angle, l, pos) in enumerate(zip(angles, lengths, center_pos)):
            # for each angle create a new seq table entry
            newrow = row.copy()
            cum_angle += angle

            # naming depends on magnet number in the sector
            if "BM1" in row["name"]:
                M = 1
            else:
                M = 2

            # add marker
            markerrow = row.copy()
            markerrow.family = "MARKER"
            markerrow.L = 0.000000
            markerrow = markerrow.drop(labels=["E1", "E2", "K1", "K2", "ANGLE"])

            # naming
            # beam ports A in first half of the magnet
            # beam ports B in second half of the magnet
            # number each per split number
            if cum_angle - halfbendangle < -1e-6:
                name = row["name"] + "1_{}_deg".format(
                    ("{:2.2f}".format(np.rad2deg(cum_angle))).replace(".", "p").strip()
                )
                markerrow["name"] = "MBEAMPORT_{}A{}".format(M, aports)
                aports += 1
            elif abs(cum_angle - halfbendangle) < 1e-6:
                name = row["name"] + "1_{}_deg".format(
                    ("{:2.2f}".format(np.rad2deg(cum_angle))).replace(".", "p").strip()
                )
                markerrow["name"] = (
                    "M"
                    + row["name"]
                    + "_MIDDLE".format(
                        ("{:2.2f}".format(np.rad2deg(cum_angle))).replace(".", "p").strip()
                    )
                )
            else:
                name = row["name"] + "2_{}_deg".format(
                    ("{:2.2f}".format(np.rad2deg(cum_angle))).replace(".", "p").strip()
                )
                markerrow["name"] = "MBEAMPORT_{}B{}".format(M, bports)
                bports += 1

            newrow["name"] = name

            # updating angles
            newrow.ANGLE = angle

            # updating lengths
            newrow.L = l

            # updating center position
            newrow.pos = pos
            markerrow.pos = pos + l / 2

            # if at is already in columns update it
            if "at" in newrow.index:
                newrow["at"] = pos

            # update E1 E2
            if i != 0:
                newrow.E1 = 0.000000

                if i != len(angles) - 1:
                    newrow.E2 = 0.000000
            else:
                newrow.E2 = 0.000000

            # add marker only if not at end of magnet
            if abs(cum_angle - 2 * halfbendangle) > 1e-6:
                newdf = newdf.append(markerrow)

            newdf = newdf.append(newrow)

    return newdf.reset_index(drop=True)


def compare_settings_dicts(dc1, dc2, threshold=1):
    """
    Method to compare lattice settings dicts
    extracted from json lattice files or tables.

                                                                    :param dict dc1: dict of lattice 1
                                                                    :param dict dc2: dict of lattice 2
                                                                    :param float threshold: threshold to show traffic light colors
    """
    combinedc = defaultdict(list)
    for k, v in chain(dc1.items(), dc2.items()):
        combinedc[k].append(v)

    for k, v in combinedc.items():
        if len(v) > 1:
            if v[0] != v[1]:
                if abs(v[1] - v[0]) > threshold:
                    print(colored("WARNING STRONG CHANGE", "red"))
                print(
                    colored(
                        "{:10} {:16.12f} {:16.12f} {:16.12f}".format(k, v[0], v[1], v[1] - v[0]),
                        "yellow",
                    )
                )
            else:
                print(
                    colored(
                        "{:10} {:16.12f} {:16.12f}".format(k, v[0], v[1], v[1] - v[0]), "green"
                    )
                )


def print_twiss_summ(tw):
    """Method to pretty print madx twiss summary generated by cpymadx

    :param object tw: twiss object produced by cpymadx
    """
    from pprint import pprint

    try:
        dc = [
            "{:15}:{:15.6e}".format(k, v)
            if isinstance(v, float)
            else "{:15}:{:>15}".format(k, v.strip())
            for k, v in dict(tw.summary).items()
        ]
    except:
        dc = [
            "{:15}:{:15.6e}".format(k, v)
            if isinstance(v, float)
            else "{:15}:{:>15}".format(k, v.strip())
            for k, v in dict(tw).items()
        ]
    pprint(dc)


# ==============================================================================
# MADX tools
# ==============================================================================
def install_start_end_marker(name: str, length: float) -> str:
    """
    Method to add end marker.

                                    :param str name: lattice name
                                    :param float length: lattice length
                                    :returns: Madx install str for start and end marker
    """
    # define  start and end marker
    text = "{:12}: {:12};\n".format("MSTART", "MARKER")
    text += "{:12}: {:12};\n\n".format("MEND", "MARKER")

    # start sequence edit
    text += "USE, SEQUENCE={};\n".format(name)
    text += "SEQEDIT, SEQUENCE = {};  \nFLATTEN;\n".format(name)

    # install start and end marker
    line = "INSTALL, ELEMENT = {:16}, AT = {:12.6f};\n".format("MSTART", 0.00000)
    text += line
    line = "INSTALL, ELEMENT = {:16}, AT = {:12.6f};\n".format("MEND", length)
    text += line

    # end sequence edit
    text += "FLATTEN;\nENDEDIT;"

    return text


# ==============================================================================
# Plot tools
# ==============================================================================
from collections import defaultdict
from itertools import chain

import matplotlib
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from cycler import cycler
from matplotlib import pyplot as plot
from matplotlib.collections import PatchCollection
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from termcolor import colored

from ..parsers import parse_from_madx_sequence_string


def draw_brace(ax, xspan, text, yshift=0.0):
    """Draws an annotated brace on the x axes."""
    xmin, xmax = xspan
    xspan = xmax - xmin
    ax_xmin, ax_xmax = ax.get_xlim()
    xax_span = ax_xmax - ax_xmin
    ymin, ymax = ax.get_ylim()
    yspan = ymax - ymin
    resolution = int(xspan / xax_span * 100) * 2 + 1  # guaranteed uneven
    beta = 300.0 / xax_span  # the higher this is, the smaller the radius

    x = np.linspace(xmin, xmax, resolution)
    x_half = x[: resolution // 2 + 1]
    y_half_brace = 1 / (1.0 + np.exp(-beta * (x_half - x_half[0]))) + 1 / (
        1.0 + np.exp(-beta * (x_half - x_half[-1]))
    )
    y = np.concatenate((y_half_brace, y_half_brace[-2::-1]))
    y = ymin + +yshift + (0.05 * y - 0.01) * yspan  # adjust vertical position

    ax.autoscale(False)
    ax.plot(x, y, color="black", lw=1)

    ax.text((xmax + xmin) / 2.0, ymin + 0.07 * yspan, text, ha="center", va="bottom")


def Beamlinegraph_compare_from_seq_files(seqfile1, seqfile2, start=0.0, stop=None):
    """
    Method to compare location of beam line elements,
    where the positions are extracted from a MADX
    sequence file.

    Arguments:
    ----------
    seqfile1    : str
                                    input seqfile 1
    seqfile2    : str
                                    input seqfile 2
    start       :
                                    s location of start
    stop        :
                                    s location of stop

    """
    _REQUIRED_COLUMNS = ["pos", "name", "L"]
    _RECTANGLE_ELEMENTS = [
        "SBEND",
        "RBEND",
        "KICKER",
        "VKICKER",
        "HKICKER",
        "QUADRUPOLE",
        "SEXTUPOLE",
        "RFCAVITY",
        "DRIFT",
    ]
    _COLMAP = {
        "SBEND": "#0099FF",
        "RBEND": "#0099FF",
        "KICKER": "#0099FF",
        "VKICKER": "#0099FF",
        "HKICKER": "#0099FF",
        "QUADRUPOLE": "green",
        "SEXTUPOLE": "#FF99FF",
        "RFCAVITY": "#08bad1",
        "MARKER": "red",
        "MONITOR": "black",
        "DIPEDGE": "blue",
        "DRIFT": "#D0D0D0",
    }

    with open(seqfile1, "r") as f:
        seqfilestr1 = f.read()

    with open(seqfile2, "r") as f:
        seqfilestr2 = f.read()

    name1, len1, table1 = parse_from_madx_sequence_string(seqfilestr1)
    name2, len2, table2 = parse_from_madx_sequence_string(seqfilestr2)

    # check if columns are ok
    for c in _REQUIRED_COLUMNS:
        assert c in table1.columns
        assert c in table2.columns

    # find range to plot
    if stop is None:
        stop = max(len1, len2)
        # idxmax_pos = table1["pos"].idxmax()
        # stop = table1.loc[idxmax_pos, "pos"] + table1.loc[idxmax_pos, "L"]
    else:
        table1 = table1.loc[table1["pos"].between(start, stop)]
        table2 = table2.loc[table2["pos"].between(start, stop)]

    _ = plt.figure(figsize=(16, 6))
    axis = plt.gca()

    offset_array = np.array([0.0, -0.5])

    for _, row in table1.iterrows():
        col = _COLMAP[row.family.upper()]

        if row.family in _RECTANGLE_ELEMENTS:
            axis.add_patch(
                mpatches.Rectangle(
                    np.array([row.pos - row.L / 2, 0.0]) + offset_array,
                    row.L,
                    0.33,
                    color=col,
                    alpha=1.0,
                )
            )
            axis.vlines(
                row.pos - row.L / 2,
                offset_array[1],
                0,
                linestyle="dashed",
                color="gray",
                linewidth=1,
            )
            axis.vlines(
                row.pos + row.L / 2,
                offset_array[1],
                0,
                linestyle="dashed",
                color="gray",
                linewidth=1,
            )

        else:
            Path = mpath.Path
            h = 1.0
            offs_mon = np.array([0.0, 0.03])

            verts = np.array(
                [
                    (0, h),
                    (0, -h),
                ]
            )

            codes = [Path.MOVETO, Path.LINETO]

            verts += offs_mon

            path = mpath.Path(verts + offset_array + np.array([row.pos, 0.0]), codes)
            patch = mpatches.PathPatch(path, color=col, lw=1, alpha=1.0 * 0.5)
            axis.add_patch(patch)

        axis.annotate(
            row.family + ": " + row["name"],
            xy=(row.pos, 0),
            # xycoords='data',
            xytext=(row.pos, 0) + offset_array,
            # textcoords='data',
            horizontalalignment="left",
            # arrowprops=dict(arrowstyle="simple",),# connectionstyle="arc3,rad=+0.2"),
            # bbox=dict(boxstyle="round", facecolor="w", edgecolor="0.5", alpha=0.9),
            fontsize=8,
            rotation=90,
        )

    offset_array = np.array([0.0, 0.5])

    for _, row in table2.iterrows():
        col = _COLMAP[row.family.upper()]

        if row.family in _RECTANGLE_ELEMENTS:
            axis.add_patch(
                mpatches.Rectangle(
                    np.array([row.pos - row.L / 2, 0.0]) + offset_array,
                    row.L,
                    0.33,
                    color=col,
                    alpha=1.0,
                )
            )
            axis.vlines(
                row.pos - row.L / 2,
                offset_array[1],
                0,
                linestyle="dashed",
                color="red",
                linewidth=1,
            )
            axis.vlines(
                row.pos + row.L / 2,
                offset_array[1],
                0,
                linestyle="dashed",
                color="red",
                linewidth=1,
            )
        else:
            Path = mpath.Path
            h = 1.0
            offs_mon = np.array([0.0, 0.03])

            verts = np.array(
                [
                    (0, h),
                    (0, -h),
                ]
            )

            codes = [Path.MOVETO, Path.LINETO]

            verts += offs_mon

            path = mpath.Path(verts + offset_array + np.array([row.pos, 0.0]), codes)
            patch = mpatches.PathPatch(path, color=col, lw=1, alpha=1.0 * 0.5)
            axis.add_patch(patch)

        axis.annotate(
            row.family + ": " + row["name"],
            xy=(row.pos, 0),
            # xycoords='data',
            xytext=(row.pos, 0) + offset_array,
            # textcoords='data',
            horizontalalignment="left",
            # arrowprops=dict(arrowstyle="simple",),# connectionstyle="arc3,rad=+0.2"),
            # bbox=dict(boxstyle="round", facecolor="w", edgecolor="0.5", alpha=0.9),
            fontsize=8,
            rotation=90,
        )

    plt.xlim(start, stop)
    plt.ylim(-1.1, 1.1)
    plt.xlabel("S[m]")
    #     plt.grid()
    return plt, axis


def Beamlinegraph_from_seq_file(
    seqfile, start=0.0, stop=None, offset_array=[0.0, 0.0], anno=True, size=(12, 6)
):
    _REQUIRED_COLUMNS = ["pos", "name", "L"]
    _RECTANGLE_ELEMENTS = ["SBEND", "RBEND", "KICKER", "VKICKER", "HKICKER", "DRIFT"]
    _MIN_HEIGTH = 0.1
    _MAX_HEIGTH = 10.0

    with open(seqfile, "r") as f:
        seqfilestr = f.read()

    name, length, table = parse_from_madx_sequence_string(seqfilestr)

    # check if columns are ok
    for c in _REQUIRED_COLUMNS:
        assert c in table.columns

    # find range to plot
    if stop is None:
        # idxmax_pos = table["pos"].idxmax()
        # stop = table.loc[idxmax_pos, "pos"] + table.loc[idxmax_pos, "L"]
        stop = length
    else:
        table = table.loc[table["pos"].between(start, stop)]

    #    print(start, stop)

    element_families = table.family.unique()

    # determine max plot heights
    if any(i in element_families for i in _RECTANGLE_ELEMENTS):
        angle_max = 1.0
        if ("ANGLE" in table.columns) and not all(table.ANGLE.isna()):
            angle_max = abs(table.ANGLE.max())
        else:
            table["ANGLE"] = 0.0

    if "QUADRUPOLE" in element_families:
        k_max = abs(table.K1.max())

    _ = plt.figure(figsize=size)
    axis = plt.gca()

    for _, row in table.iterrows():
        if row.family in _RECTANGLE_ELEMENTS:
            axis.add_patch(
                mpatches.Rectangle(
                    np.array([row.pos - row.L / 2, 0.0]) + offset_array,
                    row.L,
                    np.sign(row.ANGLE) * _MIN_HEIGTH + row.ANGLE / angle_max * (1 - _MIN_HEIGTH),
                    color="#0099FF",
                    alpha=1.0,
                )
            )

        elif row.family.upper() == "QUADRUPOLE":
            if row.K1 >= 0:
                # FOCUSSING QUAD
                axis.add_patch(
                    mpatches.Ellipse(
                        offset_array + np.array([row.pos, 0.0]),
                        row.L,
                        _MIN_HEIGTH + abs(row.K1 / k_max) * (1 - _MIN_HEIGTH),
                        color="green",
                        alpha=1.0,
                    )
                )
            else:
                Path = mpath.Path
                h = _MIN_HEIGTH + abs(row.K1 / k_max) * (
                    1 - _MIN_HEIGTH
                )  # abs(row.K1 / k_max) + _MIN_HEIGTH / 2
                dx = row.L
                verts = np.array(
                    [
                        (dx, h),
                        (-dx, h),
                        (-dx / 4, 0),
                        (-dx, -h),
                        (dx, -h),
                        (dx / 4, 0),
                        (dx, h),
                    ]
                )

                codes = [
                    Path.MOVETO,
                    Path.LINETO,
                    Path.CURVE3,
                    Path.LINETO,
                    Path.LINETO,
                    Path.CURVE3,
                    Path.CURVE3,
                ]

                path = mpath.Path(verts + offset_array + np.array([row.pos, 0.0]), codes)
                patch = mpatches.PathPatch(path, color="green", alpha=1.0)
                axis.add_patch(patch)
        elif row.family in ["SEXTUPOLE"]:
            axis.add_patch(
                mpatches.RegularPolygon(
                    np.array([row.pos, 0.0]) + offset_array,
                    6,
                    row.L / 2,
                    color="#FF99FF",
                    alpha=1.0,
                )
            )
        elif row.family in ["MONITOR"]:
            Path = mpath.Path
            h = 0.25
            offs_mon = np.array([0.0, 0.03])

            verts = np.array([(0, h), (0, -h), (h, 0), (-h, 0)])

            codes = [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]

            verts += offs_mon

            path = mpath.Path(verts + offset_array + np.array([row.pos, 0.0]), codes)
            patch = mpatches.PathPatch(path, color="black", lw=2, alpha=1.0 * 0.5)
            axis.add_patch(patch)
            axis.add_patch(
                mpatches.Circle(
                    offset_array + offs_mon + np.array([row.pos, 0.0]),
                    h / 2,
                    color="black",
                    alpha=1.0 * 0.25,
                )
            )
        elif row.family in ["MARKER"]:
            Path = mpath.Path
            h = 1.0
            offs_mon = np.array([0.0, 0.03])

            verts = np.array(
                [
                    (0, h),
                    (0, -h),
                ]
            )

            codes = [Path.MOVETO, Path.LINETO]

            verts += offs_mon

            path = mpath.Path(verts + offset_array + np.array([row.pos, 0.0]), codes)
            patch = mpatches.PathPatch(path, color="red", lw=2, alpha=1.0 * 0.5)
            axis.add_patch(patch)

        elif row.family in ["CAVITY"]:
            axis.add_patch(
                mpatches.Ellipse(
                    np.array([row.pos - row.L, 0.0]),
                    row.L,
                    2 * row.L,
                    angle=0,
                    color="#08bad1",
                    alpha=1 * 0.5,
                )
            )

        elif row.family in ["RFMODE"]:
            axis.add_patch(
                mpatches.Ellipse(
                    np.array([row.pos - row.L / 2, 0.0]),
                    row.L,
                    10 * row.L,
                    angle=0,
                    color="#f2973d",
                    alpha=1 * 0.5,
                )
            )

        elif row.family in ["DRIFT"]:
            axis.add_patch(
                mpatches.Rectangle(
                    np.array([row.pos - row.L / 2, -_MIN_HEIGTH]),
                    row.L,
                    2 * _MIN_HEIGTH,
                    color="black",
                    alpha=1 * 0.4,
                )
            )

        if anno:
            annotation = axis.annotate(
                row.family + ": " + row["name"],
                xy=(row.pos + offset_array[0], 0 + offset_array[1]),
                # xycoords='data',
                xytext=(row.pos + offset_array[0], 0 + offset_array[1]),
                # textcoords='data',
                horizontalalignment="left",
                # arrowprops=dict(arrowstyle="simple",),# connectionstyle="arc3,rad=+0.2"),
                # bbox=dict(boxstyle="round", facecolor="w", edgecolor="0.5", alpha=0.9),
                fontsize=8,
                rotation=90,
            )
    plt.xlim(start, stop)
    plt.ylim(-1.1, 1.1)
    plt.xlabel("S[m]")
    #     plt.grid()
    return plt, axis


def twissplot(
    tw, cols=["betx", "bety", "dx"], cpymadtwiss=True, beamlinegraph=False, *args, **kwargs
):
    """
    Method to plot columns from the twiss table output using cpymadtwiss.
    """
    if cpymadtwiss:
        if beamlinegraph:
            plot, ax = Beamlinegraph_from_seq_file(
                kwargs.get("sequence"),
                offset_array=kwargs.get("offset_array", np.array([0.0, 0.0])),
                start=kwargs.get("start", 0.0),
                stop=kwargs.get("stop", None),
                anno=kwargs.get("anno", False),
            )
        else:
            _ = plt.figure(figsize=kwargs.get("size", (12, 6)))
            plot = plt.gcf()
            ax = plt.gca()

        linestyle_cycler = ["-", "--", ":", "-."]
        if isinstance(tw, list):
            for i, twi in enumerate(tw):
                ax.set_prop_cycle(
                    cycler(
                        "color",
                        [
                            "#1f77b4",
                            "#ff7f0e",
                            "#2ca02c",
                            "#d62728",
                            "#9467bd",
                            "#8c564b",
                            "#e377c2",
                            "#7f7f7f",
                            "#bcbd22",
                            "#17becf",
                        ],
                    )
                    * cycler("linestyle", [linestyle_cycler[i]])
                )
                # ax.rc('axes', prop_cycle=linestyle_cycler)
                for col in cols:
                    ax.plot(twi.get("s"), twi.get(col), label=col + "_{}".format(i))
        else:
            for col in cols:
                ax.plot(tw.get("s"), tw.get(col), label=col)

        ax.legend()
        ax.relim()
        ax.autoscale()
        return plot, ax

    else:
        print("Not implemented yet!!!")
        pass
