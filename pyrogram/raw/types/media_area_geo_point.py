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


class MediaAreaGeoPoint(TLObject):  # type: ignore
    """Represents a geolocation tag attached to a story.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``224``
        - ID: ``CAD5452D``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            The size and position of the media area corresponding to the location sticker on top of the story media.

        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            Coordinates of the geolocation tag.

        address (:obj:`GeoPointAddress <pyrogram.raw.base.GeoPointAddress>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["coordinates", "geo", "address"]

    ID = 0xcad5452d
    QUALNAME = "types.MediaAreaGeoPoint"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", geo: "raw.base.GeoPoint", address: "raw.base.GeoPointAddress" = None) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.geo = geo  # GeoPoint
        self.address = address  # flags.0?GeoPointAddress

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaGeoPoint":

        flags = Int.read(b)

        coordinates = TLObject.read(b)

        geo = TLObject.read(b)

        address = TLObject.read(b) if flags & (1 << 0) else None

        return MediaAreaGeoPoint(coordinates=coordinates, geo=geo, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.address is not None else 0
        b.write(Int(flags))

        b.write(self.coordinates.write())

        b.write(self.geo.write())

        if self.address is not None:
            b.write(self.address.write())

        return b.getvalue()
