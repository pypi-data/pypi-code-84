r"""
:mod:`~matplotlib.gridspec` contains classes that help to layout multiple
`~.axes.Axes` in a grid-like pattern within a figure.

The `GridSpec` specifies the overall grid structure. Individual cells within
the grid are referenced by `SubplotSpec`\s.

See the tutorial :doc:`/tutorials/intermediate/gridspec` for a comprehensive
usage guide.
"""

import copy
import logging
from numbers import Integral

import numpy as np

import matplotlib as mpl
from matplotlib import _api, _pylab_helpers, tight_layout, rcParams
from matplotlib.transforms import Bbox
import matplotlib._layoutgrid as layoutgrid


_log = logging.getLogger(__name__)


class GridSpecBase:
    """
    A base class of GridSpec that specifies the geometry of the grid
    that a subplot will be placed.
    """

    def __init__(self, nrows, ncols, height_ratios=None, width_ratios=None):
        """
        Parameters
        ----------
        nrows, ncols : int
            The number of rows and columns of the grid.
        width_ratios : array-like of length *ncols*, optional
            Defines the relative widths of the columns. Each column gets a
            relative width of ``width_ratios[i] / sum(width_ratios)``.
            If not given, all columns will have the same width.
        height_ratios : array-like of length *nrows*, optional
            Defines the relative heights of the rows. Each column gets a
            relative height of ``height_ratios[i] / sum(height_ratios)``.
            If not given, all rows will have the same height.
        """
        if not isinstance(nrows, Integral) or nrows <= 0:
            raise ValueError(
                f"Number of rows must be a positive integer, not {nrows}")
        if not isinstance(ncols, Integral) or ncols <= 0:
            raise ValueError(
                f"Number of columns must be a positive integer, not {ncols}")
        self._nrows, self._ncols = nrows, ncols
        self.set_height_ratios(height_ratios)
        self.set_width_ratios(width_ratios)

    def __repr__(self):
        height_arg = (', height_ratios=%r' % (self._row_height_ratios,)
                      if len(set(self._row_height_ratios)) != 1 else '')
        width_arg = (', width_ratios=%r' % (self._col_width_ratios,)
                     if len(set(self._col_width_ratios)) != 1 else '')
        return '{clsname}({nrows}, {ncols}{optionals})'.format(
            clsname=self.__class__.__name__,
            nrows=self._nrows,
            ncols=self._ncols,
            optionals=height_arg + width_arg,
            )

    nrows = property(lambda self: self._nrows,
                     doc="The number of rows in the grid.")
    ncols = property(lambda self: self._ncols,
                     doc="The number of columns in the grid.")

    def get_geometry(self):
        """
        Return a tuple containing the number of rows and columns in the grid.
        """
        return self._nrows, self._ncols

    def get_subplot_params(self, figure=None):
        # Must be implemented in subclasses
        pass

    def new_subplotspec(self, loc, rowspan=1, colspan=1):
        """
        Create and return a `.SubplotSpec` instance.

        Parameters
        ----------
        loc : (int, int)
            The position of the subplot in the grid as
            ``(row_index, column_index)``.
        rowspan, colspan : int, default: 1
            The number of rows and columns the subplot should span in the grid.
        """
        loc1, loc2 = loc
        subplotspec = self[loc1:loc1+rowspan, loc2:loc2+colspan]
        return subplotspec

    def set_width_ratios(self, width_ratios):
        """
        Set the relative widths of the columns.

        *width_ratios* must be of length *ncols*. Each column gets a relative
        width of ``width_ratios[i] / sum(width_ratios)``.
        """
        if width_ratios is None:
            width_ratios = [1] * self._ncols
        elif len(width_ratios) != self._ncols:
            raise ValueError('Expected the given number of width ratios to '
                             'match the number of columns of the grid')
        self._col_width_ratios = width_ratios

    def get_width_ratios(self):
        """
        Return the width ratios.

        This is *None* if no width ratios have been set explicitly.
        """
        return self._col_width_ratios

    def set_height_ratios(self, height_ratios):
        """
        Set the relative heights of the rows.

        *height_ratios* must be of length *nrows*. Each row gets a relative
        height of ``height_ratios[i] / sum(height_ratios)``.
        """
        if height_ratios is None:
            height_ratios = [1] * self._nrows
        elif len(height_ratios) != self._nrows:
            raise ValueError('Expected the given number of height ratios to '
                             'match the number of rows of the grid')
        self._row_height_ratios = height_ratios

    def get_height_ratios(self):
        """
        Return the height ratios.

        This is *None* if no height ratios have been set explicitly.
        """
        return self._row_height_ratios

    def get_grid_positions(self, fig, raw=False):
        """
        Return the positions of the grid cells in figure coordinates.

        Parameters
        ----------
        fig : `~matplotlib.figure.Figure`
            The figure the grid should be applied to. The subplot parameters
            (margins and spacing between subplots) are taken from *fig*.
        raw : bool, default: False
            If *True*, the subplot parameters of the figure are not taken
            into account. The grid spans the range [0, 1] in both directions
            without margins and there is no space between grid cells. This is
            used for constrained_layout.

        Returns
        -------
        bottoms, tops, lefts, rights : array
            The bottom, top, left, right positions of the grid cells in
            figure coordinates.
        """
        nrows, ncols = self.get_geometry()

        if raw:
            left = 0.
            right = 1.
            bottom = 0.
            top = 1.
            wspace = 0.
            hspace = 0.
        else:
            subplot_params = self.get_subplot_params(fig)
            left = subplot_params.left
            right = subplot_params.right
            bottom = subplot_params.bottom
            top = subplot_params.top
            wspace = subplot_params.wspace
            hspace = subplot_params.hspace
        tot_width = right - left
        tot_height = top - bottom

        # calculate accumulated heights of columns
        cell_h = tot_height / (nrows + hspace*(nrows-1))
        sep_h = hspace * cell_h
        norm = cell_h * nrows / sum(self._row_height_ratios)
        cell_heights = [r * norm for r in self._row_height_ratios]
        sep_heights = [0] + ([sep_h] * (nrows-1))
        cell_hs = np.cumsum(np.column_stack([sep_heights, cell_heights]).flat)

        # calculate accumulated widths of rows
        cell_w = tot_width / (ncols + wspace*(ncols-1))
        sep_w = wspace * cell_w
        norm = cell_w * ncols / sum(self._col_width_ratios)
        cell_widths = [r * norm for r in self._col_width_ratios]
        sep_widths = [0] + ([sep_w] * (ncols-1))
        cell_ws = np.cumsum(np.column_stack([sep_widths, cell_widths]).flat)

        fig_tops, fig_bottoms = (top - cell_hs).reshape((-1, 2)).T
        fig_lefts, fig_rights = (left + cell_ws).reshape((-1, 2)).T
        return fig_bottoms, fig_tops, fig_lefts, fig_rights

    @staticmethod
    def _check_gridspec_exists(figure, nrows, ncols):
        """
        Check if the figure already has a gridspec with these dimensions,
        or create a new one
        """
        for ax in figure.get_axes():
            if hasattr(ax, 'get_subplotspec'):
                gs = ax.get_subplotspec().get_gridspec()
                if hasattr(gs, 'get_topmost_subplotspec'):
                    # This is needed for colorbar gridspec layouts.
                    # This is probably OK because this whole logic tree
                    # is for when the user is doing simple things with the
                    # add_subplot command.  For complicated layouts
                    # like subgridspecs the proper gridspec is passed in...
                    gs = gs.get_topmost_subplotspec().get_gridspec()
                if gs.get_geometry() == (nrows, ncols):
                    return gs
        # else gridspec not found:
        return GridSpec(nrows, ncols, figure=figure)

    def __getitem__(self, key):
        """Create and return a `.SubplotSpec` instance."""
        nrows, ncols = self.get_geometry()

        def _normalize(key, size, axis):  # Includes last index.
            orig_key = key
            if isinstance(key, slice):
                start, stop, _ = key.indices(size)
                if stop > start:
                    return start, stop - 1
                raise IndexError("GridSpec slice would result in no space "
                                 "allocated for subplot")
            else:
                if key < 0:
                    key = key + size
                if 0 <= key < size:
                    return key, key
                elif axis is not None:
                    raise IndexError(f"index {orig_key} is out of bounds for "
                                     f"axis {axis} with size {size}")
                else:  # flat index
                    raise IndexError(f"index {orig_key} is out of bounds for "
                                     f"GridSpec with size {size}")

        if isinstance(key, tuple):
            try:
                k1, k2 = key
            except ValueError as err:
                raise ValueError("Unrecognized subplot spec") from err
            num1, num2 = np.ravel_multi_index(
                [_normalize(k1, nrows, 0), _normalize(k2, ncols, 1)],
                (nrows, ncols))
        else:  # Single key
            num1, num2 = _normalize(key, nrows * ncols, None)

        return SubplotSpec(self, num1, num2)

    def subplots(self, *, sharex=False, sharey=False, squeeze=True,
                 subplot_kw=None):
        """
        Add all subplots specified by this `GridSpec` to its parent figure.

        See `.Figure.subplots` for detailed documentation.
        """

        figure = self.figure

        if figure is None:
            raise ValueError("GridSpec.subplots() only works for GridSpecs "
                             "created with a parent figure")

        if isinstance(sharex, bool):
            sharex = "all" if sharex else "none"
        if isinstance(sharey, bool):
            sharey = "all" if sharey else "none"
        # This check was added because it is very easy to type
        # `subplots(1, 2, 1)` when `subplot(1, 2, 1)` was intended.
        # In most cases, no error will ever occur, but mysterious behavior
        # will result because what was intended to be the subplot index is
        # instead treated as a bool for sharex.  This check should go away
        # once sharex becomes kwonly.
        if isinstance(sharex, Integral):
            _api.warn_external(
                "sharex argument to subplots() was an integer.  Did you "
                "intend to use subplot() (without 's')?")
        _api.check_in_list(["all", "row", "col", "none"],
                           sharex=sharex, sharey=sharey)
        if subplot_kw is None:
            subplot_kw = {}
        # don't mutate kwargs passed by user...
        subplot_kw = subplot_kw.copy()

        # Create array to hold all axes.
        axarr = np.empty((self._nrows, self._ncols), dtype=object)
        for row in range(self._nrows):
            for col in range(self._ncols):
                shared_with = {"none": None, "all": axarr[0, 0],
                               "row": axarr[row, 0], "col": axarr[0, col]}
                subplot_kw["sharex"] = shared_with[sharex]
                subplot_kw["sharey"] = shared_with[sharey]
                axarr[row, col] = figure.add_subplot(
                    self[row, col], **subplot_kw)

        # turn off redundant tick labeling
        if sharex in ["col", "all"]:
            for ax in axarr[:-1, :].flat:  # Remove bottom labels/offsettexts.
                ax.xaxis.set_tick_params(which="both", labelbottom=False)
                if ax.xaxis.offsetText.get_position()[1] == 0:
                    ax.xaxis.offsetText.set_visible(False)
            for ax in axarr[1:, :].flat:  # Remove top labels/offsettexts.
                ax.xaxis.set_tick_params(which="both", labeltop=False)
                if ax.xaxis.offsetText.get_position()[1] == 1:
                    ax.xaxis.offsetText.set_visible(False)
        if sharey in ["row", "all"]:
            for ax in axarr[:, 1:].flat:  # Remove left labels/offsettexts.
                ax.yaxis.set_tick_params(which="both", labelleft=False)
                if ax.yaxis.offsetText.get_position()[0] == 0:
                    ax.yaxis.offsetText.set_visible(False)
            for ax in axarr[:, :-1].flat:  # Remove right labels/offsettexts.
                ax.yaxis.set_tick_params(which="both", labelright=False)
                if ax.yaxis.offsetText.get_position()[0] == 1:
                    ax.yaxis.offsetText.set_visible(False)

        if squeeze:
            # Discarding unneeded dimensions that equal 1.  If we only have one
            # subplot, just return it instead of a 1-element array.
            return axarr.item() if axarr.size == 1 else axarr.squeeze()
        else:
            # Returned axis array will be always 2-d, even if nrows=ncols=1.
            return axarr


