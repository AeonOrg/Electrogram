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


class InputGeoPoint(TLObject):  # type: ignore
    """Defines a GeoPoint by its coordinates.

    Constructor of :obj:`~pyrogram.raw.base.InputGeoPoint`.

    Details:
        - Layer: ``224``
        - ID: ``48222FAF``

    Parameters:
        lat (``float`` ``64-bit``):
            Latitude

        long (``float`` ``64-bit``):
            Longitude

        accuracy_radius (``int`` ``32-bit``, *optional*):
            The estimated horizontal accuracy of the location, in meters; as defined by the sender.

    """

    __slots__: List[str] = ["lat", "long", "accuracy_radius"]

    ID = 0x48222faf
    QUALNAME = "types.InputGeoPoint"

    def __init__(self, *, lat: float, long: float, accuracy_radius: Optional[int] = None) -> None:
        self.lat = lat  # double
        self.long = long  # double
        self.accuracy_radius = accuracy_radius  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGeoPoint":

        flags = Int.read(b)

        lat = Double.read(b)

        long = Double.read(b)

        accuracy_radius = Int.read(b) if flags & (1 << 0) else None
        return InputGeoPoint(lat=lat, long=long, accuracy_radius=accuracy_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.accuracy_radius is not None else 0
        b.write(Int(flags))

        b.write(Double(self.lat))

        b.write(Double(self.long))

        if self.accuracy_radius is not None:
            b.write(Int(self.accuracy_radius))

        return b.getvalue()
