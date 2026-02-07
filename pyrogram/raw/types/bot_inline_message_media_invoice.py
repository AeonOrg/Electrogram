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


class BotInlineMessageMediaInvoice(TLObject):  # type: ignore
    """Send an invoice

    Constructor of :obj:`~pyrogram.raw.base.BotInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``354A9B09``

    Parameters:
        title (``str``):
            Product name, 1-32 characters

        description (``str``):
            Product description, 1-255 characters

        currency (``str``):
            Three-letter ISO 4217 currency code

        total_amount (``int`` ``64-bit``):
            Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        shipping_address_requested (``bool``, *optional*):
            Set this flag if you require the user's shipping address to complete the order

        test (``bool``, *optional*):
            Test invoice

        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            Product photo

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Inline keyboard

    """

    __slots__: List[str] = ["title", "description", "currency", "total_amount", "shipping_address_requested", "test", "photo", "reply_markup"]

    ID = 0x354a9b09
    QUALNAME = "types.BotInlineMessageMediaInvoice"

    def __init__(self, *, title: str, description: str, currency: str, total_amount: int, shipping_address_requested: Optional[bool] = None, test: Optional[bool] = None, photo: "raw.base.WebDocument" = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.shipping_address_requested = shipping_address_requested  # flags.1?true
        self.test = test  # flags.3?true
        self.photo = photo  # flags.0?WebDocument
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageMediaInvoice":

        flags = Int.read(b)

        shipping_address_requested = True if flags & (1 << 1) else False
        test = True if flags & (1 << 3) else False
        title = String.read(b)

        description = String.read(b)

        photo = TLObject.read(b) if flags & (1 << 0) else None

        currency = String.read(b)

        total_amount = Long.read(b)

        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        return BotInlineMessageMediaInvoice(title=title, description=description, currency=currency, total_amount=total_amount, shipping_address_requested=shipping_address_requested, test=test, photo=photo, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.shipping_address_requested else 0
        flags |= (1 << 3) if self.test else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))

        b.write(String(self.title))

        b.write(String(self.description))

        if self.photo is not None:
            b.write(self.photo.write())

        b.write(String(self.currency))

        b.write(Long(self.total_amount))

        if self.reply_markup is not None:
            b.write(self.reply_markup.write())

        return b.getvalue()