class GridSpec(GridSpecBase):
    """
    A grid layout to place subplots within a figure.

    The location of the grid cells is determined in a similar way to
    `~.figure.SubplotParams` using *left*, *right*, *top*, *bottom*, *wspace*
    and *hspace*.
    """
    def __init__(self, nrows, ncols, figure=None,
                 left=None, bottom=None, right=None, top=None,
                 wspace=None, hspace=None,
                 width_ratios=None, height_ratios=None):
        """
        Parameters
        ----------
        nrows, ncols : int
            The number of rows and columns of the grid.

        figure : `~.figure.Figure`, optional
            Only used for constrained layout to create a proper layoutgrid.

        left, right, top, bottom : float, optional
            Extent of the subplots as a fraction of figure width or height.
            Left cannot be larger than right, and bottom cannot be larger than
            top. If not given, the values will be inferred from a figure or
            rcParams at draw time. See also `GridSpec.get_subplot_params`.

        wspace : float, optional
            The amount of width reserved for space between subplots,
            expressed as a fraction of the average axis width.
            If not given, the values will be inferred from a figure or
            rcParams when necessary. See also `GridSpec.get_subplot_params`.

        hspace : float, optional
            The amount of height reserved for space between subplots,
            expressed as a fraction of the average axis height.
            If not given, the values will be inferred from a figure or
            rcParams when necessary. See also `GridSpec.get_subplot_params`.

        width_ratios : array-like of length *ncols*, optional
            Defines the relative widths of the columns. Each column gets a
            relative width of ``width_ratios[i] / sum(width_ratios)``.
            If not given, all columns will have the same width.

        height_ratios : array-like of length *nrows*, optional
            Defines the relative heights of the rows. Each column gets a
            relative height of ``height_ratios[i] / sum(height_ratios)``.
            If not given, all rows will have the same height.

        """
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top
        self.wspace = wspace
        self.hspace = hspace
        self.figure = figure

        super().__init__(nrows, ncols,
                         width_ratios=width_ratios,
                         height_ratios=height_ratios)

        # set up layoutgrid for constrained_layout:
        self._layoutgrid = None
        if self.figure is None or not self.figure.get_constrained_layout():
            self._layoutgrid = None
        else:
            self._toplayoutbox = self.figure._layoutgrid
            self._layoutgrid = layoutgrid.LayoutGrid(
                parent=self.figure._layoutgrid,
                parent_inner=True,
                name=(self.figure._layoutgrid.name + '.gridspec' +
                      layoutgrid.seq_id()),
                ncols=ncols, nrows=nrows, width_ratios=width_ratios,
                height_ratios=height_ratios)

    _AllowedKeys = ["left", "bottom", "right", "top", "wspace", "hspace"]

    def __getstate__(self):
        return {**self.__dict__, "_layoutgrid": None}

    def update(self, **kwargs):
        """
        Update the subplot parameters of the grid.

        Parameters that are not explicitly given are not changed. Setting a
        parameter to *None* resets it to :rc:`figure.subplot.*`.

        Parameters
        ----------
        left, right, top, bottom : float or None, optional
            Extent of the subplots as a fraction of figure width or height.
        wspace, hspace : float, optional
            Spacing between the subplots as a fraction of the average subplot
            width / height.
        """
        for k, v in kwargs.items():
            if k in self._AllowedKeys:
                setattr(self, k, v)
            else:
                raise AttributeError(f"{k} is an unknown keyword")
        for figmanager in _pylab_helpers.Gcf.figs.values():
            for ax in figmanager.canvas.figure.axes:
                if isinstance(ax, mpl.axes.SubplotBase):
                    ss = ax.get_subplotspec().get_topmost_subplotspec()
                    if ss.get_gridspec() == self:
                        ax._set_position(
                            ax.get_subplotspec().get_position(ax.figure))

    def get_subplot_params(self, figure=None):
        """
        Return the `~.SubplotParams` for the GridSpec.

        In order of precedence the values are taken from

        - non-*None* attributes of the GridSpec
        - the provided *figure*
        - :rc:`figure.subplot.*`
        """
        if figure is None:
            kw = {k: rcParams["figure.subplot."+k] for k in self._AllowedKeys}
            subplotpars = mpl.figure.SubplotParams(**kw)
        else:
            subplotpars = copy.copy(figure.subplotpars)

        subplotpars.update(**{k: getattr(self, k) for k in self._AllowedKeys})

        return subplotpars

    def locally_modified_subplot_params(self):
        """
        Return a list of the names of the subplot parameters explicitly set
        in the GridSpec.

        This is a subset of the attributes of `.SubplotParams`.
        """
        return [k for k in self._AllowedKeys if getattr(self, k)]

    def tight_layout(self, figure, renderer=None,
                     pad=1.08, h_pad=None, w_pad=None, rect=None):
        """
        Adjust subplot parameters to give specified padding.

        Parameters
        ----------
        pad : float
            Padding between the figure edge and the edges of subplots, as a
            fraction of the font-size.
        h_pad, w_pad : float, optional
            Padding (height/width) between edges of adjacent subplots.
            Defaults to *pad*.
        rect : tuple of 4 floats, default: (0, 0, 1, 1), i.e. the whole figure
            (left, bottom, right, top) rectangle in normalized figure
            coordinates that the whole subplots area (including labels) will
            fit into.
        """

        subplotspec_list = tight_layout.get_subplotspec_list(
            figure.axes, grid_spec=self)
        if None in subplotspec_list:
            _api.warn_external("This figure includes Axes that are not "
                               "compatible with tight_layout, so results "
                               "might be incorrect.")

        if renderer is None:
            renderer = tight_layout.get_renderer(figure)

        kwargs = tight_layout.get_tight_layout_figure(
            figure, figure.axes, subplotspec_list, renderer,
            pad=pad, h_pad=h_pad, w_pad=w_pad, rect=rect)
        if kwargs:
            self.update(**kwargs)


