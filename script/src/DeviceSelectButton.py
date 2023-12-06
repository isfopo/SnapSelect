from typing import Callable
from .Button import Button


class DeviceSelectButton(Button):
    def __init__(
        self,
        channel: int,
        identifier: int,
        next_device: Callable,
        log: Callable = None,
    ):
        Button.__init__(self, channel, identifier, allow_passthrough=False, log=log)
        self.next_device = next_device

    def button_value_listener(self, velocity: int):
        if velocity > 0:
            self.next_device()
