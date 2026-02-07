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


class ResetPassword(TLObject):  # type: ignore
    """Initiate a 2FA password reset: can only be used if the user is already logged-in, see here for more info »


    Details:
        - Layer: ``224``
        - ID: ``9308CE1B``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.ResetPasswordResult <pyrogram.raw.base.account.ResetPasswordResult>`
    """

    __slots__: List[str] = []

    ID = 0x9308ce1b
    QUALNAME = "functions.account.ResetPassword"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPassword":
        # No flags

        return ResetPassword()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
