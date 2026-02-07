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


class PageBlockParagraph(TLObject):  # type: ignore
    """A paragraph

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``467A0766``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Text

    """

    __slots__: List[str] = ["text"]

    ID = 0x467a0766
    QUALNAME = "types.PageBlockParagraph"

    def __init__(self, *, text: "raw.base.RichText") -> None:
        self.text = text  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockParagraph":
        # No flags

        text = TLObject.read(b)

        return PageBlockParagraph(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.text.write())

        return b.getvalue()
