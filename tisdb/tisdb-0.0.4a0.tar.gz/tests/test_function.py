# -*- coding: utf-8

from tests.test_base import TsdbTestCase
from tisdb.model import TsdbData, TsdbTags
from hashlib import md5
import json

from tisdb.types import OpType


class TsdbTest(TsdbTestCase):
    def test_taguk(self):
        gen = md5()
        data = TsdbData(metric="zzf_test", tags=TsdbTags(gameid="zzf", channel="haha"))
        a = json.dumps({"channel": "haha", "gameid": "zzf"})
        gen.update(a.encode("utf-8"))
        taguk = gen.hexdigest()
        b = json.dumps(data.tags)
        self.assertValueEqual(a, b)
        self.assertValueEqual(taguk, data.tags_uuid)

    def test_01_save_ignore(self):
        res = self.tsdb.save(
            self.tsdb.parse(
                {
                    "metric": "zzf_test",
                    "ts": "2021-05-20T01:01:01+08:00",
                    "tag": {"gameid": "zzf", "channel": "haha"},
                    "field": {"value": 1},
                }
            ),
            op_type=OpType.INSERT_IGNORE,
        )
        self.assertNotEqual(res.data[0], -1)

    def test_02_save_ignore(self):
        res = self.tsdb.save(
            self.tsdb.parse(
                {
                    "metric": "zzf_test",
                    "ts": "2021-04-01T01:01:01+08:00",
                    "tag": {"gameid": "zzf", "channel": "haha"},
                    "field": {"value": 1},
                }
            )
        )
        self.assertNotEqual(res.data[0], -1)
        res = self.tsdb._parse_mydb_result(
            {
                "metric": "zzf_test",
                "ts": "2021-04-01T01:01:01+08:00",
                "tag_gameid": "zzf",
                "tag_channel": "haha",
                "fieldvalue_yoyokaka": 1,
            }
        )
        self.assertEqual(res["metric"], "zzf_test_yoyokaka")

    def test_03_create_and_save(self):
        sql_str = """
        SELECT 'zzf_test2' as metric, DATE(ts) as ts, 'zzf2' as tag_ggid, 'zzf2' as tag_ch, count(1) as value
        FROM test.mtsv2
        WHERE
            ts > %(starttime)s and ts < %(endtime)s
        GROUP BY DATE(ts)
        """
        for tsdb_data in self.tsdb.parse_many(
            self.tsdb.create_tsdbdata_mydb(
                sql_str,
                param={"starttime": "2021-03-22", "endtime": "2021-04-30"},
                conn_conf={"db": "test"},
            )
        ):
            res = self.tsdb.save(tsdb_data)
            self.assertNotEqual(res.data[0], -1)
