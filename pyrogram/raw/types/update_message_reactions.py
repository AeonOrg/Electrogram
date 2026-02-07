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


class UpdateMessageReactions(TLObject):  # type: ignore
    """New message reactions » are available

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``1E297BFA``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer

        msg_id (``int`` ``32-bit``):
            Message ID

        reactions (:obj:`MessageReactions <pyrogram.raw.base.MessageReactions>`):
            Reactions

        top_msg_id (``int`` ``32-bit``, *optional*):
            Forum topic ID

        saved_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "msg_id", "reactions", "top_msg_id", "saved_peer_id"]

    ID = 0x1e297bfa
    QUALNAME = "types.UpdateMessageReactions"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, reactions: "raw.base.MessageReactions", top_msg_id: Optional[int] = None, saved_peer_id: "raw.base.Peer" = None) -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.reactions = reactions  # MessageReactions
        self.top_msg_id = top_msg_id  # flags.0?int
        self.saved_peer_id = saved_peer_id  # flags.1?Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessageReactions":

        flags = Int.read(b)

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        saved_peer_id = TLObject.read(b) if flags & (1 << 1) else None

        reactions = TLObject.read(b)

        return UpdateMessageReactions(peer=peer, msg_id=msg_id, reactions=reactions, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        flags |= (1 << 1) if self.saved_peer_id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())

        b.write(self.reactions.write())

        return b.getvalue()
