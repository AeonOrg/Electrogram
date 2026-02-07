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


class ConvertStarGift(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``74BF076B``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["stargift"]

    ID = 0x74bf076b
    QUALNAME = "functions.payments.ConvertStarGift"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift") -> None:
        self.stargift = stargift  # InputSavedStarGift

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConvertStarGift":
        # No flags

        stargift = TLObject.read(b)

        return ConvertStarGift(stargift=stargift)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.stargift.write())

        return b.getvalue()
