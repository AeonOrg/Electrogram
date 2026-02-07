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


class TextPlain(TLObject):  # type: ignore
    """Plain text

    Constructor of :obj:`~pyrogram.raw.base.RichText`.

    Details:
        - Layer: ``224``
        - ID: ``744694E0``

    Parameters:
        text (``str``):
            Text

    """

    __slots__: List[str] = ["text"]

    ID = 0x744694e0
    QUALNAME = "types.TextPlain"

    def __init__(self, *, text: str) -> None:
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextPlain":
        # No flags

        text = String.read(b)

        return TextPlain(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.text))

        return b.getvalue()
