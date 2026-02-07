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


class MediaAreaCoordinates(TLObject):  # type: ignore
    """Coordinates and size of a clicable rectangular area on top of a story.

    Constructor of :obj:`~pyrogram.raw.base.MediaAreaCoordinates`.

    Details:
        - Layer: ``224``
        - ID: ``CFC9E002``

    Parameters:
        x (``float`` ``64-bit``):
            The abscissa of the rectangle's center, as a percentage of the media width (0-100).

        y (``float`` ``64-bit``):
            The ordinate of the rectangle's center, as a percentage of the media height (0-100).

        w (``float`` ``64-bit``):
            The width of the rectangle, as a percentage of the media width (0-100).

        h (``float`` ``64-bit``):
            The height of the rectangle, as a percentage of the media height (0-100).

        rotation (``float`` ``64-bit``):
            Clockwise rotation angle of the rectangle, in degrees (0-360).

        radius (``float`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["x", "y", "w", "h", "rotation", "radius"]

    ID = 0xcfc9e002
    QUALNAME = "types.MediaAreaCoordinates"

    def __init__(self, *, x: float, y: float, w: float, h: float, rotation: float, radius: Optional[float] = None) -> None:
        self.x = x  # double
        self.y = y  # double
        self.w = w  # double
        self.h = h  # double
        self.rotation = rotation  # double
        self.radius = radius  # flags.0?double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaCoordinates":

        flags = Int.read(b)

        x = Double.read(b)

        y = Double.read(b)

        w = Double.read(b)

        h = Double.read(b)

        rotation = Double.read(b)

        radius = Double.read(b) if flags & (1 << 0) else None
        return MediaAreaCoordinates(x=x, y=y, w=w, h=h, rotation=rotation, radius=radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.radius is not None else 0
        b.write(Int(flags))

        b.write(Double(self.x))

        b.write(Double(self.y))

        b.write(Double(self.w))

        b.write(Double(self.h))

        b.write(Double(self.rotation))

        if self.radius is not None:
            b.write(Double(self.radius))

        return b.getvalue()
