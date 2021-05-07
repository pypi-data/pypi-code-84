"""
Class object for CommandResponse
Documentation: https://system-bridge.timmo.dev

Generated by generator/generator.py - 2021-02-20 16:57:03.395502
"""
from .payload import CommandPayload


class CommandResponse(CommandPayload):
    @property
    def success(self):
        return self.attributes.get("success", True)

    @property
    def message(self):
        return self.attributes.get("message", "")
