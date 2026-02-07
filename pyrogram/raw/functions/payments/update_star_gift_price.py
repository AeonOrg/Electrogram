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


class UpdateStarGiftPrice(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EDBE6CCB``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

        resell_amount (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["stargift", "resell_amount"]

    ID = 0xedbe6ccb
    QUALNAME = "functions.payments.UpdateStarGiftPrice"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift", resell_amount: "raw.base.StarsAmount") -> None:
        self.stargift = stargift  # InputSavedStarGift
        self.resell_amount = resell_amount  # StarsAmount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarGiftPrice":
        # No flags

        stargift = TLObject.read(b)

        resell_amount = TLObject.read(b)

        return UpdateStarGiftPrice(stargift=stargift, resell_amount=resell_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.stargift.write())

        b.write(self.resell_amount.write())

        return b.getvalue()
