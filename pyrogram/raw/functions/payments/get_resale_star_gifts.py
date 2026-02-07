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


class GetResaleStarGifts(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7A5FA236``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        sort_by_price (``bool``, *optional*):
            N/A

        sort_by_num (``bool``, *optional*):
            N/A

        for_craft (``bool``, *optional*):
            N/A

        attributes_hash (``int`` ``64-bit``, *optional*):
            N/A

        attributes (List of :obj:`StarGiftAttributeId <pyrogram.raw.base.StarGiftAttributeId>`, *optional*):
            N/A

    Returns:
        :obj:`payments.ResaleStarGifts <pyrogram.raw.base.payments.ResaleStarGifts>`
    """

    __slots__: List[str] = ["gift_id", "offset", "limit", "sort_by_price", "sort_by_num", "for_craft", "attributes_hash", "attributes"]

    ID = 0x7a5fa236
    QUALNAME = "functions.payments.GetResaleStarGifts"

    def __init__(self, *, gift_id: int, offset: str, limit: int, sort_by_price: Optional[bool] = None, sort_by_num: Optional[bool] = None, for_craft: Optional[bool] = None, attributes_hash: Optional[int] = None, attributes: Optional[List["raw.base.StarGiftAttributeId"]] = None) -> None:
        self.gift_id = gift_id  # long
        self.offset = offset  # string
        self.limit = limit  # int
        self.sort_by_price = sort_by_price  # flags.1?true
        self.sort_by_num = sort_by_num  # flags.2?true
        self.for_craft = for_craft  # flags.4?true
        self.attributes_hash = attributes_hash  # flags.0?long
        self.attributes = attributes  # flags.3?Vector<StarGiftAttributeId>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetResaleStarGifts":

        flags = Int.read(b)

        sort_by_price = True if flags & (1 << 1) else False
        sort_by_num = True if flags & (1 << 2) else False
        for_craft = True if flags & (1 << 4) else False
        attributes_hash = Long.read(b) if flags & (1 << 0) else None
        gift_id = Long.read(b)

        attributes = TLObject.read(b) if flags & (1 << 3) else []

        offset = String.read(b)

        limit = Int.read(b)

        return GetResaleStarGifts(gift_id=gift_id, offset=offset, limit=limit, sort_by_price=sort_by_price, sort_by_num=sort_by_num, for_craft=for_craft, attributes_hash=attributes_hash, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.sort_by_price else 0
        flags |= (1 << 2) if self.sort_by_num else 0
        flags |= (1 << 4) if self.for_craft else 0
        flags |= (1 << 0) if self.attributes_hash is not None else 0
        flags |= (1 << 3) if self.attributes else 0
        b.write(Int(flags))

        if self.attributes_hash is not None:
            b.write(Long(self.attributes_hash))

        b.write(Long(self.gift_id))

        if self.attributes is not None:
            b.write(Vector(self.attributes))

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
