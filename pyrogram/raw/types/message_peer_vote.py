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


class MessagePeerVote(TLObject):  # type: ignore
    """How a peer voted in a poll

    Constructor of :obj:`~pyrogram.raw.base.MessagePeerVote`.

    Details:
        - Layer: ``224``
        - ID: ``B6CC2D5C``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer ID

        option (``bytes``):
            The option chosen by the peer

        date (``int`` ``32-bit``):
            When did the peer cast the vote

    """

    __slots__: List[str] = ["peer", "option", "date"]

    ID = 0xb6cc2d5c
    QUALNAME = "types.MessagePeerVote"

    def __init__(self, *, peer: "raw.base.Peer", option: bytes, date: int) -> None:
        self.peer = peer  # Peer
        self.option = option  # bytes
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerVote":
        # No flags

        peer = TLObject.read(b)

        option = Bytes.read(b)

        date = Int.read(b)

        return MessagePeerVote(peer=peer, option=option, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Bytes(self.option))

        b.write(Int(self.date))

        return b.getvalue()
