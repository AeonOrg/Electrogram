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


class PageBlockTitle(TLObject):  # type: ignore
    """Title

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``70ABC3FD``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Title

    """

    __slots__: List[str] = ["text"]

    ID = 0x70abc3fd
    QUALNAME = "types.PageBlockTitle"

    def __init__(self, *, text: "raw.base.RichText") -> None:
        self.text = text  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockTitle":
        # No flags

        text = TLObject.read(b)

        return PageBlockTitle(text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.text.write())

        return b.getvalue()
