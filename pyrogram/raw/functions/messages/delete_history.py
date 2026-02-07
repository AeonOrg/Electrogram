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


class DeleteHistory(TLObject):  # type: ignore
    """Deletes communication history.


    Details:
        - Layer: ``224``
        - ID: ``B08F922A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            User or chat, communication history of which will be deleted

        max_id (``int`` ``32-bit``):
            Maximum ID of message to delete

        just_clear (``bool``, *optional*):
            Just clear history for the current user, without actually removing messages for every chat user

        revoke (``bool``, *optional*):
            Whether to delete the message history for all chat participants

        min_date (``int`` ``32-bit``, *optional*):
            Delete all messages newer than this UNIX timestamp

        max_date (``int`` ``32-bit``, *optional*):
            Delete all messages older than this UNIX timestamp

    Returns:
        :obj:`messages.AffectedHistory <pyrogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["peer", "max_id", "just_clear", "revoke", "min_date", "max_date"]

    ID = 0xb08f922a
    QUALNAME = "functions.messages.DeleteHistory"

    def __init__(self, *, peer: "raw.base.InputPeer", max_id: int, just_clear: Optional[bool] = None, revoke: Optional[bool] = None, min_date: Optional[int] = None, max_date: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.max_id = max_id  # int
        self.just_clear = just_clear  # flags.0?true
        self.revoke = revoke  # flags.1?true
        self.min_date = min_date  # flags.2?int
        self.max_date = max_date  # flags.3?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteHistory":

        flags = Int.read(b)

        just_clear = True if flags & (1 << 0) else False
        revoke = True if flags & (1 << 1) else False
        peer = TLObject.read(b)

        max_id = Int.read(b)

        min_date = Int.read(b) if flags & (1 << 2) else None
        max_date = Int.read(b) if flags & (1 << 3) else None
        return DeleteHistory(peer=peer, max_id=max_id, just_clear=just_clear, revoke=revoke, min_date=min_date, max_date=max_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.just_clear else 0
        flags |= (1 << 1) if self.revoke else 0
        flags |= (1 << 2) if self.min_date is not None else 0
        flags |= (1 << 3) if self.max_date is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.max_id))

        if self.min_date is not None:
            b.write(Int(self.min_date))

        if self.max_date is not None:
            b.write(Int(self.max_date))

        return b.getvalue()
