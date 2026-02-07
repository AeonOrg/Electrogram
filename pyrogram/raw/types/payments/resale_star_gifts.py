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


class ResaleStarGifts(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.ResaleStarGifts`.

    Details:
        - Layer: ``224``
        - ID: ``947A12DF``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        gifts (List of :obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

        attributes (List of :obj:`StarGiftAttribute <pyrogram.raw.base.StarGiftAttribute>`, *optional*):
            N/A

        attributes_hash (``int`` ``64-bit``, *optional*):
            N/A

        counters (List of :obj:`StarGiftAttributeCounter <pyrogram.raw.base.StarGiftAttributeCounter>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetResaleStarGifts
    """

    __slots__: List[str] = ["count", "gifts", "chats", "users", "next_offset", "attributes", "attributes_hash", "counters"]

    ID = 0x947a12df
    QUALNAME = "types.payments.ResaleStarGifts"

    def __init__(self, *, count: int, gifts: List["raw.base.StarGift"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None, attributes: Optional[List["raw.base.StarGiftAttribute"]] = None, attributes_hash: Optional[int] = None, counters: Optional[List["raw.base.StarGiftAttributeCounter"]] = None) -> None:
        self.count = count  # int
        self.gifts = gifts  # Vector<StarGift>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string
        self.attributes = attributes  # flags.1?Vector<StarGiftAttribute>
        self.attributes_hash = attributes_hash  # flags.1?long
        self.counters = counters  # flags.2?Vector<StarGiftAttributeCounter>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResaleStarGifts":

        flags = Int.read(b)

        count = Int.read(b)

        gifts = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        attributes = TLObject.read(b) if flags & (1 << 1) else []

        attributes_hash = Long.read(b) if flags & (1 << 1) else None
        chats = TLObject.read(b)

        counters = TLObject.read(b) if flags & (1 << 2) else []

        users = TLObject.read(b)

        return ResaleStarGifts(count=count, gifts=gifts, chats=chats, users=users, next_offset=next_offset, attributes=attributes, attributes_hash=attributes_hash, counters=counters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        flags |= (1 << 1) if self.attributes else 0
        flags |= (1 << 1) if self.attributes_hash is not None else 0
        flags |= (1 << 2) if self.counters else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Vector(self.gifts))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        if self.attributes is not None:
            b.write(Vector(self.attributes))

        if self.attributes_hash is not None:
            b.write(Long(self.attributes_hash))

        b.write(Vector(self.chats))

        if self.counters is not None:
            b.write(Vector(self.counters))

        b.write(Vector(self.users))

        return b.getvalue()
