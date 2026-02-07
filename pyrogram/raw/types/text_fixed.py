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


class TextFixed(TLObject):  # type: ignore
    """fixed-width rich text

    Constructor of :obj:`~pyrogram.raw.base.RichText`.

    Details:
        - Layer: ``224``
        - ID: ``6C3F19B9``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Text

    """

    __slots__: List[str] = ["text"]

    ID = 0x6c3f19b9
    QUALNAME = "types.TextFixed"

    def __init__(self, *, text: "raw.base.RichText") -> None:
        self.text = text  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextFixed":
        # No flags

        text = TLObject.read(b)

        return TextFixed(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.text.write())

        return b.getvalue()
