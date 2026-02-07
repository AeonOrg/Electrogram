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


class UpdateMessagePollVote(TLObject):  # type: ignore
    """A specific peer has voted in a poll

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``24F40E77``

    Parameters:
        poll_id (``int`` ``64-bit``):
            Poll ID

        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer that voted in the poll

        options (List of ``bytes``):
            Chosen option(s)

        qts (``int`` ``32-bit``):
            New qts value, see updates » for more info.

    """

    __slots__: List[str] = ["poll_id", "peer", "options", "qts"]

    ID = 0x24f40e77
    QUALNAME = "types.UpdateMessagePollVote"

    def __init__(self, *, poll_id: int, peer: "raw.base.Peer", options: List[bytes], qts: int) -> None:
        self.poll_id = poll_id  # long
        self.peer = peer  # Peer
        self.options = options  # Vector<bytes>
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessagePollVote":
        # No flags

        poll_id = Long.read(b)

        peer = TLObject.read(b)

        options = TLObject.read(b, Bytes)

        qts = Int.read(b)

        return UpdateMessagePollVote(poll_id=poll_id, peer=peer, options=options, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.poll_id))

        b.write(self.peer.write())

        b.write(Vector(self.options, Bytes))

        b.write(Int(self.qts))

        return b.getvalue()
