"""OpenGL Utilities.
"""
from contextlib import contextmanager
from functools import lru_cache
from typing import Tuple

import numpy as np
from vispy.app import Canvas
from vispy.gloo import gl
from vispy.gloo.context import get_current_canvas

from ..utils.translations import trans

texture_dtypes = [
    np.dtype(np.int8),
    np.dtype(np.uint8),
    np.dtype(np.int16),
    np.dtype(np.uint16),
    np.dtype(np.float32),
]


@contextmanager
def _opengl_context():
    """Assure we are running with a valid OpenGL context.

    Only create a Canvas is one doesn't exist. Creating and closing a
    Canvas causes vispy to process Qt events which can cause problems.
    Ideally call opengl_context() on start after creating your first
    Canvas. However it will work either way.
    """
    canvas = Canvas(show=False) if get_current_canvas() is None else None
    try:
        yield
    finally:
        if canvas is not None:
            canvas.close()


@lru_cache()
def get_max_texture_sizes() -> Tuple[int, int]:
    """Return the maximum texture sizes for 2D and 3D rendering.

    If this function is called without an OpenGL context it will create a
    temporary non-visible Canvas. Either way the lru_cache means subsequent
    calls to thing function will return the original values without
    actually running again.

    Returns
    -------
    Tuple[int, int]
        The max textures sizes for (2d, 3d) rendering.
    """
    with _opengl_context():
        max_size_2d = gl.glGetParameter(gl.GL_MAX_TEXTURE_SIZE)

    if max_size_2d == ():
        max_size_2d = None

    # vispy doesn't expose GL_MAX_3D_TEXTURE_SIZE so hard coding for now.
    # MAX_TEXTURE_SIZE_3D = gl.glGetParameter(gl.GL_MAX_3D_TEXTURE_SIZE)
    # if MAX_TEXTURE_SIZE_3D == ():
    #    MAX_TEXTURE_SIZE_3D = None
    max_size_3d = 2048

    return max_size_2d, max_size_3d


def fix_data_dtype(data):
    """Makes sure the dtype of the data is accetpable to vispy.

    Acceptable types are int8, uint8, int16, uint16, float32, float64.

    Parameters
    ----------
    data : np.ndarray
        Data that will need to be of right type.

    Returns
    -------
    np.ndarray
        Data that is of right type and will be passed to vispy.
    """

    dtype = np.dtype(data.dtype)
    if dtype in texture_dtypes:
        return data
    else:
        try:
            dtype = dict(i=np.int16, f=np.float32, u=np.uint16, b=np.uint8)[
                dtype.kind
            ]
        except KeyError:  # not an int or float
            raise TypeError(
                trans._(
                    'type {dtype} not allowed for texture; must be one of {textures}',  # noqa: E501
                    deferred=True,
                    dtype=dtype,
                    textures=set(texture_dtypes),
                )
            )
        return data.astype(dtype)
