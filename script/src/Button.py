from typing import Callable, Union
from Live import Clip
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE


class Button:
    def __init__(
        self,
        channel: int,
        identifier: int,
        allow_passthrough=False,
        log: Callable = None,
    ):
        self.identifier = identifier
        self.element = ButtonElement(True, MIDI_NOTE_TYPE, channel, identifier)
        self.log = log

        self.button.add_value_listener(self.button_value_listener)

        if allow_passthrough:
            self.allow_midi_passthrough()

    @property
    def note(self):
        return self.identifier

    def allow_midi_passthrough(self, allow: bool) -> None:
        self.element.suppress_script_forwarding = allow

    def button_value_listener(self, velocity: int):
        pass
