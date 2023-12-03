from __future__ import with_statement

import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.ButtonElement import ButtonElement

from .mappings import *
from .consts import *
from .enums import *


class MacroSelect(ControlSurface):
    __module__ = __name__
    __doc__ = "MacroSelect"

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            live = Live.Application.get_application()
            self._live_major_version = live.get_major_version()
            self._live_minor_version = live.get_minor_version()
            self._live_bugfix_version = live.get_bugfix_version()

            self._note_map = []
            self._load_MIDI_map()

            # write your init code here

    def disconnect(self):
        """clean up on disconnect"""
        ControlSurface.disconnect(self)
        return None

    def _load_mappings(self):
        momentary = True

        for note in range(128):
            button = ButtonElement(momentary, types.NOTE, CHANNEL, note)
            button.name = "Note_" + str(note)
            self._note_map.append(button)
        self._note_map.append(None)
