import numpy as np
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QCheckBox, QComboBox, QLabel, QSlider

from ...utils.colormaps import AVAILABLE_COLORMAPS
from ...utils.translations import trans
from ..utils import qt_signals_blocked
from .qt_layer_controls_base import QtLayerControls

MAX_TAIL_LENGTH = 300
MAX_TAIL_WIDTH = 40


class QtTracksControls(QtLayerControls):
    """Qt view and controls for the Tracks layer.

    Parameters
    ----------
    layer : napari.layers.Tracks
        An instance of a Tracks layer.

    Attributes
    ----------
    grid_layout : qtpy.QtWidgets.QGridLayout
        Layout of Qt widget controls for the layer.
    layer : layers.Tracks
        An instance of a Tracks layer.

    """

    def __init__(self, layer):
        super().__init__(layer)

        # NOTE(arl): there are no events fired for changing checkboxes
        self.layer.events.tail_width.connect(self._on_tail_width_change)
        self.layer.events.tail_length.connect(self._on_tail_length_change)
        self.layer.events.properties.connect(self._on_properties_change)
        self.layer.events.colormap.connect(self._on_colormap_change)
        self.layer.events.color_by.connect(self._on_color_by_change)

        # combo box for track coloring, we can get these from the properties
        # keys
        self.color_by_combobox = QComboBox()
        self.color_by_combobox.addItems(self.layer.properties_to_color_by)

        self.colormap_combobox = QComboBox()
        for name, colormap in AVAILABLE_COLORMAPS.items():
            display_name = colormap._display_name
            self.colormap_combobox.addItem(display_name, name)

        # slider for track tail length
        self.tail_length_slider = QSlider(Qt.Horizontal)
        self.tail_length_slider.setFocusPolicy(Qt.NoFocus)
        self.tail_length_slider.setMinimum(1)
        self.tail_length_slider.setMaximum(MAX_TAIL_LENGTH)
        self.tail_length_slider.setSingleStep(1)

        # slider for track edge width
        self.tail_width_slider = QSlider(Qt.Horizontal)
        self.tail_width_slider.setFocusPolicy(Qt.NoFocus)
        self.tail_width_slider.setMinimum(1)
        self.tail_width_slider.setMaximum(MAX_TAIL_WIDTH)
        self.tail_width_slider.setSingleStep(1)

        # checkboxes for display
        self.id_checkbox = QCheckBox()
        self.tail_checkbox = QCheckBox()
        self.tail_checkbox.setChecked(True)
        self.graph_checkbox = QCheckBox()
        self.graph_checkbox.setChecked(True)

        self.tail_width_slider.valueChanged.connect(self.change_tail_width)
        self.tail_length_slider.valueChanged.connect(self.change_tail_length)
        self.tail_checkbox.stateChanged.connect(self.change_display_tail)
        self.id_checkbox.stateChanged.connect(self.change_display_id)
        self.graph_checkbox.stateChanged.connect(self.change_display_graph)
        self.color_by_combobox.currentTextChanged.connect(self.change_color_by)
        self.colormap_combobox.currentTextChanged.connect(self.change_colormap)

        # grid_layout created in QtLayerControls
        # addWidget(widget, row, column, [row_span, column_span])

        self.grid_layout.addWidget(QLabel(trans._('color by:')), 0, 0)
        self.grid_layout.addWidget(self.color_by_combobox, 0, 1)
        self.grid_layout.addWidget(QLabel(trans._('colormap:')), 1, 0)
        self.grid_layout.addWidget(self.colormap_combobox, 1, 1)
        self.grid_layout.addWidget(QLabel(trans._('blending:')), 2, 0)
        self.grid_layout.addWidget(self.blendComboBox, 2, 1)
        self.grid_layout.addWidget(QLabel(trans._('opacity:')), 3, 0)
        self.grid_layout.addWidget(self.opacitySlider, 3, 1)
        self.grid_layout.addWidget(QLabel(trans._('tail width:')), 4, 0)
        self.grid_layout.addWidget(self.tail_width_slider, 4, 1)
        self.grid_layout.addWidget(QLabel(trans._('tail length:')), 5, 0)
        self.grid_layout.addWidget(self.tail_length_slider, 5, 1)
        self.grid_layout.addWidget(QLabel(trans._('tail:')), 6, 0)
        self.grid_layout.addWidget(self.tail_checkbox, 6, 1)
        self.grid_layout.addWidget(QLabel(trans._('show ID:')), 7, 0)
        self.grid_layout.addWidget(self.id_checkbox, 7, 1)
        self.grid_layout.addWidget(QLabel(trans._('graph:')), 8, 0)
        self.grid_layout.addWidget(self.graph_checkbox, 8, 1)
        self.grid_layout.setRowStretch(9, 1)
        self.grid_layout.setColumnStretch(1, 1)
        self.grid_layout.setSpacing(4)

        self._on_tail_length_change()
        self._on_tail_width_change()
        self._on_colormap_change()
        self._on_color_by_change()

    def _on_tail_width_change(self, event=None):
        """Receive layer model track line width change event and update slider.

        Parameters
        ----------
        event : qtpy.QtCore.QEvent, optional.
            Event from the Qt context, by default None.
        """
        with self.layer.events.tail_width.blocker():
            value = self.layer.tail_width
            value = np.clip(int(2 * value), 1, MAX_TAIL_WIDTH)
            self.tail_width_slider.setValue(value)

    def _on_tail_length_change(self, event=None):
        """Receive layer model track line width change event and update slider.

        Parameters
        ----------
        event : qtpy.QtCore.QEvent, optional.
            Event from the Qt context, by default None.
        """
        with self.layer.events.tail_length.blocker():
            value = self.layer.tail_length
            value = np.clip(value, 1, MAX_TAIL_LENGTH)
            self.tail_length_slider.setValue(value)

    def _on_properties_change(self, event=None):
        """Change the properties that can be used to color the tracks."""
        with self.layer.events.properties.blocker():

            with qt_signals_blocked(self.color_by_combobox):
                self.color_by_combobox.clear()
            self.color_by_combobox.addItems(self.layer.properties_to_color_by)

    def _on_colormap_change(self, event=None):
        """Receive layer model colormap change event and update combobox.

        Parameters
        ----------
        event : qtpy.QtCore.QEvent, optional.
            Event from the Qt context, by default None.
        """
        with self.layer.events.colormap.blocker():
            self.colormap_combobox.setCurrentIndex(
                self.colormap_combobox.findData(self.layer.colormap)
            )

    def _on_color_by_change(self, event=None):
        """Receive layer model color_by change event and update combobox.

        Parameters
        ----------
        event : qtpy.QtCore.QEvent, optional.
            Event from the Qt context, by default None.
        """
        with self.layer.events.color_by.blocker():
            color_by = self.layer.color_by

            idx = self.color_by_combobox.findText(
                color_by, Qt.MatchFixedString
            )
            self.color_by_combobox.setCurrentIndex(idx)

    def change_tail_width(self, value):
        """Change track line width of shapes on the layer model.

        Parameters
        ----------
        value : float
            Line width of track tails.
        """
        self.layer.tail_width = float(value) / 2.0

    def change_tail_length(self, value):
        """Change edge line width of shapes on the layer model.

        Parameters
        ----------
        value : int
            Line length of track tails.
        """
        self.layer.tail_length = value

    def change_display_tail(self, state):
        self.layer.display_tail = self.tail_checkbox.isChecked()

    def change_display_id(self, state):
        self.layer.display_id = self.id_checkbox.isChecked()

    def change_display_graph(self, state):
        self.layer.display_graph = self.graph_checkbox.isChecked()

    def change_color_by(self, value: str):
        self.layer.color_by = value

    def change_colormap(self, colormap: str):
        self.layer.colormap = self.colormap_combobox.currentData()
