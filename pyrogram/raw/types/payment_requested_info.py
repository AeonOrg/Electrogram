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


class PaymentRequestedInfo(TLObject):  # type: ignore
    """Order info provided by the user

    Constructor of :obj:`~pyrogram.raw.base.PaymentRequestedInfo`.

    Details:
        - Layer: ``224``
        - ID: ``909C3F94``

    Parameters:
        name (``str``, *optional*):
            User's full name

        phone (``str``, *optional*):
            User's phone number

        email (``str``, *optional*):
            User's email address

        shipping_address (:obj:`PostAddress <pyrogram.raw.base.PostAddress>`, *optional*):
            User's shipping address

    """

    __slots__: List[str] = ["name", "phone", "email", "shipping_address"]

    ID = 0x909c3f94
    QUALNAME = "types.PaymentRequestedInfo"

    def __init__(self, *, name: Optional[str] = None, phone: Optional[str] = None, email: Optional[str] = None, shipping_address: "raw.base.PostAddress" = None) -> None:
        self.name = name  # flags.0?string
        self.phone = phone  # flags.1?string
        self.email = email  # flags.2?string
        self.shipping_address = shipping_address  # flags.3?PostAddress

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentRequestedInfo":

        flags = Int.read(b)

        name = String.read(b) if flags & (1 << 0) else None
        phone = String.read(b) if flags & (1 << 1) else None
        email = String.read(b) if flags & (1 << 2) else None
        shipping_address = TLObject.read(b) if flags & (1 << 3) else None

        return PaymentRequestedInfo(name=name, phone=phone, email=email, shipping_address=shipping_address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.name is not None else 0
        flags |= (1 << 1) if self.phone is not None else 0
        flags |= (1 << 2) if self.email is not None else 0
        flags |= (1 << 3) if self.shipping_address is not None else 0
        b.write(Int(flags))

        if self.name is not None:
            b.write(String(self.name))

        if self.phone is not None:
            b.write(String(self.phone))

        if self.email is not None:
            b.write(String(self.email))

        if self.shipping_address is not None:
            b.write(self.shipping_address.write())

        return b.getvalue()
