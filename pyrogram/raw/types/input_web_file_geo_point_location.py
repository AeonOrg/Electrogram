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


class InputWebFileGeoPointLocation(TLObject):  # type: ignore
    """Used to download a server-generated image with the map preview from a geoPoint, see the webfile docs for more info ».

    Constructor of :obj:`~pyrogram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``9F2221C9``

    Parameters:
        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`):
            Generated from the lat, long and accuracy_radius parameters of the geoPoint

        access_hash (``int`` ``64-bit``):
            Access hash of the geoPoint

        w (``int`` ``32-bit``):
            Map width in pixels before applying scale; 16-1024

        h (``int`` ``32-bit``):
            Map height in pixels before applying scale; 16-1024

        zoom (``int`` ``32-bit``):
            Map zoom level; 13-20

        scale (``int`` ``32-bit``):
            Map scale; 1-3

    """

    __slots__: List[str] = ["geo_point", "access_hash", "w", "h", "zoom", "scale"]

    ID = 0x9f2221c9
    QUALNAME = "types.InputWebFileGeoPointLocation"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", access_hash: int, w: int, h: int, zoom: int, scale: int) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.access_hash = access_hash  # long
        self.w = w  # int
        self.h = h  # int
        self.zoom = zoom  # int
        self.scale = scale  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileGeoPointLocation":
        # No flags

        geo_point = TLObject.read(b)

        access_hash = Long.read(b)

        w = Int.read(b)

        h = Int.read(b)

        zoom = Int.read(b)

        scale = Int.read(b)

        return InputWebFileGeoPointLocation(geo_point=geo_point, access_hash=access_hash, w=w, h=h, zoom=zoom, scale=scale)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.geo_point.write())

        b.write(Long(self.access_hash))

        b.write(Int(self.w))

        b.write(Int(self.h))

        b.write(Int(self.zoom))

        b.write(Int(self.scale))

        return b.getvalue()
