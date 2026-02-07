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


class PageCaption(TLObject):  # type: ignore
    """Page caption

    Constructor of :obj:`~pyrogram.raw.base.PageCaption`.

    Details:
        - Layer: ``224``
        - ID: ``6F747657``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Caption

        credit (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Credits

    """

    __slots__: List[str] = ["text", "credit"]

    ID = 0x6f747657
    QUALNAME = "types.PageCaption"

    def __init__(self, *, text: "raw.base.RichText", credit: "raw.base.RichText") -> None:
        self.text = text  # RichText
        self.credit = credit  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageCaption":
        # No flags

        text = TLObject.read(b)

        credit = TLObject.read(b)

        return PageCaption(text=text, credit=credit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.text.write())

        b.write(self.credit.write())

        return b.getvalue()
