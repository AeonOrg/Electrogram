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


class PageBlockPreformatted(TLObject):  # type: ignore
    """Preformatted (<pre> text)

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``C070D93E``

    Parameters:
        text (:obj:`RichText <pyrogram.raw.base.RichText>`):
            Text

        language (``str``):
            Programming language of preformatted text

    """

    __slots__: List[str] = ["text", "language"]

    ID = 0xc070d93e
    QUALNAME = "types.PageBlockPreformatted"

    def __init__(self, *, text: "raw.base.RichText", language: str) -> None:
        self.text = text  # RichText
        self.language = language  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockPreformatted":
        # No flags

        text = TLObject.read(b)

        language = String.read(b)

        return PageBlockPreformatted(text=text, language=language)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.text.write())

        b.write(String(self.language))

        return b.getvalue()
