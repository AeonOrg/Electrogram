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


class InputMediaVenue(TLObject):  # type: ignore
    """Can be used to send a venue geolocation.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``C13D1C11``

    Parameters:
        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`):
            Geolocation

        title (``str``):
            Venue name

        address (``str``):
            Physical address of the venue

        provider (``str``):
            Venue provider: currently only "foursquare" and "gplaces" (Google Places) need to be supported

        venue_id (``str``):
            Venue ID in the provider's database

        venue_type (``str``):
            Venue type in the provider's database

    """

    __slots__: List[str] = ["geo_point", "title", "address", "provider", "venue_id", "venue_type"]

    ID = 0xc13d1c11
    QUALNAME = "types.InputMediaVenue"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", title: str, address: str, provider: str, venue_id: str, venue_type: str) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.title = title  # string
        self.address = address  # string
        self.provider = provider  # string
        self.venue_id = venue_id  # string
        self.venue_type = venue_type  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaVenue":
        # No flags

        geo_point = TLObject.read(b)

        title = String.read(b)

        address = String.read(b)

        provider = String.read(b)

        venue_id = String.read(b)

        venue_type = String.read(b)

        return InputMediaVenue(geo_point=geo_point, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.geo_point.write())

        b.write(String(self.title))

        b.write(String(self.address))

        b.write(String(self.provider))

        b.write(String(self.venue_id))

        b.write(String(self.venue_type))

        return b.getvalue()
