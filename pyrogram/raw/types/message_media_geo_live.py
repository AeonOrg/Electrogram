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


class MessageMediaGeoLive(TLObject):  # type: ignore
    """Indicates a live geolocation

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``B940C666``

    Parameters:
        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            Geolocation

        period (``int`` ``32-bit``):
            Validity period of provided geolocation

        heading (``int`` ``32-bit``, *optional*):
            For live locations, a direction in which the location moves, in degrees; 1-360

        proximity_notification_radius (``int`` ``32-bit``, *optional*):
            For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000).

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["geo", "period", "heading", "proximity_notification_radius"]

    ID = 0xb940c666
    QUALNAME = "types.MessageMediaGeoLive"

    def __init__(self, *, geo: "raw.base.GeoPoint", period: int, heading: Optional[int] = None, proximity_notification_radius: Optional[int] = None) -> None:
        self.geo = geo  # GeoPoint
        self.period = period  # int
        self.heading = heading  # flags.0?int
        self.proximity_notification_radius = proximity_notification_radius  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGeoLive":

        flags = Int.read(b)

        geo = TLObject.read(b)

        heading = Int.read(b) if flags & (1 << 0) else None
        period = Int.read(b)

        proximity_notification_radius = Int.read(b) if flags & (1 << 1) else None
        return MessageMediaGeoLive(geo=geo, period=period, heading=heading, proximity_notification_radius=proximity_notification_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.heading is not None else 0
        flags |= (1 << 1) if self.proximity_notification_radius is not None else 0
        b.write(Int(flags))

        b.write(self.geo.write())

        if self.heading is not None:
            b.write(Int(self.heading))

        b.write(Int(self.period))

        if self.proximity_notification_radius is not None:
            b.write(Int(self.proximity_notification_radius))

        return b.getvalue()