class GridSpecFromSubplotSpec(GridSpecBase):
    """
    GridSpec whose subplot layout parameters are inherited from the
    location specified by a given SubplotSpec.
    """
    def __init__(self, nrows, ncols,
                 subplot_spec,
                 wspace=None, hspace=None,
                 height_ratios=None, width_ratios=None):
        """
        The number of rows and number of columns of the grid need to
        be set. An instance of SubplotSpec is also needed to be set
        from which the layout parameters will be inherited. The wspace
        and hspace of the layout can be optionally specified or the
        default values (from the figure or rcParams) will be used.
        """
        self._wspace = wspace
        self._hspace = hspace
        self._subplot_spec = subplot_spec
        self.figure = self._subplot_spec.get_gridspec().figure
        super().__init__(nrows, ncols,
                         width_ratios=width_ratios,
                         height_ratios=height_ratios)
        # do the layoutgrids for constrained_layout:
        subspeclb = subplot_spec.get_gridspec()._layoutgrid
        if subspeclb is None:
            self._layoutgrid = None
        else:
            # this _toplayoutbox is a container that spans the cols and
            # rows in the parent gridspec.  Not yet implemented,
            # but we do this so that it is possible to have subgridspec
            # level artists.
            self._toplayoutgrid = layoutgrid.LayoutGrid(
                parent=subspeclb,
                name=subspeclb.name + '.top' + layoutgrid.seq_id(),
                nrows=1, ncols=1,
                parent_pos=(subplot_spec.rowspan, subplot_spec.colspan))
            self._layoutgrid = layoutgrid.LayoutGrid(
                    parent=self._toplayoutgrid,
                    name=(self._toplayoutgrid.name + '.gridspec' +
                          layoutgrid.seq_id()),
                    nrows=nrows, ncols=ncols,
                    width_ratios=width_ratios, height_ratios=height_ratios)

    def get_subplot_params(self, figure=None):
        """Return a dictionary of subplot layout parameters."""
        hspace = (self._hspace if self._hspace is not None
                  else figure.subplotpars.hspace if figure is not None
                  else rcParams["figure.subplot.hspace"])
        wspace = (self._wspace if self._wspace is not None
                  else figure.subplotpars.wspace if figure is not None
                  else rcParams["figure.subplot.wspace"])

        figbox = self._subplot_spec.get_position(figure)
        left, bottom, right, top = figbox.extents

        return mpl.figure.SubplotParams(left=left, right=right,
                                        bottom=bottom, top=top,
                                        wspace=wspace, hspace=hspace)

    def get_topmost_subplotspec(self):
        """
        Return the topmost `.SubplotSpec` instance associated with the subplot.
        """
        return self._subplot_spec.get_topmost_subplotspec()


