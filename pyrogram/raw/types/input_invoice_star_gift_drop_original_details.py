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


class InputInvoiceStarGiftDropOriginalDetails(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``923D8D1``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

    """

    __slots__: List[str] = ["stargift"]

    ID = 0x923d8d1
    QUALNAME = "types.InputInvoiceStarGiftDropOriginalDetails"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift") -> None:
        self.stargift = stargift  # InputSavedStarGift

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftDropOriginalDetails":
        # No flags

        stargift = TLObject.read(b)

        return InputInvoiceStarGiftDropOriginalDetails(stargift=stargift)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.stargift.write())

        return b.getvalue()
