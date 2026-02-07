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


class DocumentAttributeImageSize(TLObject):  # type: ignore
    """Defines the width and height of an image uploaded as document

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``6C37C15C``

    Parameters:
        w (``int`` ``32-bit``):
            Width of image

        h (``int`` ``32-bit``):
            Height of image

    """

    __slots__: List[str] = ["w", "h"]

    ID = 0x6c37c15c
    QUALNAME = "types.DocumentAttributeImageSize"

    def __init__(self, *, w: int, h: int) -> None:
        self.w = w  # int
        self.h = h  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeImageSize":
        # No flags

        w = Int.read(b)

        h = Int.read(b)

        return DocumentAttributeImageSize(w=w, h=h)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.w))

        b.write(Int(self.h))

        return b.getvalue()
