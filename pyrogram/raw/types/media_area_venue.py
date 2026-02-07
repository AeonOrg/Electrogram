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


class MediaAreaVenue(TLObject):  # type: ignore
    """Represents a location tag attached to a story, with additional venue information.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``224``
        - ID: ``BE82DB9C``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            The size and location of the media area corresponding to the location sticker on top of the story media.

        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            Coordinates of the venue

        title (``str``):
            Venue name

        address (``str``):
            Address

        provider (``str``):
            Venue provider: currently only "foursquare" needs to be supported.

        venue_id (``str``):
            Venue ID in the provider's database

        venue_type (``str``):
            Venue type in the provider's database

    """

    __slots__: List[str] = ["coordinates", "geo", "title", "address", "provider", "venue_id", "venue_type"]

    ID = 0xbe82db9c
    QUALNAME = "types.MediaAreaVenue"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", geo: "raw.base.GeoPoint", title: str, address: str, provider: str, venue_id: str, venue_type: str) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.geo = geo  # GeoPoint
        self.title = title  # string
        self.address = address  # string
        self.provider = provider  # string
        self.venue_id = venue_id  # string
        self.venue_type = venue_type  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaVenue":
        # No flags

        coordinates = TLObject.read(b)

        geo = TLObject.read(b)

        title = String.read(b)

        address = String.read(b)

        provider = String.read(b)

        venue_id = String.read(b)

        venue_type = String.read(b)

        return MediaAreaVenue(coordinates=coordinates, geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.coordinates.write())

        b.write(self.geo.write())

        b.write(String(self.title))

        b.write(String(self.address))

        b.write(String(self.provider))

        b.write(String(self.venue_id))

        b.write(String(self.venue_type))

        return b.getvalue()
