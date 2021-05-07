import json
import os
import pickle
from contextlib import contextmanager
from typing import IO, Any, BinaryIO, Iterator, TextIO, Union

import numpy as np
import scipy.io
import toml
import torch
import yaml

from . import fs

__all__ = [
    'load', 'save', 'load_json', 'save_json', 'load_jsonl', 'save_jsonl',
    'load_mat', 'save_mat', 'load_npy', 'save_npy', 'load_npz', 'save_npz',
    'load_pt', 'save_pt', 'load_taml', 'save_taml', 'load_yaml', 'save_yaml'
]


@contextmanager
def file_descriptor(f: Union[str, IO], mode: str = 'r') -> Iterator[IO]:
    opened = False
    try:
        if isinstance(f, str):
            f = open(f, mode)
            opened = True
        yield f
    finally:
        if opened:
            f.close()


def load_json(f: Union[str, TextIO], **kwargs) -> Any:
    with file_descriptor(f, mode='r') as fd:
        return json.load(fd, **kwargs)


def save_json(f: Union[str, TextIO], obj: Any, **kwargs) -> None:
    with file_descriptor(f, mode='w') as fd:
        json.dump(obj, fd, **kwargs)


def load_jsonl(f: Union[str, TextIO], **kwargs) -> Any:
    with file_descriptor(f, mode='r') as fd:
        return [json.loads(datum, **kwargs) for datum in fd.readlines()]


def save_jsonl(f: Union[str, TextIO], obj: Any, **kwargs) -> None:
    with file_descriptor(f, mode='w') as fd:
        fd.write('\n'.join(json.dumps(datum, **kwargs) for datum in obj))


def load_mat(f: Union[str, BinaryIO], **kwargs) -> Any:
    return scipy.io.loadmat(f, **kwargs)


def save_mat(f: Union[str, BinaryIO], obj: Any, **kwargs) -> None:
    scipy.io.savemat(f, obj, **kwargs)


def load_npy(f: Union[str, BinaryIO], **kwargs) -> Any:
    return np.load(f, **kwargs)


def save_npy(f: Union[str, BinaryIO], obj: Any, **kwargs) -> None:
    np.save(f, obj, **kwargs)


def load_npz(f: Union[str, BinaryIO], **kwargs) -> Any:
    return np.load(f, **kwargs)


def save_npz(f: Union[str, BinaryIO], obj: Any, **kwargs) -> None:
    np.savez(f, obj, **kwargs)


def load_pkl(f: Union[str, BinaryIO], **kwargs) -> Any:
    with file_descriptor(f, mode='rb') as fd:
        try:
            return pickle.load(fd, **kwargs)
        except UnicodeDecodeError:
            if 'encoding' in kwargs:
                raise
            fd.seek(0)
            return pickle.load(fd, encoding='latin1', **kwargs)


def save_pkl(f: Union[str, BinaryIO], obj: Any, **kwargs) -> None:
    with file_descriptor(f, mode='wb') as fd:
        pickle.dump(obj, fd, **kwargs)


def load_pt(f: Union[str, BinaryIO], **kwargs) -> Any:
    return torch.load(f, **kwargs)


def save_pt(f: Union[str, BinaryIO], obj: Any, **kwargs) -> None:
    torch.save(obj, f, **kwargs)


def load_toml(f: Union[str, TextIO], obj: Any, **kwargs) -> Any:
    return toml.load(f, obj, **kwargs)


def save_toml(f: Union[str, TextIO], obj: Any, **kwargs) -> None:
    with file_descriptor(f, mode='w') as fd:
        toml.dump(obj, fd, **kwargs)


def load_yaml(f: Union[str, TextIO], **kwargs) -> Any:
    with file_descriptor(f, mode='r') as fd:
        return yaml.safe_load(fd, **kwargs)


def save_yaml(f: Union[str, TextIO], obj: Any, **kwargs) -> None:
    with file_descriptor(f, mode='w') as fd:
        yaml.safe_dump(obj, fd, **kwargs)


# yapf: disable
__io_registry = {
    '.json': {'load': load_json, 'save': save_json},
    '.jsonl': {'load': load_jsonl, 'save': save_jsonl},
    '.mat': {'load': load_mat, 'save': save_mat},
    '.npy': {'load': load_npy, 'save': save_npy},
    '.npz': {'load': load_npz, 'save': save_npz},
    '.pkl': {'load': load_pkl, 'save': save_pkl},
    '.pt': {'load': load_pt, 'save': save_pt},
    '.pth': {'load': load_pt, 'save': save_pt},
    '.pth.tar': {'load': load_pt, 'save': save_pt},
    '.toml': {'load': load_toml, 'save': save_toml},
    '.yaml': {'load': load_yaml, 'save': save_yaml},
    '.yml': {'load': load_yaml, 'save': save_yaml},
}
# yapf: enable


def load(fpath: str, **kwargs) -> Any:
    assert isinstance(fpath, str), type(fpath)

    for extension in sorted(__io_registry.keys(), key=len, reverse=True):
        if fpath.endswith(extension) and 'load' in __io_registry[extension]:
            return __io_registry[extension]['load'](fpath, **kwargs)

    raise NotImplementedError(f'"{fpath}" cannot be loaded.')


def save(fpath: str, obj: Any, **kwargs) -> None:
    assert isinstance(fpath, str), type(fpath)
    fs.makedir(os.path.dirname(fpath))

    for extension in sorted(__io_registry.keys(), key=len, reverse=True):
        if fpath.endswith(extension) and 'save' in __io_registry[extension]:
            __io_registry[extension]['save'](fpath, obj, **kwargs)
            return

    raise NotImplementedError(f'"{fpath}" cannot be saved.')
