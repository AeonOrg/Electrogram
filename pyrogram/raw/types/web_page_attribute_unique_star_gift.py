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


class WebPageAttributeUniqueStarGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPageAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``CF6F6DB8``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

    """

    __slots__: List[str] = ["gift"]

    ID = 0xcf6f6db8
    QUALNAME = "types.WebPageAttributeUniqueStarGift"

    def __init__(self, *, gift: "raw.base.StarGift") -> None:
        self.gift = gift  # StarGift

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageAttributeUniqueStarGift":
        # No flags

        gift = TLObject.read(b)

        return WebPageAttributeUniqueStarGift(gift=gift)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.gift.write())

        return b.getvalue()
