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


class MaskCoords(TLObject):  # type: ignore
    """Position on a photo where a mask should be placed when attaching stickers to media »

    Constructor of :obj:`~pyrogram.raw.base.MaskCoords`.

    Details:
        - Layer: ``224``
        - ID: ``AED6DBB2``

    Parameters:
        n (``int`` ``32-bit``):
            Part of the face, relative to which the mask should be placed

        x (``float`` ``64-bit``):
            Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)

        y (``float`` ``64-bit``):
            Shift by Y-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just below the default mask position)

        zoom (``float`` ``64-bit``):
            Mask scaling coefficient. (For example, 2.0 means a doubled size)

    """

    __slots__: List[str] = ["n", "x", "y", "zoom"]

    ID = 0xaed6dbb2
    QUALNAME = "types.MaskCoords"

    def __init__(self, *, n: int, x: float, y: float, zoom: float) -> None:
        self.n = n  # int
        self.x = x  # double
        self.y = y  # double
        self.zoom = zoom  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MaskCoords":
        # No flags

        n = Int.read(b)

        x = Double.read(b)

        y = Double.read(b)

        zoom = Double.read(b)

        return MaskCoords(n=n, x=x, y=y, zoom=zoom)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.n))

        b.write(Double(self.x))

        b.write(Double(self.y))

        b.write(Double(self.zoom))

        return b.getvalue()
