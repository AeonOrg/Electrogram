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


class StarsRevenueWithdrawalUrl(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarsRevenueWithdrawalUrl`.

    Details:
        - Layer: ``224``
        - ID: ``1DAB80B7``

    Parameters:
        url (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarsRevenueWithdrawalUrl
    """

    __slots__: List[str] = ["url"]

    ID = 0x1dab80b7
    QUALNAME = "types.payments.StarsRevenueWithdrawalUrl"

    def __init__(self, *, url: str) -> None:
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsRevenueWithdrawalUrl":
        # No flags

        url = String.read(b)

        return StarsRevenueWithdrawalUrl(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        return b.getvalue()
