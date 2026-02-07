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


class SentCodeTypeSmsWord(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``A416AC81``

    Parameters:
        beginning (``str``, *optional*):


    """

    __slots__: List[str] = ["beginning"]

    ID = 0xa416ac81
    QUALNAME = "types.auth.SentCodeTypeSmsWord"

    def __init__(self, *, beginning: Optional[str] = None) -> None:
        self.beginning = beginning  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeSmsWord":

        flags = Int.read(b)

        beginning = String.read(b) if flags & (1 << 0) else None
        return SentCodeTypeSmsWord(beginning=beginning)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.beginning is not None else 0
        b.write(Int(flags))

        if self.beginning is not None:
            b.write(String(self.beginning))

        return b.getvalue()
