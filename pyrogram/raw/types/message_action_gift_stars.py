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


class MessageActionGiftStars(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``45D5B021``

    Parameters:
        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        stars (``int`` ``64-bit``):
            N/A

        crypto_currency (``str``, *optional*):
            N/A

        crypto_amount (``int`` ``64-bit``, *optional*):
            N/A

        transaction_id (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["currency", "amount", "stars", "crypto_currency", "crypto_amount", "transaction_id"]

    ID = 0x45d5b021
    QUALNAME = "types.MessageActionGiftStars"

    def __init__(self, *, currency: str, amount: int, stars: int, crypto_currency: Optional[str] = None, crypto_amount: Optional[int] = None, transaction_id: Optional[str] = None) -> None:
        self.currency = currency  # string
        self.amount = amount  # long
        self.stars = stars  # long
        self.crypto_currency = crypto_currency  # flags.0?string
        self.crypto_amount = crypto_amount  # flags.0?long
        self.transaction_id = transaction_id  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiftStars":

        flags = Int.read(b)

        currency = String.read(b)

        amount = Long.read(b)

        stars = Long.read(b)

        crypto_currency = String.read(b) if flags & (1 << 0) else None
        crypto_amount = Long.read(b) if flags & (1 << 0) else None
        transaction_id = String.read(b) if flags & (1 << 1) else None
        return MessageActionGiftStars(currency=currency, amount=amount, stars=stars, crypto_currency=crypto_currency, crypto_amount=crypto_amount, transaction_id=transaction_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.crypto_currency is not None else 0
        flags |= (1 << 0) if self.crypto_amount is not None else 0
        flags |= (1 << 1) if self.transaction_id is not None else 0
        b.write(Int(flags))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        b.write(Long(self.stars))

        if self.crypto_currency is not None:
            b.write(String(self.crypto_currency))

        if self.crypto_amount is not None:
            b.write(Long(self.crypto_amount))

        if self.transaction_id is not None:
            b.write(String(self.transaction_id))

        return b.getvalue()
