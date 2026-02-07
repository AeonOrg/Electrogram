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


class PaymentSavedCredentialsCard(TLObject):  # type: ignore
    """Saved credit card

    Constructor of :obj:`~pyrogram.raw.base.PaymentSavedCredentials`.

    Details:
        - Layer: ``224``
        - ID: ``CDC27A1F``

    Parameters:
        id (``str``):
            Card ID

        title (``str``):
            Title

    """

    __slots__: List[str] = ["id", "title"]

    ID = 0xcdc27a1f
    QUALNAME = "types.PaymentSavedCredentialsCard"

    def __init__(self, *, id: str, title: str) -> None:
        self.id = id  # string
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentSavedCredentialsCard":
        # No flags

        id = String.read(b)

        title = String.read(b)

        return PaymentSavedCredentialsCard(id=id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.id))

        b.write(String(self.title))

        return b.getvalue()
