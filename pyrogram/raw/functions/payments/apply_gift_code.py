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


class ApplyGiftCode(TLObject):  # type: ignore
    """Apply a Telegram Premium giftcode »


    Details:
        - Layer: ``224``
        - ID: ``F6E26854``

    Parameters:
        slug (``str``):
            The code to apply

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0xf6e26854
    QUALNAME = "functions.payments.ApplyGiftCode"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ApplyGiftCode":
        # No flags

        slug = String.read(b)

        return ApplyGiftCode(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.slug))

        return b.getvalue()
