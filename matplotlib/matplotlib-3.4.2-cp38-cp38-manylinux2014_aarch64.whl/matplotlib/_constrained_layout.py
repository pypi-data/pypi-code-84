"""
Adjust subplot layouts so that there are no overlapping axes or axes
decorations.  All axes decorations are dealt with (labels, ticks, titles,
ticklabels) and some dependent artists are also dealt with (colorbar,
suptitle).

Layout is done via `~matplotlib.gridspec`, with one constraint per gridspec,
so it is possible to have overlapping axes if the gridspecs overlap (i.e.
using `~matplotlib.gridspec.GridSpecFromSubplotSpec`).  Axes placed using
``figure.subplots()`` or ``figure.add_subplots()`` will participate in the
layout.  Axes manually placed via ``figure.add_axes()`` will not.

See Tutorial: :doc:`/tutorials/intermediate/constrainedlayout_guide`
"""

import logging

import numpy as np

from matplotlib import _api
import matplotlib.transforms as mtransforms

_log = logging.getLogger(__name__)

"""
General idea:
-------------

First, a figure has a gridspec that divides the figure into nrows and ncols,
with heights and widths set by ``height_ratios`` and ``width_ratios``,
often just set to 1 for an equal grid.

Subplotspecs that are derived from this gridspec can contain either a
``SubPanel``, a ``GridSpecFromSubplotSpec``, or an axes.  The ``SubPanel`` and
``GridSpecFromSubplotSpec`` are dealt with recursively and each contain an
analogous layout.

Each ``GridSpec`` has a ``_layoutgrid`` attached to it.  The ``_layoutgrid``
has the same logical layout as the ``GridSpec``.   Each row of the grid spec
has a top and bottom "margin" and each column has a left and right "margin".
The "inner" height of each row is constrained to be the same (or as modified
by ``height_ratio``), and the "inner" width of each column is
constrained to be the same (as modified by ``width_ratio``), where "inner"
is the width or height of each column/row minus the size of the margins.

Then the size of the margins for each row and column are determined as the
max width of the decorators on each axes that has decorators in that margin.
For instance, a normal axes would have a left margin that includes the
left ticklabels, and the ylabel if it exists.  The right margin may include a
colorbar, the bottom margin the xaxis decorations, and the top margin the
title.

With these constraints, the solver then finds appropriate bounds for the
columns and rows.  It's possible that the margins take up the whole figure,
in which case the algorithm is not applied and a warning is raised.

See the tutorial doc:`/tutorials/intermediate/constrainedlayout_guide`
for more discussion of the algorithm with examples.
"""


######################################################
def do_constrained_layout(fig, renderer, h_pad, w_pad,
                          hspace=None, wspace=None):
    """
    Do the constrained_layout.  Called at draw time in
     ``figure.constrained_layout()``

    Parameters
    ----------
    fig : Figure
        ``Figure`` instance to do the layout in.

    renderer : Renderer
        Renderer to use.

    h_pad, w_pad : float
      Padding around the axes elements in figure-normalized units.

    hspace, wspace : float
       Fraction of the figure to dedicate to space between the
       axes.  These are evenly spread between the gaps between the axes.
       A value of 0.2 for a three-column layout would have a space
       of 0.1 of the figure width between each column.
       If h/wspace < h/w_pad, then the pads are used instead.
    """

    # list of unique gridspecs that contain child axes:
    gss = set()
    for ax in fig.axes:
        if hasattr(ax, 'get_subplotspec'):
            gs = ax.get_subplotspec().get_gridspec()
            if gs._layoutgrid is not None:
                gss.add(gs)
    gss = list(gss)
    if len(gss) == 0:
        _api.warn_external('There are no gridspecs with layoutgrids. '
                           'Possibly did not call parent GridSpec with the'
                           ' "figure" keyword')

    for _ in range(2):
        # do the algorithm twice.  This has to be done because decorations
        # change size after the first re-position (i.e. x/yticklabels get
        # larger/smaller).  This second reposition tends to be much milder,
        # so doing twice makes things work OK.

        # make margins for all the axes and subfigures in the
        # figure.  Add margins for colorbars...
        _make_layout_margins(fig, renderer, h_pad=h_pad, w_pad=w_pad,
                             hspace=hspace, wspace=wspace)
        _make_margin_suptitles(fig, renderer, h_pad=h_pad, w_pad=w_pad)

        # if a layout is such that a columns (or rows) margin has no
        # constraints, we need to make all such instances in the grid
        # match in margin size.
        _match_submerged_margins(fig)

        # update all the variables in the layout.
        fig._layoutgrid.update_variables()

        if _check_no_collapsed_axes(fig):
            _reposition_axes(fig, renderer, h_pad=h_pad, w_pad=w_pad,
                             hspace=hspace, wspace=wspace)
        else:
            _api.warn_external('constrained_layout not applied because '
                               'axes sizes collapsed to zero.  Try making '
                               'figure larger or axes decorations smaller.')
        _reset_margins(fig)


