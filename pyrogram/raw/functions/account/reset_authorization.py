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


class ResetAuthorization(TLObject):  # type: ignore
    """Log out an active authorized session by its hash


    Details:
        - Layer: ``224``
        - ID: ``DF77F3BC``

    Parameters:
        hash (``int`` ``64-bit``):
            Session hash

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["hash"]

    ID = 0xdf77f3bc
    QUALNAME = "functions.account.ResetAuthorization"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetAuthorization":
        # No flags

        hash = Long.read(b)

        return ResetAuthorization(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        return b.getvalue()
