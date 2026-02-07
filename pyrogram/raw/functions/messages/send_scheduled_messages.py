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


class SendScheduledMessages(TLObject):  # type: ignore
    """Send scheduled messages right away


    Details:
        - Layer: ``224``
        - ID: ``BD38850A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer

        id (List of ``int`` ``32-bit``):
            Scheduled message IDs

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0xbd38850a
    QUALNAME = "functions.messages.SendScheduledMessages"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int]) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendScheduledMessages":
        # No flags

        peer = TLObject.read(b)

        id = TLObject.read(b, Int)

        return SendScheduledMessages(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Vector(self.id, Int))

        return b.getvalue()