def _check_no_collapsed_axes(fig):
    """
    Check that no axes have collapsed to zero size.
    """
    for panel in fig.subfigs:
        ok = _check_no_collapsed_axes(panel)
        if not ok:
            return False

    for ax in fig.axes:
        if hasattr(ax, 'get_subplotspec'):
            gs = ax.get_subplotspec().get_gridspec()
            lg = gs._layoutgrid
            if lg is not None:
                for i in range(gs.nrows):
                    for j in range(gs.ncols):
                        bb = lg.get_inner_bbox(i, j)
                        if bb.width <= 0 or bb.height <= 0:
                            return False
    return True


def _get_margin_from_padding(object, *, w_pad=0, h_pad=0,
                             hspace=0, wspace=0):

    ss = object._subplotspec
    gs = ss.get_gridspec()
    lg = gs._layoutgrid

    if hasattr(gs, 'hspace'):
        _hspace = (gs.hspace if gs.hspace is not None else hspace)
        _wspace = (gs.wspace if gs.wspace is not None else wspace)
    else:
        _hspace = (gs._hspace if gs._hspace is not None else hspace)
        _wspace = (gs._wspace if gs._wspace is not None else wspace)

    _wspace = _wspace / 2
    _hspace = _hspace / 2

    nrows, ncols = gs.get_geometry()
    # there are two margins for each direction.  The "cb"
    # margins are for pads and colorbars, the non-"cb" are
    # for the axes decorations (labels etc).
    margin = {'leftcb': w_pad, 'rightcb': w_pad,
              'bottomcb': h_pad, 'topcb': h_pad,
              'left': 0, 'right': 0,
              'top': 0, 'bottom': 0}
    if _wspace / ncols > w_pad:
        if ss.colspan.start > 0:
            margin['leftcb'] = _wspace / ncols
        if ss.colspan.stop < ncols:
            margin['rightcb'] = _wspace / ncols
    if _hspace / nrows > h_pad:
        if ss.rowspan.stop < nrows:
            margin['bottomcb'] = _hspace / nrows
        if ss.rowspan.start > 0:
            margin['topcb'] = _hspace / nrows

    return margin


