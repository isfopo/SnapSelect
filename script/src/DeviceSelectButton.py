from typing import Callable
from .Button import Button


class DeviceSelectButton(Button):
    def __init__(
        self,
        channel: int,
        identifier: int,
        log: Callable = None,
    ):
        log("device button loaded")
        Button.__init__(self, channel, identifier, allow_passthrough=False, log=log)

    def button_value_listener(self, velocity: int):
        self.log("button pressed")
