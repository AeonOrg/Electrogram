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


class MessagePeerVoteInputOption(TLObject):  # type: ignore
    """How a peer voted in a poll (reduced constructor, returned if an option was provided to messages.getPollVotes)

    Constructor of :obj:`~pyrogram.raw.base.MessagePeerVote`.

    Details:
        - Layer: ``224``
        - ID: ``74CDA504``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer that voted for the queried option

        date (``int`` ``32-bit``):
            When did the peer cast the vote

    """

    __slots__: List[str] = ["peer", "date"]

    ID = 0x74cda504
    QUALNAME = "types.MessagePeerVoteInputOption"

    def __init__(self, *, peer: "raw.base.Peer", date: int) -> None:
        self.peer = peer  # Peer
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerVoteInputOption":
        # No flags

        peer = TLObject.read(b)

        date = Int.read(b)

        return MessagePeerVoteInputOption(peer=peer, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.date))

        return b.getvalue()
