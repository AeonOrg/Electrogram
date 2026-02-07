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


class SetGameScore(TLObject):  # type: ignore
    """Use this method to set the score of the specified user in a game sent as a normal message (bots only).


    Details:
        - Layer: ``224``
        - ID: ``8EF8ECC0``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Unique identifier of target chat

        id (``int`` ``32-bit``):
            Identifier of the sent message

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            User identifier

        score (``int`` ``32-bit``):
            New score

        edit_message (``bool``, *optional*):
            Set this flag if the game message should be automatically edited to include the current scoreboard

        force (``bool``, *optional*):
            Set this flag if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "user_id", "score", "edit_message", "force"]

    ID = 0x8ef8ecc0
    QUALNAME = "functions.messages.SetGameScore"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, user_id: "raw.base.InputUser", score: int, edit_message: Optional[bool] = None, force: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.user_id = user_id  # InputUser
        self.score = score  # int
        self.edit_message = edit_message  # flags.0?true
        self.force = force  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetGameScore":

        flags = Int.read(b)

        edit_message = True if flags & (1 << 0) else False
        force = True if flags & (1 << 1) else False
        peer = TLObject.read(b)

        id = Int.read(b)

        user_id = TLObject.read(b)

        score = Int.read(b)

        return SetGameScore(peer=peer, id=id, user_id=user_id, score=score, edit_message=edit_message, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.edit_message else 0
        flags |= (1 << 1) if self.force else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.id))

        b.write(self.user_id.write())

        b.write(Int(self.score))

        return b.getvalue()