def _make_layout_margins(fig, renderer, *, w_pad=0, h_pad=0,
                         hspace=0, wspace=0):
    """
    For each axes, make a margin between the *pos* layoutbox and the
    *axes* layoutbox be a minimum size that can accommodate the
    decorations on the axis.

    Then make room for colorbars.
    """
    for panel in fig.subfigs:  # recursively make child panel margins
        ss = panel._subplotspec
        _make_layout_margins(panel, renderer, w_pad=w_pad, h_pad=h_pad,
                             hspace=hspace, wspace=wspace)

        margins = _get_margin_from_padding(panel, w_pad=0, h_pad=0,
                                           hspace=hspace, wspace=wspace)
        panel._layoutgrid.parent.edit_outer_margin_mins(margins, ss)

    for ax in fig._localaxes.as_list():
        if not hasattr(ax, 'get_subplotspec') or not ax.get_in_layout():
            continue

        ss = ax.get_subplotspec()
        gs = ss.get_gridspec()
        nrows, ncols = gs.get_geometry()

        if gs._layoutgrid is None:
            return

        margin = _get_margin_from_padding(ax, w_pad=w_pad, h_pad=h_pad,
                                           hspace=hspace, wspace=wspace)
        margin0 = margin.copy()
        pos, bbox = _get_pos_and_bbox(ax, renderer)
        # the margin is the distance between the bounding box of the axes
        # and its position (plus the padding from above)
        margin['left'] += pos.x0 - bbox.x0
        margin['right'] += bbox.x1 - pos.x1
        # remember that rows are ordered from top:
        margin['bottom'] += pos.y0 - bbox.y0
        margin['top'] += bbox.y1 - pos.y1

        # make margin for colorbars.  These margins go in the
        # padding margin, versus the margin for axes decorators.
        for cbax in ax._colorbars:
            # note pad is a fraction of the parent width...
            pad = _colorbar_get_pad(cbax)
            # colorbars can be child of more than one subplot spec:
            cbp_rspan, cbp_cspan = _get_cb_parent_spans(cbax)
            loc = cbax._colorbar_info['location']
            cbpos, cbbbox = _get_pos_and_bbox(cbax, renderer)
            if loc == 'right':
                if cbp_cspan.stop == ss.colspan.stop:
                    # only increase if the colorbar is on the right edge
                    margin['rightcb'] += cbbbox.width + pad
            elif loc == 'left':
                if cbp_cspan.start == ss.colspan.start:
                    # only increase if the colorbar is on the left edge
                    margin['leftcb'] += cbbbox.width + pad
            elif loc == 'top':
                if cbp_rspan.start == ss.rowspan.start:
                    margin['topcb'] += cbbbox.height + pad
            else:
                if cbp_rspan.stop == ss.rowspan.stop:
                    margin['bottomcb'] += cbbbox.height + pad
            # If the colorbars are wider than the parent box in the
            # cross direction
            if loc in ['top', 'bottom']:
                if (cbp_cspan.start == ss.colspan.start and
                        cbbbox.x0 < bbox.x0):
                    margin['left'] += bbox.x0 - cbbbox.x0
                if (cbp_cspan.stop == ss.colspan.stop and
                        cbbbox.x1 > bbox.x1):
                    margin['right'] += cbbbox.x1 - bbox.x1
            # or taller:
            if loc in ['left', 'right']:
                if (cbp_rspan.stop == ss.rowspan.stop and
                        cbbbox.y0 < bbox.y0):
                    margin['bottom'] += bbox.y0 - cbbbox.y0
                if (cbp_rspan.start == ss.rowspan.start and
                        cbbbox.y1 > bbox.y1):
                    margin['top'] += cbbbox.y1 - bbox.y1
        # pass the new margins down to the layout grid for the solution...
        gs._layoutgrid.edit_outer_margin_mins(margin, ss)


def _make_margin_suptitles(fig, renderer, *, w_pad=0, h_pad=0):
    # Figure out how large the suptitle is and make the
    # top level figure margin larger.

    inv_trans_fig = fig.transFigure.inverted().transform_bbox
    # get the h_pad and w_pad as distances in the local subfigure coordinates:
    padbox = mtransforms.Bbox([[0, 0], [w_pad, h_pad]])
    padbox = (fig.transFigure -
                   fig.transSubfigure).transform_bbox(padbox)
    h_pad_local = padbox.height
    w_pad_local = padbox.width

    for panel in fig.subfigs:
        _make_margin_suptitles(panel, renderer, w_pad=w_pad, h_pad=h_pad)

    if fig._suptitle is not None and fig._suptitle.get_in_layout():
        p = fig._suptitle.get_position()
        if getattr(fig._suptitle, '_autopos', False):
            fig._suptitle.set_position((p[0], 1 - h_pad_local))
            bbox = inv_trans_fig(fig._suptitle.get_tightbbox(renderer))
            fig._layoutgrid.edit_margin_min('top', bbox.height + 2 * h_pad)

    if fig._supxlabel is not None and fig._supxlabel.get_in_layout():
        p = fig._supxlabel.get_position()
        if getattr(fig._supxlabel, '_autopos', False):
            fig._supxlabel.set_position((p[0], h_pad_local))
            bbox = inv_trans_fig(fig._supxlabel.get_tightbbox(renderer))
            fig._layoutgrid.edit_margin_min('bottom', bbox.height + 2 * h_pad)

    if fig._supylabel is not None and fig._supxlabel.get_in_layout():
        p = fig._supylabel.get_position()
        if getattr(fig._supylabel, '_autopos', False):
            fig._supylabel.set_position((w_pad_local, p[1]))
            bbox = inv_trans_fig(fig._supylabel.get_tightbbox(renderer))
            fig._layoutgrid.edit_margin_min('left', bbox.width + 2 * w_pad)


