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


class ChannelAdminLogEventActionParticipantMute(TLObject):  # type: ignore
    """A group call participant was muted

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``F92424D2``

    Parameters:
        participant (:obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            The participant that was muted

    """

    __slots__: List[str] = ["participant"]

    ID = 0xf92424d2
    QUALNAME = "types.ChannelAdminLogEventActionParticipantMute"

    def __init__(self, *, participant: "raw.base.GroupCallParticipant") -> None:
        self.participant = participant  # GroupCallParticipant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantMute":
        # No flags

        participant = TLObject.read(b)

        return ChannelAdminLogEventActionParticipantMute(participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.participant.write())

        return b.getvalue()
