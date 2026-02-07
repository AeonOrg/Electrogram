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


class ReportSpam(TLObject):  # type: ignore
    """Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup


    Details:
        - Layer: ``224``
        - ID: ``F44A8315``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Supergroup

        participant (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Participant whose messages should be reported

        id (List of ``int`` ``32-bit``):
            IDs of spam messages

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "participant", "id"]

    ID = 0xf44a8315
    QUALNAME = "functions.channels.ReportSpam"

    def __init__(self, *, channel: "raw.base.InputChannel", participant: "raw.base.InputPeer", id: List[int]) -> None:
        self.channel = channel  # InputChannel
        self.participant = participant  # InputPeer
        self.id = id  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportSpam":
        # No flags

        channel = TLObject.read(b)

        participant = TLObject.read(b)

        id = TLObject.read(b, Int)

        return ReportSpam(channel=channel, participant=participant, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(self.participant.write())

        b.write(Vector(self.id, Int))

        return b.getvalue()
