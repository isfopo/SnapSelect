from typing import Callable
from .Button import Button


class SnapSelectButton(Button):
    def __init__(
        self,
        channel: int,
        identifier: int,
        next_snap: Callable,
        log: Callable = None,
    ):
        Button.__init__(self, channel, identifier, allow_passthrough=False, log=log)
        self.next_snap = next_snap

    def button_value_listener(self, velocity: int):
        if velocity > 0:
            self.next_snap()
