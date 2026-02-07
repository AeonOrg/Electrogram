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


class GetLocated(TLObject):  # type: ignore
    """Get users and geochats near you, see here » for more info.


    Details:
        - Layer: ``224``
        - ID: ``D348BC44``

    Parameters:
        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`):
            Geolocation

        background (``bool``, *optional*):
            While the geolocation of the current user is public, clients should update it in the background every half-an-hour or so, while setting this flag. Do this only if the new location is more than 1 KM away from the previous one, or if the previous location is unknown.

        self_expires (``int`` ``32-bit``, *optional*):
            If set, the geolocation of the current user will be public for the specified number of seconds; pass 0x7fffffff to disable expiry, 0 to make the current geolocation private; if the flag isn't set, no changes will be applied.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["geo_point", "background", "self_expires"]

    ID = 0xd348bc44
    QUALNAME = "functions.contacts.GetLocated"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", background: Optional[bool] = None, self_expires: Optional[int] = None) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.background = background  # flags.1?true
        self.self_expires = self_expires  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLocated":

        flags = Int.read(b)

        background = True if flags & (1 << 1) else False
        geo_point = TLObject.read(b)

        self_expires = Int.read(b) if flags & (1 << 0) else None
        return GetLocated(geo_point=geo_point, background=background, self_expires=self_expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.background else 0
        flags |= (1 << 0) if self.self_expires is not None else 0
        b.write(Int(flags))

        b.write(self.geo_point.write())

        if self.self_expires is not None:
            b.write(Int(self.self_expires))

        return b.getvalue()
