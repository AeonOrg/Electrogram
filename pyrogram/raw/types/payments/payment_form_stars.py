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


class PaymentFormStars(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.payments.PaymentForm`.

    Details:
        - Layer: ``224``
        - ID: ``7BF6B15C``

    Parameters:
        form_id (``int`` ``64-bit``):


        bot_id (``int`` ``64-bit``):


        title (``str``):


        description (``str``):


        invoice (:obj:`Invoice <pyrogram.raw.base.Invoice>`):


        users (List of :obj:`User <pyrogram.raw.base.User>`):


        can_save_credentials (``bool``, *optional*):
            N/A

        password_missing (``bool``, *optional*):
            N/A

        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):


    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentForm
    """

    __slots__: List[str] = ["form_id", "bot_id", "title", "description", "invoice", "users", "can_save_credentials", "password_missing", "photo"]

    ID = 0x7bf6b15c
    QUALNAME = "types.payments.PaymentFormStars"

    def __init__(self, *, form_id: int, bot_id: int, title: str, description: str, invoice: "raw.base.Invoice", users: List["raw.base.User"], can_save_credentials: Optional[bool] = None, password_missing: Optional[bool] = None, photo: "raw.base.WebDocument" = None) -> None:
        self.form_id = form_id  # long
        self.bot_id = bot_id  # long
        self.title = title  # string
        self.description = description  # string
        self.invoice = invoice  # Invoice
        self.users = users  # Vector<User>
        self.can_save_credentials = can_save_credentials  # flags.2?true
        self.password_missing = password_missing  # flags.3?true
        self.photo = photo  # flags.5?WebDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentFormStars":

        flags = Int.read(b)

        can_save_credentials = True if flags & (1 << 2) else False
        password_missing = True if flags & (1 << 3) else False
        form_id = Long.read(b)

        bot_id = Long.read(b)

        title = String.read(b)

        description = String.read(b)

        photo = TLObject.read(b) if flags & (1 << 5) else None

        invoice = TLObject.read(b)

        users = TLObject.read(b)

        return PaymentFormStars(form_id=form_id, bot_id=bot_id, title=title, description=description, invoice=invoice, users=users, can_save_credentials=can_save_credentials, password_missing=password_missing, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.can_save_credentials else 0
        flags |= (1 << 3) if self.password_missing else 0
        flags |= (1 << 5) if self.photo is not None else 0
        b.write(Int(flags))

        b.write(Long(self.form_id))

        b.write(Long(self.bot_id))

        b.write(String(self.title))

        b.write(String(self.description))

        if self.photo is not None:
            b.write(self.photo.write())

        b.write(self.invoice.write())

        b.write(Vector(self.users))

        return b.getvalue()
