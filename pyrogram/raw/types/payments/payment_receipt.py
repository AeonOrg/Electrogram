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


class PaymentReceipt(TLObject):  # type: ignore
    """Receipt

    Constructor of :obj:`~pyrogram.raw.base.payments.PaymentReceipt`.

    Details:
        - Layer: ``224``
        - ID: ``70C4FE03``

    Parameters:
        date (``int`` ``32-bit``):
            Date of generation

        bot_id (``int`` ``64-bit``):
            Bot ID

        provider_id (``int`` ``64-bit``):
            Provider ID

        title (``str``):
            Title

        description (``str``):
            Description

        invoice (:obj:`Invoice <pyrogram.raw.base.Invoice>`):
            Invoice

        currency (``str``):
            Three-letter ISO 4217 currency code

        total_amount (``int`` ``64-bit``):
            Total amount in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        credentials_title (``str``):
            Payment credential name

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users

        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            Photo

        info (:obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`, *optional*):
            Info

        shipping (:obj:`ShippingOption <pyrogram.raw.base.ShippingOption>`, *optional*):
            Selected shipping option

        tip_amount (``int`` ``64-bit``, *optional*):
            Tipped amount

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentReceipt
    """

    __slots__: List[str] = ["date", "bot_id", "provider_id", "title", "description", "invoice", "currency", "total_amount", "credentials_title", "users", "photo", "info", "shipping", "tip_amount"]

    ID = 0x70c4fe03
    QUALNAME = "types.payments.PaymentReceipt"

    def __init__(self, *, date: int, bot_id: int, provider_id: int, title: str, description: str, invoice: "raw.base.Invoice", currency: str, total_amount: int, credentials_title: str, users: List["raw.base.User"], photo: "raw.base.WebDocument" = None, info: "raw.base.PaymentRequestedInfo" = None, shipping: "raw.base.ShippingOption" = None, tip_amount: Optional[int] = None) -> None:
        self.date = date  # int
        self.bot_id = bot_id  # long
        self.provider_id = provider_id  # long
        self.title = title  # string
        self.description = description  # string
        self.invoice = invoice  # Invoice
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.credentials_title = credentials_title  # string
        self.users = users  # Vector<User>
        self.photo = photo  # flags.2?WebDocument
        self.info = info  # flags.0?PaymentRequestedInfo
        self.shipping = shipping  # flags.1?ShippingOption
        self.tip_amount = tip_amount  # flags.3?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentReceipt":

        flags = Int.read(b)

        date = Int.read(b)

        bot_id = Long.read(b)

        provider_id = Long.read(b)

        title = String.read(b)

        description = String.read(b)

        photo = TLObject.read(b) if flags & (1 << 2) else None

        invoice = TLObject.read(b)

        info = TLObject.read(b) if flags & (1 << 0) else None

        shipping = TLObject.read(b) if flags & (1 << 1) else None

        tip_amount = Long.read(b) if flags & (1 << 3) else None
        currency = String.read(b)

        total_amount = Long.read(b)

        credentials_title = String.read(b)

        users = TLObject.read(b)

        return PaymentReceipt(date=date, bot_id=bot_id, provider_id=provider_id, title=title, description=description, invoice=invoice, currency=currency, total_amount=total_amount, credentials_title=credentials_title, users=users, photo=photo, info=info, shipping=shipping, tip_amount=tip_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.photo is not None else 0
        flags |= (1 << 0) if self.info is not None else 0
        flags |= (1 << 1) if self.shipping is not None else 0
        flags |= (1 << 3) if self.tip_amount is not None else 0
        b.write(Int(flags))

        b.write(Int(self.date))

        b.write(Long(self.bot_id))

        b.write(Long(self.provider_id))

        b.write(String(self.title))

        b.write(String(self.description))

        if self.photo is not None:
            b.write(self.photo.write())

        b.write(self.invoice.write())

        if self.info is not None:
            b.write(self.info.write())

        if self.shipping is not None:
            b.write(self.shipping.write())

        if self.tip_amount is not None:
            b.write(Long(self.tip_amount))

        b.write(String(self.currency))

        b.write(Long(self.total_amount))

        b.write(String(self.credentials_title))

        b.write(Vector(self.users))

        return b.getvalue()
