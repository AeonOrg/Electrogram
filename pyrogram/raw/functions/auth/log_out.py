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


class LogOut(TLObject):  # type: ignore
    """Logs out the user.


    Details:
        - Layer: ``224``
        - ID: ``3E72BA19``

    Parameters:
        No parameters required.

    Returns:
        :obj:`auth.LoggedOut <pyrogram.raw.base.auth.LoggedOut>`
    """

    __slots__: List[str] = []

    ID = 0x3e72ba19
    QUALNAME = "functions.auth.LogOut"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LogOut":
        # No flags

        return LogOut()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
