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


class GetUniqueStarGiftValueInfo(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4365AF6B``

    Parameters:
        slug (``str``):
            N/A

    Returns:
        :obj:`payments.UniqueStarGiftValueInfo <pyrogram.raw.base.payments.UniqueStarGiftValueInfo>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0x4365af6b
    QUALNAME = "functions.payments.GetUniqueStarGiftValueInfo"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUniqueStarGiftValueInfo":
        # No flags

        slug = String.read(b)

        return GetUniqueStarGiftValueInfo(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.slug))

        return b.getvalue()
