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


class SetChatAvailableReactions(TLObject):  # type: ignore
    """Change the set of message reactions » that can be used in a certain group, supergroup or channel


    Details:
        - Layer: ``224``
        - ID: ``864B2581``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Group where to apply changes

        available_reactions (:obj:`ChatReactions <pyrogram.raw.base.ChatReactions>`):
            Allowed reaction emojis

        reactions_limit (``int`` ``32-bit``, *optional*):


        paid_enabled (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "available_reactions", "reactions_limit", "paid_enabled"]

    ID = 0x864b2581
    QUALNAME = "functions.messages.SetChatAvailableReactions"

    def __init__(self, *, peer: "raw.base.InputPeer", available_reactions: "raw.base.ChatReactions", reactions_limit: Optional[int] = None, paid_enabled: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.available_reactions = available_reactions  # ChatReactions
        self.reactions_limit = reactions_limit  # flags.0?int
        self.paid_enabled = paid_enabled  # flags.1?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatAvailableReactions":

        flags = Int.read(b)

        peer = TLObject.read(b)

        available_reactions = TLObject.read(b)

        reactions_limit = Int.read(b) if flags & (1 << 0) else None
        paid_enabled = Bool.read(b) if flags & (1 << 1) else None
        return SetChatAvailableReactions(peer=peer, available_reactions=available_reactions, reactions_limit=reactions_limit, paid_enabled=paid_enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reactions_limit is not None else 0
        flags |= (1 << 1) if self.paid_enabled is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(self.available_reactions.write())

        if self.reactions_limit is not None:
            b.write(Int(self.reactions_limit))

        if self.paid_enabled is not None:
            b.write(Bool(self.paid_enabled))

        return b.getvalue()
