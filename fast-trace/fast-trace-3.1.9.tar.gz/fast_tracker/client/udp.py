#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by FAST-DEV 2021/4/6
"""
import json
import requests
import socket
from fast_tracker import config
from fast_tracker.fast_tracker import FastTracker
from fast_tracker.loggings import logger
from fast_tracker.client import ServiceManagementClient, TraceSegmentReportService
from fast_tracker.report.report_struct import ReportStruct
from fast_tracker.trace import tags
from fast_tracker.utils import functions


class UdpServiceManagementClient(ServiceManagementClient):
    def __init__(self):
        self.session = requests.session()

    def send_instance_props(self):
        url = config.collector_address.rstrip("/") + "/v3/management/reportProperties"
        res = self.session.post(
            url,
            json={
                "service": config.service_name,
                "serviceInstance": config.service_instance,
                "properties": [
                    {
                        "language": "Python",
                    }
                ],
            },
        )
        logger.debug("heartbeat response: %s", res)

    def send_heart_beat(self):
        logger.debug(
            "service heart beats, [%s], [%s]",
            config.service_name,
            config.service_instance,
        )
        url = config.collector_address.rstrip("/") + "/v3/management/keepAlive"
        res = self.session.post(
            url,
            json={
                "service": config.service_name,
                "serviceInstance": config.service_instance,
            },
        )
        logger.debug("heartbeat response: %s", res)


class UdpTraceSegmentReportService(TraceSegmentReportService):
    def __init__(self):
        self.udp_ip = ""
        self.udp_port = 80
        if config.collector_address:
            self._init_ip_and_port(config.collector_address)
        self.buffer_size = config.buffer_size
        self.type_dict = {"Entry": 0, "Exit": 1, "Local": 2}
        self.layer_dict = {
            "local": 0,
            "database": 1,
            "rpc_framework": 2,
            "http": 3,
            "mq": 4,
            "cache": 5,
        }

    def _init_ip_and_port(self, collector):
        """
        初始化udp数据上报的ip和port信息
        :param str collector: 上报数据的ip和port信息合并在一起的字符串
        :return:
        """
        if not collector:
            functions.log("socket_path参数为空")
            return False

        connections = collector.split(":")
        if len(connections) == 2:
            self.udp_ip, self.udp_port = connections
            self.udp_port = int(self.udp_port)
        elif len(connections) == 3:
            self.udp_ip = connections[1].strip("//")
            self.udp_port = int(connections[2]) if len(connections) > 2 else 80
        else:
            functions.log("socket_path参数不合法")
            return False

    def report(self, generator):
        """
        udp 数据包发送
        :param generator:
        :return:
        """
        try:
            functions.log("udp socket start", level=4)
            udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
            functions.log("udp socket object success")
            for segment in generator:
                for span in segment.spans:
                    functions.log("udp socket object will get data", level=4)
                    data = self._get_data(segment, span)
                    functions.log("udp socket object get data", level=4)
                    res = udp_sock.sendto(data, (self.udp_ip, self.udp_port))
                    # res = udp_sock.sendto(data, ("fluent-bit", 5140))
                    functions.log("udp socket ip: %s, port: %d", self.udp_ip, self.udp_port, level=4)
                    functions.log("sended message: %r, result is: %r", data, res)
        except BaseException as e:
            functions.log("udp report error: %r", e)

    def _get_data(self, segment, span):
        """
        udp 数据包组装
        :param segment:
        :param span:
        :return:
        """
        ft = FastTracker()
        report_struct = ReportStruct()
        report_struct.product_code = config.product_code
        report_struct.app_code = config.app_code
        report_struct.service_name = config.service_name
        report_struct.env_code = ft.env_code
        report_struct.tenant_code = ft.tenant_code
        report_struct.user_code = ft.user_code
        report_struct.trace_id = str(segment.related_traces[0])
        report_struct.parent_span_id = span.pid
        report_struct.span_id = span.sid
        report_struct.span_type = self.type_dict.get(span.kind.name, 3)
        report_struct.span_layer = self.layer_dict.get(str(span.layer.name).lower(), 10)
        report_struct.start_time = span.start_time
        report_struct.end_time = span.end_time
        report_struct.duration = 1 if span.end_time - span.start_time == 0 else span.end_time - span.start_time
        report_struct.component = span.component
        report_struct.operation_name = span.op
        report_struct.peer = span.peer
        report_struct.is_error = span.error_occurred
        report_struct.tags = self.convert_tags(span.tags)
        report_struct.logs = self.convert_logs(span.logs)
        item = ReportStruct.convert(report_struct)
        functions.log("report_struct: %r", item, level=2)
        data = json.dumps(item).encode("utf-8")
        return data

    def convert_tags(self, tags_data):
        """
        组装上报的tags数据结构
        :param tags_data:
        :return:
        """
        data = {}
        if not tags_data:
            return data
        for tag in tags_data:
            data[tag.key] = str(tag.val)

        return data

    def convert_logs(self, logs_data):
        """
        组装上报的logs数据结构
        :param logs_data:
        :return:
        """
        data = []
        if not logs_data:
            return data
        for log in logs_data:
            for item in log.items:
                if type(item.val) == str:
                    alpha = {
                        "Timestamp": str(log.timestamp * 1000),
                        "Data": {
                            "event": item.key,
                            "message": item.val,
                            "error_kind": "Error",
                            "stack": "",
                        },
                    }
                else:
                    alpha = {
                        "Timestamp": str(log.timestamp * 1000),
                        "Data": {
                            "event": item.key,
                            "message": item.val.get("err_msg"),
                            "error_kind": item.val.get("err_type"),
                            "stack": item.val.get("err_trace"),
                        },
                    }
                data.append(alpha)

        return data
