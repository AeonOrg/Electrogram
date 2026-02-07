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


class SendReaction(TLObject):  # type: ignore
    """React to message.


    Details:
        - Layer: ``224``
        - ID: ``D30D78D4``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer

        msg_id (``int`` ``32-bit``):
            Message ID to react to

        big (``bool``, *optional*):
            Whether a bigger and longer reaction should be shown

        add_to_recent (``bool``, *optional*):
            Whether to add this reaction to the recent reactions list ».

        reaction (List of :obj:`Reaction <pyrogram.raw.base.Reaction>`, *optional*):
            A list of reactions

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "big", "add_to_recent", "reaction"]

    ID = 0xd30d78d4
    QUALNAME = "functions.messages.SendReaction"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, big: Optional[bool] = None, add_to_recent: Optional[bool] = None, reaction: Optional[List["raw.base.Reaction"]] = None) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.big = big  # flags.1?true
        self.add_to_recent = add_to_recent  # flags.2?true
        self.reaction = reaction  # flags.0?Vector<Reaction>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendReaction":

        flags = Int.read(b)

        big = True if flags & (1 << 1) else False
        add_to_recent = True if flags & (1 << 2) else False
        peer = TLObject.read(b)

        msg_id = Int.read(b)

        reaction = TLObject.read(b) if flags & (1 << 0) else []

        return SendReaction(peer=peer, msg_id=msg_id, big=big, add_to_recent=add_to_recent, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.big else 0
        flags |= (1 << 2) if self.add_to_recent else 0
        flags |= (1 << 0) if self.reaction else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        if self.reaction is not None:
            b.write(Vector(self.reaction))

        return b.getvalue()
