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


class BusinessLocation(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.BusinessLocation`.

    Details:
        - Layer: ``224``
        - ID: ``AC5C1AF7``

    Parameters:
        address (``str``):


        geo_point (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`, *optional*):


    """

    __slots__: List[str] = ["address", "geo_point"]

    ID = 0xac5c1af7
    QUALNAME = "types.BusinessLocation"

    def __init__(self, *, address: str, geo_point: "raw.base.GeoPoint" = None) -> None:
        self.address = address  # string
        self.geo_point = geo_point  # flags.0?GeoPoint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessLocation":

        flags = Int.read(b)

        geo_point = TLObject.read(b) if flags & (1 << 0) else None

        address = String.read(b)

        return BusinessLocation(address=address, geo_point=geo_point)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.geo_point is not None else 0
        b.write(Int(flags))

        if self.geo_point is not None:
            b.write(self.geo_point.write())

        b.write(String(self.address))

        return b.getvalue()
