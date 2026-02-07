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


class GroupCallMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.GroupCallMessage`.

    Details:
        - Layer: ``224``
        - ID: ``1A8AFC7E``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        from_admin (``bool``, *optional*):
            N/A

        paid_message_stars (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "from_id", "date", "message", "from_admin", "paid_message_stars"]

    ID = 0x1a8afc7e
    QUALNAME = "types.GroupCallMessage"

    def __init__(self, *, id: int, from_id: "raw.base.Peer", date: int, message: "raw.base.TextWithEntities", from_admin: Optional[bool] = None, paid_message_stars: Optional[int] = None) -> None:
        self.id = id  # int
        self.from_id = from_id  # Peer
        self.date = date  # int
        self.message = message  # TextWithEntities
        self.from_admin = from_admin  # flags.1?true
        self.paid_message_stars = paid_message_stars  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallMessage":

        flags = Int.read(b)

        from_admin = True if flags & (1 << 1) else False
        id = Int.read(b)

        from_id = TLObject.read(b)

        date = Int.read(b)

        message = TLObject.read(b)

        paid_message_stars = Long.read(b) if flags & (1 << 0) else None
        return GroupCallMessage(id=id, from_id=from_id, date=date, message=message, from_admin=from_admin, paid_message_stars=paid_message_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.from_admin else 0
        flags |= (1 << 0) if self.paid_message_stars is not None else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        b.write(self.from_id.write())

        b.write(Int(self.date))

        b.write(self.message.write())

        if self.paid_message_stars is not None:
            b.write(Long(self.paid_message_stars))

        return b.getvalue()