def _match_submerged_margins(fig):
    """
    Make the margins that are submerged inside an Axes the same size.

    This allows axes that span two columns (or rows) that are offset
    from one another to have the same size.

    This gives the proper layout for something like::
        fig = plt.figure(constrained_layout=True)
        axs = fig.subplot_mosaic("AAAB\nCCDD")

    Without this routine, the axes D will be wider than C, because the
    margin width between the two columns in C has no width by default,
    whereas the margins between the two columns of D are set by the
    width of the margin between A and B. However, obviously the user would
    like C and D to be the same size, so we need to add constraints to these
    "submerged" margins.

    This routine makes all the interior margins the same, and the spacing
    between the three columns in A and the two column in C are all set to the
    margins between the two columns of D.

    See test_constrained_layout::test_constrained_layout12 for an example.
    """

    for panel in fig.subfigs:
        _match_submerged_margins(panel)

    axs = [a for a in fig.get_axes() if (hasattr(a, 'get_subplotspec')
                                         and a.get_in_layout())]

    for ax1 in axs:
        ss1 = ax1.get_subplotspec()
        lg1 = ss1.get_gridspec()._layoutgrid
        if lg1 is None:
            axs.remove(ax1)
            continue

        # interior columns:
        if len(ss1.colspan) > 1:
            maxsubl = np.max(
                lg1.margin_vals['left'][ss1.colspan[1:]] +
                lg1.margin_vals['leftcb'][ss1.colspan[1:]]
            )
            maxsubr = np.max(
                lg1.margin_vals['right'][ss1.colspan[:-1]] +
                lg1.margin_vals['rightcb'][ss1.colspan[:-1]]
            )
            for ax2 in axs:
                ss2 = ax2.get_subplotspec()
                lg2 = ss2.get_gridspec()._layoutgrid
                if lg2 is not None and len(ss2.colspan) > 1:
                    maxsubl2 = np.max(
                        lg2.margin_vals['left'][ss2.colspan[1:]] +
                        lg2.margin_vals['leftcb'][ss2.colspan[1:]])
                    if maxsubl2 > maxsubl:
                        maxsubl = maxsubl2
                    maxsubr2 = np.max(
                        lg2.margin_vals['right'][ss2.colspan[:-1]] +
                        lg2.margin_vals['rightcb'][ss2.colspan[:-1]])
                    if maxsubr2 > maxsubr:
                        maxsubr = maxsubr2
            for i in ss1.colspan[1:]:
                lg1.edit_margin_min('left', maxsubl, cell=i)
            for i in ss1.colspan[:-1]:
                lg1.edit_margin_min('right', maxsubr, cell=i)

        # interior rows:
        if len(ss1.rowspan) > 1:
            maxsubt = np.max(
                lg1.margin_vals['top'][ss1.rowspan[1:]] +
                lg1.margin_vals['topcb'][ss1.rowspan[1:]]
            )
            maxsubb = np.max(
                lg1.margin_vals['bottom'][ss1.rowspan[:-1]] +
                lg1.margin_vals['bottomcb'][ss1.rowspan[:-1]]
            )

            for ax2 in axs:
                ss2 = ax2.get_subplotspec()
                lg2 = ss2.get_gridspec()._layoutgrid
                if lg2 is not None:
                    if len(ss2.rowspan) > 1:
                        maxsubt = np.max([np.max(
                            lg2.margin_vals['top'][ss2.rowspan[1:]] +
                            lg2.margin_vals['topcb'][ss2.rowspan[1:]]
                        ), maxsubt])
                        maxsubb = np.max([np.max(
                            lg2.margin_vals['bottom'][ss2.rowspan[:-1]] +
                            lg2.margin_vals['bottomcb'][ss2.rowspan[:-1]]
                        ), maxsubb])
            for i in ss1.rowspan[1:]:
                lg1.edit_margin_min('top', maxsubt, cell=i)
            for i in ss1.rowspan[:-1]:
                lg1.edit_margin_min('bottom', maxsubb, cell=i)


