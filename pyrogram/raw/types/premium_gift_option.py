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


class PremiumGiftOption(TLObject):  # type: ignore
    """Telegram Premium gift option

    Constructor of :obj:`~pyrogram.raw.base.PremiumGiftOption`.

    Details:
        - Layer: ``224``
        - ID: ``79C059F7``

    Parameters:
        months (``int`` ``32-bit``):
            Duration of gifted Telegram Premium subscription

        currency (``str``):
            Three-letter ISO 4217 currency code

        amount (``int`` ``64-bit``):
            Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        bot_url (``str``, *optional*):
            An invoice deep link » to an invoice for in-app payment, using the official Premium bot; may be empty if direct payment isn't available.

        store_product (``str``, *optional*):
            An identifier for the App Store/Play Store product associated with the Premium gift.

    """

    __slots__: List[str] = ["months", "currency", "amount", "bot_url", "store_product"]

    ID = 0x79c059f7
    QUALNAME = "types.PremiumGiftOption"

    def __init__(self, *, months: int, currency: str, amount: int, bot_url: Optional[str] = None, store_product: Optional[str] = None) -> None:
        self.months = months  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.bot_url = bot_url  # flags.1?string
        self.store_product = store_product  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumGiftOption":

        flags = Int.read(b)

        months = Int.read(b)

        currency = String.read(b)

        amount = Long.read(b)

        bot_url = String.read(b) if flags & (1 << 1) else None
        store_product = String.read(b) if flags & (1 << 0) else None
        return PremiumGiftOption(months=months, currency=currency, amount=amount, bot_url=bot_url, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.bot_url is not None else 0
        flags |= (1 << 0) if self.store_product is not None else 0
        b.write(Int(flags))

        b.write(Int(self.months))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        if self.bot_url is not None:
            b.write(String(self.bot_url))

        if self.store_product is not None:
            b.write(String(self.store_product))

        return b.getvalue()
