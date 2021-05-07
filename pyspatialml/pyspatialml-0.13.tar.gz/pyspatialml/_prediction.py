import numpy as np


def predict_output(img, estimator):
    """Prediction function for classification or regression response.

    Parameters
    ----
    img : tuple (window, numpy.ndarray)
        A window object, and a 3d ndarray of raster data with the dimensions in
        order of (band, rows, columns).

    estimator : estimator object implementing 'fit'
        The object to use to fit the data.

    Returns
    -------
    numpy.ndarray
        2d numpy array representing a single band raster containing the
        classification or regression result.
    """
    window, img = img

    # reorder into rows, cols, bands(transpose)
    n_features, rows, cols = img.shape[0], img.shape[1], img.shape[2]

    # reshape into 2D array (rows=sample_n, cols=band_values)
    n_samples = rows * cols
    flat_pixels = img.transpose(1, 2, 0).reshape((n_samples, n_features))

    # create mask for NaN values and replace with number
    flat_pixels_mask = flat_pixels.mask.copy()
    flat_pixels = flat_pixels.filled(0)

    # predict and replace mask
    result_cla = estimator.predict(flat_pixels)
    result_cla = np.ma.masked_array(
        data=result_cla, mask=flat_pixels_mask.any(axis=1)
    )

    # reshape the prediction from a 1D into 3D array [band, row, col]
    result_cla = result_cla.reshape((1, window.height, window.width))

    return result_cla


def predict_prob(img, estimator):
    """Class probabilities function.

    Parameters
    ----------
    img : tuple (window, numpy.ndarray)
        A window object, and a 3d ndarray of raster data with the dimensions in
        order of (band, rows, columns).

    estimator : estimator object implementing 'fit'
        The object to use to fit the data.

    Returns
    -------
    numpy.ndarray
        Multi band raster as a 3d numpy array containing the probabilities
        associated with each class. ndarray dimensions are in the order of
        (class, row, column).
    """
    window, img = img

    # reorder into rows, cols, bands (transpose)
    n_features, rows, cols = img.shape[0], img.shape[1], img.shape[2]
    mask2d = img.mask.any(axis=0)

    # then resample into 2D array (rows=sample_n, cols=band_values)
    n_samples = rows * cols
    flat_pixels = img.transpose(1, 2, 0).reshape((n_samples, n_features))
    flat_pixels = flat_pixels.filled(0)

    # predict probabilities
    result_proba = estimator.predict_proba(flat_pixels)

    # reshape class probabilities back to 3D array [class, rows, cols]
    result_proba = result_proba.reshape(
        (window.height, window.width, result_proba.shape[1])
    )

    # reshape band into rasterio format [band, row, col]
    result_proba = result_proba.transpose(2, 0, 1)

    # repeat mask for n_bands
    mask3d = np.repeat(
        a=mask2d[np.newaxis, :, :],
        repeats=result_proba.shape[0],
        axis=0
    )

    # convert proba to masked array
    result_proba = np.ma.masked_array(
        result_proba,
        mask=mask3d,
        fill_value=np.nan
    )

    return result_proba


def predict_multioutput(img, estimator):
    """Multi-target prediction function.

    Parameters
    ----------
    img : tuple (window, numpy.ndarray)
        A window object, and a 3d ndarray of raster data with the dimensions in
        order of (band, rows, columns).

    estimator : estimator object implementing 'fit'
        The object to use to fit the data.

    Returns
    -------
    numpy.ndarray
        3d numpy array representing the multi-target prediction result with the
        dimensions in the order of (target, row, column).
    """
    window, img = img

    # reorder into rows, cols, bands(transpose)
    n_features, rows, cols = img.shape[0], img.shape[1], img.shape[2]
    mask2d = img.mask.any(axis=0)

    # reshape into 2D array (rows=sample_n, cols=band_values)
    n_samples = rows * cols
    flat_pixels = img.transpose(1, 2, 0).reshape((n_samples, n_features))
    flat_pixels = flat_pixels.filled(0)

    # predict probabilities
    result = estimator.predict(flat_pixels)

    # reshape class probabilities back to 3D array [class, rows, cols]
    result = result.reshape((window.height, window.width, result.shape[1]))

    # reshape band into rasterio format [band, row, col]
    result = result.transpose(2, 0, 1)

    # repeat mask for n_bands
    mask3d = np.repeat(
        a=mask2d[np.newaxis, :, :],
        repeats=result.shape[0],
        axis=0
    )

    # convert proba to masked array
    result = np.ma.masked_array(result, mask=mask3d, fill_value=np.nan)

    return result
