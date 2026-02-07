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


class SecurePlainPhone(TLObject):  # type: ignore
    """Phone number to use in telegram passport: it must be verified, first ».

    Constructor of :obj:`~pyrogram.raw.base.SecurePlainData`.

    Details:
        - Layer: ``224``
        - ID: ``7D6099DD``

    Parameters:
        phone (``str``):
            Phone number

    """

    __slots__: List[str] = ["phone"]

    ID = 0x7d6099dd
    QUALNAME = "types.SecurePlainPhone"

    def __init__(self, *, phone: str) -> None:
        self.phone = phone  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePlainPhone":
        # No flags

        phone = String.read(b)

        return SecurePlainPhone(phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.phone))

        return b.getvalue()
