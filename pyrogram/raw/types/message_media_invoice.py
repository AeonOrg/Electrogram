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


class MessageMediaInvoice(TLObject):  # type: ignore
    """Invoice

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``F6A548D3``

    Parameters:
        title (``str``):
            Product name, 1-32 characters

        description (``str``):
            Product description, 1-255 characters

        currency (``str``):
            Three-letter ISO 4217 currency code

        total_amount (``int`` ``64-bit``):
            Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        start_param (``str``):
            Unique bot deep-linking parameter that can be used to generate this invoice

        shipping_address_requested (``bool``, *optional*):
            Whether the shipping address was requested

        test (``bool``, *optional*):
            Whether this is an example invoice

        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.

        receipt_msg_id (``int`` ``32-bit``, *optional*):
            Message ID of receipt: if set, clients should change the text of the first keyboardButtonBuy button always attached to the message to a localized version of the word Receipt

        extended_media (:obj:`MessageExtendedMedia <pyrogram.raw.base.MessageExtendedMedia>`, *optional*):
            Extended media

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["title", "description", "currency", "total_amount", "start_param", "shipping_address_requested", "test", "photo", "receipt_msg_id", "extended_media"]

    ID = 0xf6a548d3
    QUALNAME = "types.MessageMediaInvoice"

    def __init__(self, *, title: str, description: str, currency: str, total_amount: int, start_param: str, shipping_address_requested: Optional[bool] = None, test: Optional[bool] = None, photo: "raw.base.WebDocument" = None, receipt_msg_id: Optional[int] = None, extended_media: "raw.base.MessageExtendedMedia" = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.start_param = start_param  # string
        self.shipping_address_requested = shipping_address_requested  # flags.1?true
        self.test = test  # flags.3?true
        self.photo = photo  # flags.0?WebDocument
        self.receipt_msg_id = receipt_msg_id  # flags.2?int
        self.extended_media = extended_media  # flags.4?MessageExtendedMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaInvoice":

        flags = Int.read(b)

        shipping_address_requested = True if flags & (1 << 1) else False
        test = True if flags & (1 << 3) else False
        title = String.read(b)

        description = String.read(b)

        photo = TLObject.read(b) if flags & (1 << 0) else None

        receipt_msg_id = Int.read(b) if flags & (1 << 2) else None
        currency = String.read(b)

        total_amount = Long.read(b)

        start_param = String.read(b)

        extended_media = TLObject.read(b) if flags & (1 << 4) else None

        return MessageMediaInvoice(title=title, description=description, currency=currency, total_amount=total_amount, start_param=start_param, shipping_address_requested=shipping_address_requested, test=test, photo=photo, receipt_msg_id=receipt_msg_id, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.shipping_address_requested else 0
        flags |= (1 << 3) if self.test else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.receipt_msg_id is not None else 0
        flags |= (1 << 4) if self.extended_media is not None else 0
        b.write(Int(flags))

        b.write(String(self.title))

        b.write(String(self.description))

        if self.photo is not None:
            b.write(self.photo.write())

        if self.receipt_msg_id is not None:
            b.write(Int(self.receipt_msg_id))

        b.write(String(self.currency))

        b.write(Long(self.total_amount))

        b.write(String(self.start_param))

        if self.extended_media is not None:
            b.write(self.extended_media.write())

        return b.getvalue()
