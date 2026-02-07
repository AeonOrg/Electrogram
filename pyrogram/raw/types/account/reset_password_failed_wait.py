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


class ResetPasswordFailedWait(TLObject):  # type: ignore
    """You recently requested a password reset that was canceled, please wait until the specified date before requesting another reset.

    Constructor of :obj:`~pyrogram.raw.base.account.ResetPasswordResult`.

    Details:
        - Layer: ``224``
        - ID: ``E3779861``

    Parameters:
        retry_date (``int`` ``32-bit``):
            Wait until this date before requesting another reset.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    __slots__: List[str] = ["retry_date"]

    ID = 0xe3779861
    QUALNAME = "types.account.ResetPasswordFailedWait"

    def __init__(self, *, retry_date: int) -> None:
        self.retry_date = retry_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPasswordFailedWait":
        # No flags

        retry_date = Int.read(b)

        return ResetPasswordFailedWait(retry_date=retry_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.retry_date))

        return b.getvalue()
