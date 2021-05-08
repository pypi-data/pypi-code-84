from functools import partial

import numpy as np
from scipy.special import binom


def fdiff_coef(d, window) -> np.array:
    """
    Returns sequence of coefficients in fracdiff operator.

    Parameters
    ----------
    d : float
        Order of differentiation.
    window : int
        Number of terms.

    Returns
    -------
    coef : numpy.array, shape (window,)
        Coefficients in fracdiff operator.

    Examples
    --------
    >>> fdiff_coef(1.0, 4)
    array([ 1., -1.,  0., -0.])
    >>> fdiff_coef(1.5, 4)
    array([ 1.    , -1.5   ,  0.375 ,  0.0625])
    >>> fdiff_coef(0.5, 4)
    array([ 1.    , -0.5   , -0.125 , -0.0625])
    """
    s = np.tile([1.0, -1.0], -(-window // 2))[:window]
    return s * binom(d, np.arange(window))


def fdiff(
    a, n=1.0, axis=-1, prepend=np._NoValue, append=np._NoValue, window=10, mode="full"
) -> np.array:
    """
    Calculate the `n`-th differentiation along the given axis.

    Extention of ``numpy.diff`` to fractional differentiation.

    Parameters
    ----------
    a : array_like
        Input array.
    n : float, default=1.0
        The order of differentiation.
        For integer `n`, it returns the same output with ``numpy.diff``.
    axis : int, default=-1
        The axis along which the difference is taken, default is the last axis.
    prepend, append : array_like, optional
        Values to prepend or append to `a` along axis prior to performing
        the difference.
        Scalar values are expanded to arrays with length 1 in the direction of axis and
        the shape of the input array in along all other axes.
        Otherwise the dimension and shape must match `a` except along axis.
    window : int, default=10
        Number of observations to compute each element in the output.
    mode : {"full", "valid"}, default="full"
        "full" (default) :
            Return elements where at least one coefficient is used.
            Output size along `axis` is `M` where `M` is the length of `a`
            (plus the lengths of append and prepend if these are given).
            At the beginning of a time-series, boundary effects may be seen.
        "valid" :
            Return elements where all coefficients are used.
            Output size along `axis` is `M - window` where `M` is the length of
            `a` (plus the lengths of append and prepend if these are given).
            At the beginning of a time-series, boundary effects is not seen.

    Returns
    -------
    fdiff : numpy.array
        The fractional differentiation.
        The shape of the output is the same as `a` except along `axis`.
        The dimension is `a.shape[axis] - window + d1 + d2` with
        `d1` and `d2` being the dimension of ``prepend`` and ``append``, respectively.

    Examples
    --------
    This returns the same result with ``numpy.diff`` for integer `n`.

    >>> a = np.array([1, 2, 4, 7, 0])
    >>> (np.diff(a) == fdiff(a)).all()
    True
    >>> (np.diff(a, 2) == fdiff(a, 2)).all()
    True

    This returns fractional differentiation for noninteger `n`.

    >>> fdiff(a, 0.5, window=3)
    array([ 1.   ,  1.5  ,  2.875,  4.75 , -4.   ])

    Mode "valid" returns elements for which all coefficients are convoluted.

    >>> fdiff(a, 0.5, window=3, mode="valid")
    array([ 2.875,  4.75 , -4.   ])
    >>> fdiff(a, 0.5, window=3, mode="valid", prepend=[1, 1])
    array([ 0.375,  1.375,  2.875,  4.75 , -4.   ])

    Differentiation along desired axis.

    >>> a = np.array([[  1,  3,  6, 10, 15],
    ...               [  0,  5,  6,  8, 11]])
    >>> fdiff(a, 0.5, window=3)
    array([[1.   , 2.5  , 4.375, 6.625, 9.25 ],
           [0.   , 5.   , 3.5  , 4.375, 6.25 ]])
    >>> fdiff(a, 0.5, window=3, axis=0)
    array([[ 1. ,  3. ,  6. , 10. , 15. ],
           [-0.5,  3.5,  3. ,  3. ,  3.5]])
    """
    # Return `np.diff(...)` if n is integer
    if isinstance(n, int) or n.is_integer():
        return np.diff(a, n=int(n), axis=axis, prepend=prepend, append=append)

    # if n < 0:
    #     raise ValueError("order must be non-negative but got {}".format(n))
    if a.ndim == 0:
        raise ValueError("diff requires input that is at least one dimensional")

    a = np.asanyarray(a)
    axis = np.core.multiarray.normalize_axis_index(axis, a.ndim)
    dtype = a.dtype if np.issubdtype(a.dtype, np.floating) else np.float64

    combined = []
    if prepend is not np._NoValue:
        prepend = np.asanyarray(prepend)
        if prepend.ndim == 0:
            shape = list(a.shape)
            shape[axis] = 1
            prepend = np.broadcast_to(prepend, tuple(shape))
        combined.append(prepend)

    combined.append(a)

    if append is not np._NoValue:
        append = np.asanyarray(append)
        if append.ndim == 0:
            shape = list(a.shape)
            shape[axis] = 1
            append = np.broadcast_to(append, tuple(shape))
        combined.append(append)

    if len(combined) > 1:
        a = np.concatenate(combined, axis)

    if mode == "valid":
        D = partial(np.convolve, fdiff_coef(n, window).astype(dtype), mode="valid")
        a = np.apply_along_axis(D, axis, a)
    elif mode == "full":
        D = partial(np.convolve, fdiff_coef(n, window).astype(dtype), mode="full")
        s = tuple(
            slice(a.shape[axis]) if i == axis else slice(None) for i in range(a.ndim)
        )
        a = np.apply_along_axis(D, axis, a)
        a = a[s]
    else:
        raise ValueError("Invalid mode: {}".format(mode))

    return a
