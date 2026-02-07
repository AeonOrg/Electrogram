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


class StarGiftAttributeOriginalDetails(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``E0BFF26C``

    Parameters:
        recipient_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        sender_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["recipient_id", "date", "sender_id", "message"]

    ID = 0xe0bff26c
    QUALNAME = "types.StarGiftAttributeOriginalDetails"

    def __init__(self, *, recipient_id: "raw.base.Peer", date: int, sender_id: "raw.base.Peer" = None, message: "raw.base.TextWithEntities" = None) -> None:
        self.recipient_id = recipient_id  # Peer
        self.date = date  # int
        self.sender_id = sender_id  # flags.0?Peer
        self.message = message  # flags.1?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeOriginalDetails":

        flags = Int.read(b)

        sender_id = TLObject.read(b) if flags & (1 << 0) else None

        recipient_id = TLObject.read(b)

        date = Int.read(b)

        message = TLObject.read(b) if flags & (1 << 1) else None

        return StarGiftAttributeOriginalDetails(recipient_id=recipient_id, date=date, sender_id=sender_id, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sender_id is not None else 0
        flags |= (1 << 1) if self.message is not None else 0
        b.write(Int(flags))

        if self.sender_id is not None:
            b.write(self.sender_id.write())

        b.write(self.recipient_id.write())

        b.write(Int(self.date))

        if self.message is not None:
            b.write(self.message.write())

        return b.getvalue()
