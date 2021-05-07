"""
Class object for Processes
Documentation: https://system-bridge.timmo.dev

Generated by generator/generator.py - 2021-02-21 13:16:34.619813
"""
from .base import BridgeBase


class ProccessList(BridgeBase):
    @property
    def pid(self):
        return self.attributes.get("pid", None)

    @property
    def parentPid(self):
        return self.attributes.get("parentPid", None)

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def cpu(self):
        return self.attributes.get("cpu", None)

    @property
    def cpuu(self):
        return self.attributes.get("cpuu", None)

    @property
    def cpus(self):
        return self.attributes.get("cpus", None)

    @property
    def mem(self):
        return self.attributes.get("mem", None)

    @property
    def priority(self):
        return self.attributes.get("priority", None)

    @property
    def memVsz(self):
        return self.attributes.get("memVsz", None)

    @property
    def memRss(self):
        return self.attributes.get("memRss", None)

    @property
    def nice(self):
        return self.attributes.get("nice", None)

    @property
    def started(self):
        return self.attributes.get("started", "")

    @property
    def state(self):
        return self.attributes.get("state", "")

    @property
    def tty(self):
        return self.attributes.get("tty", "")

    @property
    def user(self):
        return self.attributes.get("user", "")

    @property
    def command(self):
        return self.attributes.get("command", "")

    @property
    def params(self):
        return self.attributes.get("params", "")

    @property
    def path(self):
        return self.attributes.get("path", "")


class Cpus(BridgeBase):
    @property
    def load(self):
        return self.attributes.get("load", None)

    @property
    def loadUser(self):
        return self.attributes.get("loadUser", None)

    @property
    def loadSystem(self):
        return self.attributes.get("loadSystem", None)

    @property
    def loadNice(self):
        return self.attributes.get("loadNice", None)

    @property
    def loadIdle(self):
        return self.attributes.get("loadIdle", None)

    @property
    def loadIrq(self):
        return self.attributes.get("loadIrq", None)

    @property
    def rawLoad(self):
        return self.attributes.get("rawLoad", None)

    @property
    def rawLoadUser(self):
        return self.attributes.get("rawLoadUser", None)

    @property
    def rawLoadSystem(self):
        return self.attributes.get("rawLoadSystem", None)

    @property
    def rawLoadNice(self):
        return self.attributes.get("rawLoadNice", None)

    @property
    def rawLoadIdle(self):
        return self.attributes.get("rawLoadIdle", None)

    @property
    def rawLoadIrq(self):
        return self.attributes.get("rawLoadIrq", None)


class Load(BridgeBase):
    @property
    def avgLoad(self):
        return self.attributes.get("avgLoad", None)

    @property
    def currentLoad(self):
        return self.attributes.get("currentLoad", None)

    @property
    def currentLoadUser(self):
        return self.attributes.get("currentLoadUser", None)

    @property
    def currentLoadSystem(self):
        return self.attributes.get("currentLoadSystem", None)

    @property
    def currentLoadNice(self):
        return self.attributes.get("currentLoadNice", None)

    @property
    def currentLoadIdle(self):
        return self.attributes.get("currentLoadIdle", None)

    @property
    def currentLoadIrq(self):
        return self.attributes.get("currentLoadIrq", None)

    @property
    def rawCurrentLoad(self):
        return self.attributes.get("rawCurrentLoad", None)

    @property
    def rawCurrentLoadUser(self):
        return self.attributes.get("rawCurrentLoadUser", None)

    @property
    def rawCurrentLoadSystem(self):
        return self.attributes.get("rawCurrentLoadSystem", None)

    @property
    def rawCurrentLoadNice(self):
        return self.attributes.get("rawCurrentLoadNice", None)

    @property
    def rawCurrentLoadIdle(self):
        return self.attributes.get("rawCurrentLoadIdle", None)

    @property
    def rawCurrentLoadIrq(self):
        return self.attributes.get("rawCurrentLoadIrq", None)

    @property
    def cpus(self):
        return [Cpus(x) for x in self.attributes.get("cpus", [])]


class Processes(BridgeBase):
    @property
    def all(self):
        return self.attributes.get("all", None)

    @property
    def running(self):
        return self.attributes.get("running", None)

    @property
    def blocked(self):
        return self.attributes.get("blocked", None)

    @property
    def sleeping(self):
        return self.attributes.get("sleeping", None)

    @property
    def unknown(self):
        return self.attributes.get("unknown", None)

    @property
    def proccessList(self):
        return [ProccessList(x) for x in self.attributes.get("list", [])]

    @property
    def load(self):
        return Load(self.attributes.get("load", {}))
