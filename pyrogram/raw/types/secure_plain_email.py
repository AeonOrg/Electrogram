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


class SecurePlainEmail(TLObject):  # type: ignore
    """Email address to use in telegram passport: it must be verified, first ».

    Constructor of :obj:`~pyrogram.raw.base.SecurePlainData`.

    Details:
        - Layer: ``224``
        - ID: ``21EC5A5F``

    Parameters:
        email (``str``):
            Email address

    """

    __slots__: List[str] = ["email"]

    ID = 0x21ec5a5f
    QUALNAME = "types.SecurePlainEmail"

    def __init__(self, *, email: str) -> None:
        self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePlainEmail":
        # No flags

        email = String.read(b)

        return SecurePlainEmail(email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.email))

        return b.getvalue()
