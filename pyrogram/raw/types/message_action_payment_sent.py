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


class MessageActionPaymentSent(TLObject):  # type: ignore
    """A payment was sent

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``C624B16E``

    Parameters:
        currency (``str``):
            Three-letter ISO 4217 currency code

        total_amount (``int`` ``64-bit``):
            Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        recurring_init (``bool``, *optional*):
            Whether this is the first payment of a recurring payment we just subscribed to

        recurring_used (``bool``, *optional*):
            Whether this payment is part of a recurring payment

        invoice_slug (``str``, *optional*):
            An invoice slug taken from an invoice deep link or from the premium_invoice_slug app config parameter »

        subscription_until_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["currency", "total_amount", "recurring_init", "recurring_used", "invoice_slug", "subscription_until_date"]

    ID = 0xc624b16e
    QUALNAME = "types.MessageActionPaymentSent"

    def __init__(self, *, currency: str, total_amount: int, recurring_init: Optional[bool] = None, recurring_used: Optional[bool] = None, invoice_slug: Optional[str] = None, subscription_until_date: Optional[int] = None) -> None:
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.recurring_init = recurring_init  # flags.2?true
        self.recurring_used = recurring_used  # flags.3?true
        self.invoice_slug = invoice_slug  # flags.0?string
        self.subscription_until_date = subscription_until_date  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaymentSent":

        flags = Int.read(b)

        recurring_init = True if flags & (1 << 2) else False
        recurring_used = True if flags & (1 << 3) else False
        currency = String.read(b)

        total_amount = Long.read(b)

        invoice_slug = String.read(b) if flags & (1 << 0) else None
        subscription_until_date = Int.read(b) if flags & (1 << 4) else None
        return MessageActionPaymentSent(currency=currency, total_amount=total_amount, recurring_init=recurring_init, recurring_used=recurring_used, invoice_slug=invoice_slug, subscription_until_date=subscription_until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.recurring_init else 0
        flags |= (1 << 3) if self.recurring_used else 0
        flags |= (1 << 0) if self.invoice_slug is not None else 0
        flags |= (1 << 4) if self.subscription_until_date is not None else 0
        b.write(Int(flags))

        b.write(String(self.currency))

        b.write(Long(self.total_amount))

        if self.invoice_slug is not None:
            b.write(String(self.invoice_slug))

        if self.subscription_until_date is not None:
            b.write(Int(self.subscription_until_date))

        return b.getvalue()
