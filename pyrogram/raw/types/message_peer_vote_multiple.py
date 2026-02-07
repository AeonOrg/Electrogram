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


class MessagePeerVoteMultiple(TLObject):  # type: ignore
    """How a peer voted in a multiple-choice poll

    Constructor of :obj:`~pyrogram.raw.base.MessagePeerVote`.

    Details:
        - Layer: ``224``
        - ID: ``4628F6E6``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer ID

        options (List of ``bytes``):
            Options chosen by the peer

        date (``int`` ``32-bit``):
            When did the peer cast their votes

    """

    __slots__: List[str] = ["peer", "options", "date"]

    ID = 0x4628f6e6
    QUALNAME = "types.MessagePeerVoteMultiple"

    def __init__(self, *, peer: "raw.base.Peer", options: List[bytes], date: int) -> None:
        self.peer = peer  # Peer
        self.options = options  # Vector<bytes>
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerVoteMultiple":
        # No flags

        peer = TLObject.read(b)

        options = TLObject.read(b, Bytes)

        date = Int.read(b)

        return MessagePeerVoteMultiple(peer=peer, options=options, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Vector(self.options, Bytes))

        b.write(Int(self.date))

        return b.getvalue()
