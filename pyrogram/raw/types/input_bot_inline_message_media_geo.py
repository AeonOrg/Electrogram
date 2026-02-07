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


class InputBotInlineMessageMediaGeo(TLObject):  # type: ignore
    """Geolocation

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``96929A85``

    Parameters:
        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`):
            Geolocation

        heading (``int`` ``32-bit``, *optional*):
            For live locations, a direction in which the location moves, in degrees; 1-360

        period (``int`` ``32-bit``, *optional*):
            Validity period

        proximity_notification_radius (``int`` ``32-bit``, *optional*):
            For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000)

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Reply markup for bot/inline keyboards

    """

    __slots__: List[str] = ["geo_point", "heading", "period", "proximity_notification_radius", "reply_markup"]

    ID = 0x96929a85
    QUALNAME = "types.InputBotInlineMessageMediaGeo"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.heading = heading  # flags.0?int
        self.period = period  # flags.1?int
        self.proximity_notification_radius = proximity_notification_radius  # flags.3?int
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageMediaGeo":

        flags = Int.read(b)

        geo_point = TLObject.read(b)

        heading = Int.read(b) if flags & (1 << 0) else None
        period = Int.read(b) if flags & (1 << 1) else None
        proximity_notification_radius = Int.read(b) if flags & (1 << 3) else None
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        return InputBotInlineMessageMediaGeo(geo_point=geo_point, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.heading is not None else 0
        flags |= (1 << 1) if self.period is not None else 0
        flags |= (1 << 3) if self.proximity_notification_radius is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))

        b.write(self.geo_point.write())

        if self.heading is not None:
            b.write(Int(self.heading))

        if self.period is not None:
            b.write(Int(self.period))

        if self.proximity_notification_radius is not None:
            b.write(Int(self.proximity_notification_radius))

        if self.reply_markup is not None:
            b.write(self.reply_markup.write())

        return b.getvalue()