def _get_cb_parent_spans(cbax):
    """
    Figure out which subplotspecs this colorbar belongs to:
    """
    rowstart = np.inf
    rowstop = -np.inf
    colstart = np.inf
    colstop = -np.inf
    for parent in cbax._colorbar_info['parents']:
        ss = parent.get_subplotspec()
        rowstart = min(ss.rowspan.start, rowstart)
        rowstop = max(ss.rowspan.stop, rowstop)
        colstart = min(ss.colspan.start, colstart)
        colstop = max(ss.colspan.stop, colstop)

    rowspan = range(rowstart, rowstop)
    colspan = range(colstart, colstop)
    return rowspan, colspan


def _get_pos_and_bbox(ax, renderer):
    """
    Get the position and the bbox for the axes.

    Parameters
    ----------
    ax
    renderer

    Returns
    -------
    pos : Bbox
        Position in figure coordinates.
    bbox : Bbox
        Tight bounding box in figure coordinates.

    """
    fig = ax.figure
    pos = ax.get_position(original=True)
    # pos is in panel co-ords, but we need in figure for the layout
    pos = pos.transformed(fig.transSubfigure - fig.transFigure)
    try:
        tightbbox = ax.get_tightbbox(renderer=renderer, for_layout_only=True)
    except TypeError:
        tightbbox = ax.get_tightbbox(renderer=renderer)

    if tightbbox is None:
        bbox = pos
    else:
        bbox = tightbbox.transformed(fig.transFigure.inverted())
    return pos, bbox


def _reposition_axes(fig, renderer, *, w_pad=0, h_pad=0, hspace=0, wspace=0):
    """
    Reposition all the axes based on the new inner bounding box.
    """
    trans_fig_to_subfig = fig.transFigure - fig.transSubfigure
    for sfig in fig.subfigs:
        bbox = sfig._layoutgrid.get_outer_bbox()
        sfig._redo_transform_rel_fig(
            bbox=bbox.transformed(trans_fig_to_subfig))
        _reposition_axes(sfig, renderer,
                         w_pad=w_pad, h_pad=h_pad,
                         wspace=wspace, hspace=hspace)

    for ax in fig._localaxes.as_list():
        if not hasattr(ax, 'get_subplotspec') or not ax.get_in_layout():
            continue

        # grid bbox is in Figure coordinates, but we specify in panel
        # coordinates...
        ss = ax.get_subplotspec()
        gs = ss.get_gridspec()
        nrows, ncols = gs.get_geometry()
        if gs._layoutgrid is None:
            return

        bbox = gs._layoutgrid.get_inner_bbox(rows=ss.rowspan, cols=ss.colspan)

        bboxouter = gs._layoutgrid.get_outer_bbox(rows=ss.rowspan,
                                                  cols=ss.colspan)

        # transform from figure to panel for set_position:
        newbbox = trans_fig_to_subfig.transform_bbox(bbox)
        ax._set_position(newbbox)

        # move the colorbars:
        # we need to keep track of oldw and oldh if there is more than
        # one colorbar:
        offset = {'left': 0, 'right': 0, 'bottom': 0, 'top': 0}
        for nn, cbax in enumerate(ax._colorbars[::-1]):
            if ax == cbax._colorbar_info['parents'][0]:
                margin = _reposition_colorbar(
                    cbax, renderer, offset=offset)


