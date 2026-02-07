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


class ResetWebAuthorization(TLObject):  # type: ignore
    """Log out an active web telegram login session


    Details:
        - Layer: ``224``
        - ID: ``2D01B9EF``

    Parameters:
        hash (``int`` ``64-bit``):
            Session hash

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["hash"]

    ID = 0x2d01b9ef
    QUALNAME = "functions.account.ResetWebAuthorization"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetWebAuthorization":
        # No flags

        hash = Long.read(b)

        return ResetWebAuthorization(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        return b.getvalue()
