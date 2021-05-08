# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/forecast.ipynb (unless otherwise specified).

__all__ = ['Forecast']

# Cell
from typing import Callable, Dict, Generator

import pandas as pd

from .core import predictions_flow, preprocessing_flow
from .utils import backtest_splits


# Cell
class Forecast:
    """Full pipeline encapsulation.

    Takes a model (scikit-learn compatible regressor) and a flow configuration
    and runs all the forecasting pipeline."""

    def __init__(self, model, flow_config: Dict):
        self.model = model
        self.flow_config = flow_config

    def __repr__(self):
        return f'Forecast(model={self.model}, flow_config={self.flow_config})'

    def preprocess(self,
                   data: pd.DataFrame,
                   prep_fn: Callable = preprocessing_flow) -> pd.DataFrame:
        """Calls `prep_fn(data, **self.flow_config)`, saves the resulting `TimeSeries` object
        for the forecasting step and returns the `data` with the features added."""
        self.ts, series_df = prep_fn(data, **self.flow_config)
        return series_df

    def fit(self,
            data: pd.DataFrame,
            prep_fn: Callable = preprocessing_flow,
            **fit_kwargs) -> 'Forecast':
        """Preprocesses `data` and fits `model` to it."""
        series_df = self.preprocess(data, prep_fn)
        X, y = series_df.drop(columns=['ds', 'y']), series_df.y.values
        del series_df
        self.model.fit(X, y, **fit_kwargs)
        return self

    def predict(self,
                horizon: int,
                predict_fn: Callable = predictions_flow,
                **predict_fn_kwargs) -> pd.DataFrame:
        """Compute the predictions for the next `horizon` steps."""
        return predict_fn(self.ts, self.model, horizon, **predict_fn_kwargs)

    def backtest(self,
                 data,
                 n_windows: int,
                 window_size: int,
                 predict_fn: Callable = predictions_flow,
                 **predict_fn_kwargs) -> Generator[pd.DataFrame, None, None]:
        """Creates `n_windows` splits of `window_size` from `data`, trains the model
        on the training set, predicts the window and merges the actuals and the predictions
        in a dataframe.

        Returns a generator to the dataframes containing the datestamps, actual values
        and predictions."""
        for train, valid in backtest_splits(data, n_windows, window_size):
            self.fit(train)
            y_pred = self.predict(window_size, predict_fn, **predict_fn_kwargs)
            y_valid = valid[['ds', 'y']]
            result = y_valid.merge(y_pred, on=['unique_id', 'ds'], how='left')
            yield result