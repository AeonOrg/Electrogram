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


class InputStorePaymentStarsGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``1D741EF7``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        stars (``int`` ``64-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "stars", "currency", "amount"]

    ID = 0x1d741ef7
    QUALNAME = "types.InputStorePaymentStarsGift"

    def __init__(self, *, user_id: "raw.base.InputUser", stars: int, currency: str, amount: int) -> None:
        self.user_id = user_id  # InputUser
        self.stars = stars  # long
        self.currency = currency  # string
        self.amount = amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentStarsGift":
        # No flags

        user_id = TLObject.read(b)

        stars = Long.read(b)

        currency = String.read(b)

        amount = Long.read(b)

        return InputStorePaymentStarsGift(user_id=user_id, stars=stars, currency=currency, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.user_id.write())

        b.write(Long(self.stars))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        return b.getvalue()
