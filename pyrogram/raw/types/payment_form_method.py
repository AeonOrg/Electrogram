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


class PaymentFormMethod(TLObject):  # type: ignore
    """Represents an additional payment method

    Constructor of :obj:`~pyrogram.raw.base.PaymentFormMethod`.

    Details:
        - Layer: ``224``
        - ID: ``88F8F21B``

    Parameters:
        url (``str``):
            URL to open in a webview to process the payment

        title (``str``):
            Payment method description

    """

    __slots__: List[str] = ["url", "title"]

    ID = 0x88f8f21b
    QUALNAME = "types.PaymentFormMethod"

    def __init__(self, *, url: str, title: str) -> None:
        self.url = url  # string
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentFormMethod":
        # No flags

        url = String.read(b)

        title = String.read(b)

        return PaymentFormMethod(url=url, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(String(self.title))

        return b.getvalue()
