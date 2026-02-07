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


class UpdateBotMessageReaction(TLObject):  # type: ignore
    """Bots only: a user has changed their reactions on a message with public reactions.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``AC21D3CE``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer of the reacted-to message.

        msg_id (``int`` ``32-bit``):
            ID of the reacted-to message.

        date (``int`` ``32-bit``):
            Date of the change.

        actor (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The user that (un)reacted to the message.

        old_reactions (List of :obj:`Reaction <pyrogram.raw.base.Reaction>`):
            Old reactions

        new_reactions (List of :obj:`Reaction <pyrogram.raw.base.Reaction>`):
            New reactions

        qts (``int`` ``32-bit``):
            QTS event sequence identifier

    """

    __slots__: List[str] = ["peer", "msg_id", "date", "actor", "old_reactions", "new_reactions", "qts"]

    ID = 0xac21d3ce
    QUALNAME = "types.UpdateBotMessageReaction"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, date: int, actor: "raw.base.Peer", old_reactions: List["raw.base.Reaction"], new_reactions: List["raw.base.Reaction"], qts: int) -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.date = date  # int
        self.actor = actor  # Peer
        self.old_reactions = old_reactions  # Vector<Reaction>
        self.new_reactions = new_reactions  # Vector<Reaction>
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotMessageReaction":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        date = Int.read(b)

        actor = TLObject.read(b)

        old_reactions = TLObject.read(b)

        new_reactions = TLObject.read(b)

        qts = Int.read(b)

        return UpdateBotMessageReaction(peer=peer, msg_id=msg_id, date=date, actor=actor, old_reactions=old_reactions, new_reactions=new_reactions, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Int(self.date))

        b.write(self.actor.write())

        b.write(Vector(self.old_reactions))

        b.write(Vector(self.new_reactions))

        b.write(Int(self.qts))

        return b.getvalue()
