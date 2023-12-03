from __future__ import with_statement
from typing import List

import Live
from _Framework.ControlSurface import ControlSurface
from .DeviceSelectButton import DeviceSelectButton
from .SnapSelectButton import SnapSelectButton

from .mappings import *
from .enums import *


class SnapSelect(ControlSurface):
    __module__ = __name__
    __doc__ = "SnapSelect"

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            live = Live.Application.get_application()
            self._live_major_version = live.get_major_version()
            self._live_minor_version = live.get_minor_version()
            self._live_bugfix_version = live.get_bugfix_version()

            for track in self.tracks():
                self.log_message(track.name)

            self.log_message("Loaded MacroSelect")

            self.device_select_button = DeviceSelectButton(
                channel=CHANNEL, identifier=DEVICE_SELECT_BUTTON, log=self.log_message
            )

            self.snap_select_button = SnapSelectButton(
                channel=CHANNEL, identifier=SNAP_SELECT_BUTTON, log=self.log_message
            )

    def song(self) -> Live.Song.Song:
        return super().song()

    def tracks(self) -> List[Live.Track.Track]:
        return self.song().tracks

    def disconnect(self):
        """clean up on disconnect"""
        ControlSurface.disconnect(self)
        return None
