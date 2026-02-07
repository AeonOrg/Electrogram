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


class PhotoSize(TLObject):  # type: ignore
    """Image description.

    Constructor of :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``224``
        - ID: ``75C78E60``

    Parameters:
        type (``str``):
            Thumbnail type »

        w (``int`` ``32-bit``):
            Image width

        h (``int`` ``32-bit``):
            Image height

        size (``int`` ``32-bit``):
            File size

    """

    __slots__: List[str] = ["type", "w", "h", "size"]

    ID = 0x75c78e60
    QUALNAME = "types.PhotoSize"

    def __init__(self, *, type: str, w: int, h: int, size: int) -> None:
        self.type = type  # string
        self.w = w  # int
        self.h = h  # int
        self.size = size  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoSize":
        # No flags

        type = String.read(b)

        w = Int.read(b)

        h = Int.read(b)

        size = Int.read(b)

        return PhotoSize(type=type, w=w, h=h, size=size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.type))

        b.write(Int(self.w))

        b.write(Int(self.h))

        b.write(Int(self.size))

        return b.getvalue()
