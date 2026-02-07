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


class MessageActionStarGiftPurchaseOfferDeclined(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``73ADA76B``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        price (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

        expired (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["gift", "price", "expired"]

    ID = 0x73ada76b
    QUALNAME = "types.MessageActionStarGiftPurchaseOfferDeclined"

    def __init__(self, *, gift: "raw.base.StarGift", price: "raw.base.StarsAmount", expired: Optional[bool] = None) -> None:
        self.gift = gift  # StarGift
        self.price = price  # StarsAmount
        self.expired = expired  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionStarGiftPurchaseOfferDeclined":

        flags = Int.read(b)

        expired = True if flags & (1 << 0) else False
        gift = TLObject.read(b)

        price = TLObject.read(b)

        return MessageActionStarGiftPurchaseOfferDeclined(gift=gift, price=price, expired=expired)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.expired else 0
        b.write(Int(flags))

        b.write(self.gift.write())

        b.write(self.price.write())

        return b.getvalue()