class SubplotSpec:
    """
    Specifies the location of a subplot in a `GridSpec`.

    .. note::

        Likely, you'll never instantiate a `SubplotSpec` yourself. Instead you
        will typically obtain one from a `GridSpec` using item-access.

    Parameters
    ----------
    gridspec : `~matplotlib.gridspec.GridSpec`
        The GridSpec, which the subplot is referencing.
    num1, num2 : int
        The subplot will occupy the num1-th cell of the given
        gridspec.  If num2 is provided, the subplot will span between
        num1-th cell and num2-th cell *inclusive*.

        The index starts from 0.
    """
    def __init__(self, gridspec, num1, num2=None):
        self._gridspec = gridspec
        self.num1 = num1
        self.num2 = num2

    def __repr__(self):
        return (f"{self.get_gridspec()}["
                f"{self.rowspan.start}:{self.rowspan.stop}, "
                f"{self.colspan.start}:{self.colspan.stop}]")

    @staticmethod
    def _from_subplot_args(figure, args):
        """
        Construct a `.SubplotSpec` from a parent `.Figure` and either

        - a `.SubplotSpec` -- returned as is;
        - one or three numbers -- a MATLAB-style subplot specifier.
        """
        message = ("Passing non-integers as three-element position "
                   "specification is deprecated since %(since)s and will be "
                   "removed %(removal)s.")
        if len(args) == 1:
            arg, = args
            if isinstance(arg, SubplotSpec):
                return arg
            else:
                if not isinstance(arg, Integral):
                    _api.warn_deprecated("3.3", message=message)
                    arg = str(arg)
                try:
                    rows, cols, num = map(int, str(arg))
                except ValueError:
                    raise ValueError(
                        f"Single argument to subplot must be a three-digit "
                        f"integer, not {arg}") from None
                i = j = num
        elif len(args) == 3:
            rows, cols, num = args
            if not (isinstance(rows, Integral) and isinstance(cols, Integral)):
                _api.warn_deprecated("3.3", message=message)
                rows, cols = map(int, [rows, cols])
            gs = GridSpec(rows, cols, figure=figure)
            if isinstance(num, tuple) and len(num) == 2:
                if not all(isinstance(n, Integral) for n in num):
                    _api.warn_deprecated("3.3", message=message)
                    i, j = map(int, num)
                else:
                    i, j = num
            else:
                if not isinstance(num, Integral):
                    _api.warn_deprecated("3.3", message=message)
                    num = int(num)
                if num < 1 or num > rows*cols:
                    raise ValueError(
                        f"num must be 1 <= num <= {rows*cols}, not {num}")
                i = j = num
        else:
            raise TypeError(f"subplot() takes 1 or 3 positional arguments but "
                            f"{len(args)} were given")

        gs = GridSpec._check_gridspec_exists(figure, rows, cols)
        if gs is None:
            gs = GridSpec(rows, cols, figure=figure)
        return gs[i-1:j]

    # num2 is a property only to handle the case where it is None and someone
    # mutates num1.

    @property
    def num2(self):
        return self.num1 if self._num2 is None else self._num2

    @num2.setter
    def num2(self, value):
        self._num2 = value

    def __getstate__(self):
        return {**self.__dict__}

    def get_gridspec(self):
        return self._gridspec

    def get_geometry(self):
        """
        Return the subplot geometry as tuple ``(n_rows, n_cols, start, stop)``.

        The indices *start* and *stop* define the range of the subplot within
        the `GridSpec`. *stop* is inclusive (i.e. for a single cell
        ``start == stop``).
        """
        rows, cols = self.get_gridspec().get_geometry()
        return rows, cols, self.num1, self.num2

    @_api.deprecated("3.3", alternative="rowspan, colspan")
    def get_rows_columns(self):
        """
        Return the subplot row and column numbers as a tuple
        ``(n_rows, n_cols, row_start, row_stop, col_start, col_stop)``.
        """
        gridspec = self.get_gridspec()
        nrows, ncols = gridspec.get_geometry()
        row_start, col_start = divmod(self.num1, ncols)
        row_stop, col_stop = divmod(self.num2, ncols)
        return nrows, ncols, row_start, row_stop, col_start, col_stop

    @property
    def rowspan(self):
        """The rows spanned by this subplot, as a `range` object."""
        ncols = self.get_gridspec().ncols
        return range(self.num1 // ncols, self.num2 // ncols + 1)

    @property
    def colspan(self):
        """The columns spanned by this subplot, as a `range` object."""
        ncols = self.get_gridspec().ncols
        # We explicitly support num2 referring to a column on num1's *left*, so
        # we must sort the column indices here so that the range makes sense.
        c1, c2 = sorted([self.num1 % ncols, self.num2 % ncols])
        return range(c1, c2 + 1)

    def is_first_row(self):
        return self.rowspan.start == 0

    def is_last_row(self):
        return self.rowspan.stop == self.get_gridspec().nrows

    def is_first_col(self):
        return self.colspan.start == 0

    def is_last_col(self):
        return self.colspan.stop == self.get_gridspec().ncols

    @_api.delete_parameter("3.4", "return_all")
    def get_position(self, figure, return_all=False):
        """
        Update the subplot position from ``figure.subplotpars``.
        """
        gridspec = self.get_gridspec()
        nrows, ncols = gridspec.get_geometry()
        rows, cols = np.unravel_index([self.num1, self.num2], (nrows, ncols))
        fig_bottoms, fig_tops, fig_lefts, fig_rights = \
            gridspec.get_grid_positions(figure)

        fig_bottom = fig_bottoms[rows].min()
        fig_top = fig_tops[rows].max()
        fig_left = fig_lefts[cols].min()
        fig_right = fig_rights[cols].max()
        figbox = Bbox.from_extents(fig_left, fig_bottom, fig_right, fig_top)

        if return_all:
            return figbox, rows[0], cols[0], nrows, ncols
        else:
            return figbox

    def get_topmost_subplotspec(self):
        """
        Return the topmost `SubplotSpec` instance associated with the subplot.
        """
        gridspec = self.get_gridspec()
        if hasattr(gridspec, "get_topmost_subplotspec"):
            return gridspec.get_topmost_subplotspec()
        else:
            return self

    def __eq__(self, other):
        """
        Two SubplotSpecs are considered equal if they refer to the same
        position(s) in the same `GridSpec`.
        """
        # other may not even have the attributes we are checking.
        return ((self._gridspec, self.num1, self.num2)
                == (getattr(other, "_gridspec", object()),
                    getattr(other, "num1", object()),
                    getattr(other, "num2", object())))

    def __hash__(self):
        return hash((self._gridspec, self.num1, self.num2))

    def subgridspec(self, nrows, ncols, **kwargs):
        """
        Create a GridSpec within this subplot.

        The created `.GridSpecFromSubplotSpec` will have this `SubplotSpec` as
        a parent.

        Parameters
        ----------
        nrows : int
            Number of rows in grid.

        ncols : int
            Number or columns in grid.

        Returns
        -------
        `.GridSpecFromSubplotSpec`

        Other Parameters
        ----------------
        **kwargs
            All other parameters are passed to `.GridSpecFromSubplotSpec`.

        See Also
        --------
        matplotlib.pyplot.subplots

        Examples
        --------
        Adding three subplots in the space occupied by a single subplot::

            fig = plt.figure()
            gs0 = fig.add_gridspec(3, 1)
            ax1 = fig.add_subplot(gs0[0])
            ax2 = fig.add_subplot(gs0[1])
            gssub = gs0[2].subgridspec(1, 3)
            for i in range(3):
                fig.add_subplot(gssub[0, i])
        """
        return GridSpecFromSubplotSpec(nrows, ncols, self, **kwargs)
