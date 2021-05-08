# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/cli.ipynb (unless otherwise specified).

__all__ = ['run_forecast']

# Cell
from pathlib import Path

import pandas as pd
import typer

from .api import (S3Path, _is_s3_path, _path_as_str, fcst_from_config,
                  parse_config, perform_backtest, read_data, setup_client)

# Internal Cell
app = typer.Typer()

# Cell
@app.command()
def run_forecast(config_file: str):
    """Run the forecasting pipeline using the configuration defined in `config_file`."""
    config = parse_config(config_file)
    is_distributed = config.distributed is not None
    if config.distributed is not None:  # mypy
        client = setup_client(config.distributed.cluster)
    try:
        data = read_data(config.data, is_distributed)
        prefix = config.data.prefix
        path = S3Path.from_uri(prefix) if _is_s3_path(prefix) else Path(prefix)
        output_path = path/config.data.output
        output_path.mkdir(exist_ok=True)

        fcst = fcst_from_config(config)
        if config.backtest is not None:
            perform_backtest(fcst, data, config, output_path)
        if config.forecast is not None:
            fcst.fit(data)
            preds = fcst.predict(config.forecast.horizon)
            writer = getattr(preds, f'to_{config.data.format}')
            write_path = _path_as_str(output_path/'forecast')
            if isinstance(data, pd.DataFrame):
                write_path += f'.{config.data.format}'
            writer(write_path)
    except Exception as e:
        raise e
    finally:
        if is_distributed:
            client.cluster.close()
            client.close()