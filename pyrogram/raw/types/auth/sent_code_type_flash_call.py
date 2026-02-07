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


class SentCodeTypeFlashCall(TLObject):  # type: ignore
    """The code will be sent via a flash phone call, that will be closed immediately. The phone code will then be the phone number itself, just make sure that the phone number matches the specified pattern.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``AB03C6D9``

    Parameters:
        pattern (``str``):
            pattern to match

    """

    __slots__: List[str] = ["pattern"]

    ID = 0xab03c6d9
    QUALNAME = "types.auth.SentCodeTypeFlashCall"

    def __init__(self, *, pattern: str) -> None:
        self.pattern = pattern  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeFlashCall":
        # No flags

        pattern = String.read(b)

        return SentCodeTypeFlashCall(pattern=pattern)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.pattern))

        return b.getvalue()
