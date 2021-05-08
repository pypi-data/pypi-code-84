"""Class implementation for line style related interface.

See Also
--------
- graphics_clear_interface
"""

from typing import Dict
from typing import Optional
from typing import TypeVar
from typing import Union

from apysc import Int
from apysc import Number
from apysc import String
from apysc.display.line_caps import LineCaps
from apysc.type.revert_interface import RevertInterface

StrOrString = TypeVar('StrOrString', str, String)


class LineStyleInterface(RevertInterface):

    _line_color: String
    _line_thickness: Int
    _line_alpha: Number
    _line_cap: String

    def line_style(
            self, color: StrOrString,
            thickness: Union[int, Int] = 1,
            alpha: Union[float, Number] = 1.0,
            cap: Optional[LineCaps] = None) -> None:
        """
        Set line style values.

        Parameters
        ----------
        color : str or String
            Hexadecimal color string. e.g., '#00aaff'
        thickness : int or Int, default 1
            Line thickness (minimum value is 1).
        alpha : float or Number, default 1.0
            Line color opacity (0.0 to 1.0).
        cap : LineCaps or None, default None
            Line cap (edge style) setting. This will be ignored by not
            line-related graphics (e.g., Rectangle will ignore this,
            conversely used by Polyline).
        """
        from apysc.color import color_util
        from apysc.converter import cast
        from apysc.type.number_value_interface import NumberValueInterface
        from apysc.validation import color_validation
        from apysc.validation import number_validation

        self._initialize_line_color_if_not_initialized()
        self._initialize_line_thickness_if_not_initialized()
        self._initialize_line_alpha_if_not_initialized()

        color = color_util.complement_hex_color(
            hex_color_code=color)
        self._line_color.value = color
        number_validation.validate_integer(integer=thickness)
        number_validation.validate_num_is_gt_zero(num=thickness)
        self._line_thickness = Int(thickness)
        number_validation.validate_num(num=alpha)
        if not isinstance(alpha, NumberValueInterface):
            alpha = cast.to_float_from_int(int_or_float=alpha)
            alpha = Number(alpha)
        color_validation.validate_alpha_range(alpha=alpha)
        self._line_alpha = alpha
        self._set_line_cap(cap=cap)

    def _set_line_cap(self, cap: Optional[LineCaps]) -> None:
        """
        Set line cap setting to attribute.

        Parameters
        ----------
        cap : LineCaps or None, default None
            Line cap (edge style) setting.
        """
        from apysc.validation.display_validation import validate_line_cap
        if cap is None:
            cap = LineCaps.BUTT
        validate_line_cap(cap=cap)
        self._line_cap = String(cap.value)

    def _initialize_line_color_if_not_initialized(self) -> None:
        """
        Initialize _line_color attribute it it is not
        initialized yet.
        """
        if hasattr(self, '_line_color'):
            return
        self._line_color = String('')

    def _initialize_line_thickness_if_not_initialized(self) -> None:
        """
        Initialize _line_thickness attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_thickness'):
            return
        self._line_thickness = Int(1)

    def _initialize_line_alpha_if_not_initialized(self) -> None:
        """
        Initialize _line_alpha attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_alpha'):
            return
        self._line_alpha = Number(1.0)

    def _initialize_line_cap_if_not_initialized(self) -> None:
        """
        Initialize _line_cap attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_cap'):
            return
        self._line_cap = String(LineCaps.BUTT.value)

    @property
    def line_color(self) -> String:
        """
        Get current line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.
        """
        from apysc.type import value_util
        self._initialize_line_color_if_not_initialized()
        return value_util.get_copy(value=self._line_color)

    @property
    def line_thickness(self) -> Int:
        """
        Get current line thickness.

        Returns
        -------
        line_thickness : Int
            Current line thickness.
        """
        from apysc.type import value_util
        self._initialize_line_thickness_if_not_initialized()
        return value_util.get_copy(value=self._line_thickness)

    @property
    def line_alpha(self) -> Number:
        """
        Get current line color opacity.

        Returns
        -------
        line_alpha : Number
            Current line opacity (0.0 to 1.0).
            If not be set, None will be returned.
        """
        from apysc.type import value_util
        self._initialize_line_alpha_if_not_initialized()
        return value_util.get_copy(value=self._line_alpha)

    @property
    def line_cap(self) -> String:
        """
        Get current line cap (edge) style setting.

        Returns
        -------
        line_cap : String
            Current line cap (edge) style setting.
        """
        self._initialize_line_cap_if_not_initialized()
        return self._line_cap

    _line_color_snapshots: Dict[str, str]
    _line_thickness_snapshots: Dict[str, int]
    _line_alpha_snapshots: Dict[str, float]
    _line_cap_snapshots: Dict[str, str]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_line_color_snapshots'):
            self._line_color_snapshots = {}
            self._line_thickness_snapshots = {}
            self._line_alpha_snapshots = {}
            self._line_cap_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_line_color_if_not_initialized()
        self._initialize_line_thickness_if_not_initialized()
        self._initialize_line_alpha_if_not_initialized()
        self._initialize_line_cap_if_not_initialized()
        self._line_color_snapshots[snapshot_name] = self._line_color._value
        self._line_thickness_snapshots[snapshot_name] = \
            int(self._line_thickness._value)
        self._line_alpha_snapshots[snapshot_name] = self._line_alpha._value
        self._line_cap_snapshots[snapshot_name] = self._line_cap._value

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._line_color._value = self._line_color_snapshots[snapshot_name]
        self._line_thickness._value = self._line_thickness_snapshots[
            snapshot_name]
        self._line_alpha._value = self._line_alpha_snapshots[snapshot_name]
        self._line_cap._value = self._line_cap_snapshots[snapshot_name]