def _reposition_colorbar(cbax, renderer, *, offset=None):
    """
    Place the colorbar in its new place.

    Parameters
    ----------
    cbax : Axes
        Axes for the colorbar

    renderer :
    w_pad, h_pad : float
        width and height padding (in fraction of figure)
    hspace, wspace : float
        width and height padding as fraction of figure size divided by
        number of  columns or rows
    margin : array-like
        offset the colorbar needs to be pushed to in order to
        account for multiple colorbars
    """

    parents = cbax._colorbar_info['parents']
    gs = parents[0].get_gridspec()
    ncols, nrows = gs.ncols, gs.nrows
    fig = cbax.figure
    trans_fig_to_subfig = fig.transFigure - fig.transSubfigure

    cb_rspans, cb_cspans = _get_cb_parent_spans(cbax)
    bboxparent = gs._layoutgrid.get_bbox_for_cb(rows=cb_rspans, cols=cb_cspans)
    pb = gs._layoutgrid.get_inner_bbox(rows=cb_rspans, cols=cb_cspans)

    location = cbax._colorbar_info['location']
    anchor = cbax._colorbar_info['anchor']
    fraction = cbax._colorbar_info['fraction']
    aspect = cbax._colorbar_info['aspect']
    shrink = cbax._colorbar_info['shrink']

    cbpos, cbbbox = _get_pos_and_bbox(cbax, renderer)

    # Colorbar gets put at extreme edge of outer bbox of the subplotspec
    # It needs to be moved in by: 1) a pad 2) its "margin" 3) by
    # any colorbars already added at this location:
    cbpad = _colorbar_get_pad(cbax)
    if location in ('left', 'right'):
        # fraction and shrink are fractions of parent
        pbcb = pb.shrunk(fraction, shrink).anchored(anchor, pb)
        # The colorbar is at the left side of the parent.  Need
        # to translate to right (or left)
        if location == 'right':
            lmargin = cbpos.x0 - cbbbox.x0
            dx = bboxparent.x1 - pbcb.x0 + offset['right']
            dx += cbpad + lmargin
            offset['right'] += cbbbox.width + cbpad
            pbcb = pbcb.translated(dx, 0)
        else:
            lmargin = cbpos.x0 - cbbbox.x0
            dx = bboxparent.x0 - pbcb.x0  # edge of parent
            dx += -cbbbox.width - cbpad + lmargin - offset['left']
            offset['left'] += cbbbox.width + cbpad
            pbcb = pbcb.translated(dx, 0)
    else:  # horizontal axes:
        pbcb = pb.shrunk(shrink, fraction).anchored(anchor, pb)
        if location == 'top':
            bmargin = cbpos.y0 - cbbbox.y0
            dy = bboxparent.y1 - pbcb.y0 + offset['top']
            dy += cbpad + bmargin
            offset['top'] += cbbbox.height + cbpad
            pbcb = pbcb.translated(0, dy)
        else:
            bmargin = cbpos.y0 - cbbbox.y0
            dy = bboxparent.y0 - pbcb.y0
            dy += -cbbbox.height - cbpad + bmargin - offset['bottom']
            offset['bottom'] += cbbbox.height + cbpad
            pbcb = pbcb.translated(0, dy)

    pbcb = trans_fig_to_subfig.transform_bbox(pbcb)
    cbax.set_transform(fig.transSubfigure)
    cbax._set_position(pbcb)
    cbax.set_aspect(aspect, anchor=anchor, adjustable='box')
    return offset


def _reset_margins(fig):
    """
    Reset the margins in the layoutboxes of fig.

    Margins are usually set as a minimum, so if the figure gets smaller
    the minimum needs to be zero in order for it to grow again.
    """
    for span in fig.subfigs:
        _reset_margins(span)
    for ax in fig.axes:
        if hasattr(ax, 'get_subplotspec') and ax.get_in_layout():
            ss = ax.get_subplotspec()
            gs = ss.get_gridspec()
            if gs._layoutgrid is not None:
                gs._layoutgrid.reset_margins()
    fig._layoutgrid.reset_margins()


def _colorbar_get_pad(cax):
    parents = cax._colorbar_info['parents']
    gs = parents[0].get_gridspec()

    cb_rspans, cb_cspans = _get_cb_parent_spans(cax)
    bboxouter = gs._layoutgrid.get_inner_bbox(rows=cb_rspans, cols=cb_cspans)

    if cax._colorbar_info['location'] in ['right', 'left']:
        size = bboxouter.width
    else:
        size = bboxouter.height

    return cax._colorbar_info['pad'] * size
