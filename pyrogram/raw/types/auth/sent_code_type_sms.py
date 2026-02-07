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


class SentCodeTypeSms(TLObject):  # type: ignore
    """The code was sent via SMS

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``C000BBA2``

    Parameters:
        length (``int`` ``32-bit``):
            Length of the code in bytes

    """

    __slots__: List[str] = ["length"]

    ID = 0xc000bba2
    QUALNAME = "types.auth.SentCodeTypeSms"

    def __init__(self, *, length: int) -> None:
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeSms":
        # No flags

        length = Int.read(b)

        return SentCodeTypeSms(length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.length))

        return b.getvalue()
