from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ChannelAdminLogEventActionParticipantVolume(TLObject):  # type: ignore
    """channelAdminLogEvent.user_id has set the volume of participant.peer to participant.volume

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``3E7F6847``

    Parameters:
        participant (:obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            The participant whose volume was changed

    """

    __slots__: List[str] = ["participant"]

    ID = 0x3e7f6847
    QUALNAME = "types.ChannelAdminLogEventActionParticipantVolume"

    def __init__(self, *, participant: "raw.base.GroupCallParticipant") -> None:
        self.participant = participant  # GroupCallParticipant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantVolume":
        # No flags

        participant = TLObject.read(b)

        return ChannelAdminLogEventActionParticipantVolume(participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.participant.write())

        return b.getvalue()
