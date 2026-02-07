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


class PhotoSizeProgressive(TLObject):  # type: ignore
    """Progressively encoded photosize

    Constructor of :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``224``
        - ID: ``FA3EFB95``

    Parameters:
        type (``str``):
            Photosize type »

        w (``int`` ``32-bit``):
            Photo width

        h (``int`` ``32-bit``):
            Photo height

        sizes (List of ``int`` ``32-bit``):
            Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image.

    """

    __slots__: List[str] = ["type", "w", "h", "sizes"]

    ID = 0xfa3efb95
    QUALNAME = "types.PhotoSizeProgressive"

    def __init__(self, *, type: str, w: int, h: int, sizes: List[int]) -> None:
        self.type = type  # string
        self.w = w  # int
        self.h = h  # int
        self.sizes = sizes  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoSizeProgressive":
        # No flags

        type = String.read(b)

        w = Int.read(b)

        h = Int.read(b)

        sizes = TLObject.read(b, Int)

        return PhotoSizeProgressive(type=type, w=w, h=h, sizes=sizes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.type))

        b.write(Int(self.w))

        b.write(Int(self.h))

        b.write(Vector(self.sizes, Int))

        return b.getvalue()
