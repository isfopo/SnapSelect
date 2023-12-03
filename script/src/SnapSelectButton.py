from typing import Callable
from .Button import Button


class SnapSelectButton(Button):
    def __init__(
        self,
        channel: int,
        identifier: int,
        log: Callable = None,
    ):
        Button.__init__(self, channel, identifier, allow_passthrough=False, log=log)

    def button_value_listener(self, velocity: int):
        if velocity > 0:
            # get a list of snapshots for selected device
            # cycle through snapshots in list on press
            pass
