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


class StarsGiftOption(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsGiftOption`.

    Details:
        - Layer: ``224``
        - ID: ``5E0589F1``

    Parameters:
        stars (``int`` ``64-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        extended (``bool``, *optional*):
            N/A

        store_product (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarsGiftOptions
    """

    __slots__: List[str] = ["stars", "currency", "amount", "extended", "store_product"]

    ID = 0x5e0589f1
    QUALNAME = "types.StarsGiftOption"

    def __init__(self, *, stars: int, currency: str, amount: int, extended: Optional[bool] = None, store_product: Optional[str] = None) -> None:
        self.stars = stars  # long
        self.currency = currency  # string
        self.amount = amount  # long
        self.extended = extended  # flags.1?true
        self.store_product = store_product  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsGiftOption":

        flags = Int.read(b)

        extended = True if flags & (1 << 1) else False
        stars = Long.read(b)

        store_product = String.read(b) if flags & (1 << 0) else None
        currency = String.read(b)

        amount = Long.read(b)

        return StarsGiftOption(stars=stars, currency=currency, amount=amount, extended=extended, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.extended else 0
        flags |= (1 << 0) if self.store_product is not None else 0
        b.write(Int(flags))

        b.write(Long(self.stars))

        if self.store_product is not None:
            b.write(String(self.store_product))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        return b.getvalue()
