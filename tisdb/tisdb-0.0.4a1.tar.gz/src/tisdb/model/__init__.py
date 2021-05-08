# -*- coding; utf-8

from typing import List
from sortedcontainers import SortedDict
from datetime import datetime
from hashlib import md5
import json

from tisdb.errors import BaseInfo

__all__ = ("TsdbData", "TsdbTags", "TsdbFields", "SaveResult")


class TsdbTags(SortedDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TsdbFields(SortedDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TsdbData(object):
    """Tsdb Data Value Object

    Args:
        metric (str): metric name
        ts (datetime): timestamp of this data
        tags (TsdbTags): tags of this data
        fields (TsdbFields): fields of this data
    """

    def __init__(
        self,
        metric: str,
        ts: datetime = datetime.now(),
        tags: TsdbTags = TsdbTags(),
        fields: TsdbFields = TsdbFields(value=0),
    ):
        super().__init__()
        self._metric = metric
        self._ts = datetime.strptime(
            ts.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"
        )
        self._tags = tags
        uuid_gen = md5()
        uuid_gen.update(json.dumps(tags).encode(encoding="utf-8"))
        self._tags_uuid = uuid_gen.hexdigest()
        self._fields = fields
        self._value_id = -1

    @property
    def metric(self) -> str:
        return self._metric

    @property
    def ts(self) -> datetime:
        return self._ts

    @property
    def tags_uuid(self) -> str:
        return self._tags_uuid

    @property
    def tags(self) -> TsdbTags:
        return self._tags

    def get_value(self, field_name: str) -> float:
        return self._fields[field_name]

    @property
    def value_id(self) -> int:
        return self._value_id

    @value_id.setter
    def value_id(self, value_id: int):
        self._value_id = value_id


class SaveResult(object):
    """Result of the save function

    Args:
        data (List[TsdbData]): Tsdb data to save this time
        subcode (int): return subcode of this save result
        status (str): status of this save result
    """

    def __init__(
        self, data: List[TsdbData], subcode: int = None, status: str = None
    ) -> None:
        super().__init__()
        self._data = data
        self._subcode = subcode or BaseInfo.SUBCODE
        self._status = status or BaseInfo.STATUS

    @property
    def data(self):
        return self._data
