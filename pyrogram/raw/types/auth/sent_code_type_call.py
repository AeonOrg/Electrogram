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


class SentCodeTypeCall(TLObject):  # type: ignore
    """The code will be sent via a phone call: a synthesized voice will tell the user which verification code to input.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``5353E5A7``

    Parameters:
        length (``int`` ``32-bit``):
            Length of the verification code

    """

    __slots__: List[str] = ["length"]

    ID = 0x5353e5a7
    QUALNAME = "types.auth.SentCodeTypeCall"

    def __init__(self, *, length: int) -> None:
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeCall":
        # No flags

        length = Int.read(b)

        return SentCodeTypeCall(length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.length))

        return b.getvalue()
