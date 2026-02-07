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


class ChannelAdminLogEventActionParticipantInvite(TLObject):  # type: ignore
    """A user was invited to the group

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``E31C34D8``

    Parameters:
        participant (:obj:`ChannelParticipant <pyrogram.raw.base.ChannelParticipant>`):
            The user that was invited

    """

    __slots__: List[str] = ["participant"]

    ID = 0xe31c34d8
    QUALNAME = "types.ChannelAdminLogEventActionParticipantInvite"

    def __init__(self, *, participant: "raw.base.ChannelParticipant") -> None:
        self.participant = participant  # ChannelParticipant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantInvite":
        # No flags

        participant = TLObject.read(b)

        return ChannelAdminLogEventActionParticipantInvite(participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.participant.write())

        return b.getvalue()
