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


class UpdateBotMessageReactions(TLObject):  # type: ignore
    """Bots only: the number of reactions on a message with anonymous reactions has changed.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``9CB7759``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer of the reacted-to message.

        msg_id (``int`` ``32-bit``):
            ID of the reacted-to message.

        date (``int`` ``32-bit``):
            Date of the change.

        reactions (List of :obj:`ReactionCount <pyrogram.raw.base.ReactionCount>`):
            New reaction counters.

        qts (``int`` ``32-bit``):
            QTS event sequence identifier

    """

    __slots__: List[str] = ["peer", "msg_id", "date", "reactions", "qts"]

    ID = 0x9cb7759
    QUALNAME = "types.UpdateBotMessageReactions"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, date: int, reactions: List["raw.base.ReactionCount"], qts: int) -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.date = date  # int
        self.reactions = reactions  # Vector<ReactionCount>
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotMessageReactions":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        date = Int.read(b)

        reactions = TLObject.read(b)

        qts = Int.read(b)

        return UpdateBotMessageReactions(peer=peer, msg_id=msg_id, date=date, reactions=reactions, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Int(self.date))

        b.write(Vector(self.reactions))

        b.write(Int(self.qts))

        return b.getvalue()
