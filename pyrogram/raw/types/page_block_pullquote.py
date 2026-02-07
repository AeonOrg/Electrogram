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


class PageBlockPullquote(TLObject):  # type: ignore
    """Pullquote

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``4F4456D3``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Text

        caption (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Caption

    """

    __slots__: List[str] = ["text", "caption"]

    ID = 0x4f4456d3
    QUALNAME = "types.PageBlockPullquote"

    def __init__(self, *, text: "raw.base.RichText", caption: "raw.base.RichText") -> None:
        self.text = text  # RichText
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockPullquote":
        # No flags

        text = TLObject.read(b)

        caption = TLObject.read(b)

        return PageBlockPullquote(text=text, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.text.write())

        b.write(self.caption.write())

        return b.getvalue()
