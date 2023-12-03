from typing import Callable
from .Button import Button


class DeviceSelectButton(Button):
    def __init__(
        self,
        channel: int,
        identifier: int,
        log: Callable = None,
    ):
        Button.__init__(self, channel, identifier, allow_passthrough=False, log=log)

    def button_value_listener(self, velocity: int):
        if velocity > 0:
            # get a list of all devices that have snapshots
            # cycle through devices in list on press, selecting them - if none are selected, then start on first
            pass
