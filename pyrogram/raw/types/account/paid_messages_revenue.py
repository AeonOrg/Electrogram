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


class PaidMessagesRevenue(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.PaidMessagesRevenue`.

    Details:
        - Layer: ``224``
        - ID: ``1E109708``

    Parameters:
        stars_amount (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPaidMessagesRevenue
    """

    __slots__: List[str] = ["stars_amount"]

    ID = 0x1e109708
    QUALNAME = "types.account.PaidMessagesRevenue"

    def __init__(self, *, stars_amount: int) -> None:
        self.stars_amount = stars_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaidMessagesRevenue":
        # No flags

        stars_amount = Long.read(b)

        return PaidMessagesRevenue(stars_amount=stars_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.stars_amount))

        return b.getvalue()
