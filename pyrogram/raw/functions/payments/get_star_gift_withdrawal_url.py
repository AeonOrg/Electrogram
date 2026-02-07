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


class GetStarGiftWithdrawalUrl(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D06E93A8``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            N/A

    Returns:
        :obj:`payments.StarGiftWithdrawalUrl <pyrogram.raw.base.payments.StarGiftWithdrawalUrl>`
    """

    __slots__: List[str] = ["stargift", "password"]

    ID = 0xd06e93a8
    QUALNAME = "functions.payments.GetStarGiftWithdrawalUrl"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift", password: "raw.base.InputCheckPasswordSRP") -> None:
        self.stargift = stargift  # InputSavedStarGift
        self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarGiftWithdrawalUrl":
        # No flags

        stargift = TLObject.read(b)

        password = TLObject.read(b)

        return GetStarGiftWithdrawalUrl(stargift=stargift, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.stargift.write())

        b.write(self.password.write())

        return b.getvalue()
