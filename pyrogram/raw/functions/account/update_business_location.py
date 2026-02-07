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


class UpdateBusinessLocation(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``9E6B131A``

    Parameters:
        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`, *optional*):


        address (``str``, *optional*):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["geo_point", "address"]

    ID = 0x9e6b131a
    QUALNAME = "functions.account.UpdateBusinessLocation"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint" = None, address: Optional[str] = None) -> None:
        self.geo_point = geo_point  # flags.1?InputGeoPoint
        self.address = address  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessLocation":

        flags = Int.read(b)

        geo_point = TLObject.read(b) if flags & (1 << 1) else None

        address = String.read(b) if flags & (1 << 0) else None
        return UpdateBusinessLocation(geo_point=geo_point, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.geo_point is not None else 0
        flags |= (1 << 0) if self.address is not None else 0
        b.write(Int(flags))

        if self.geo_point is not None:
            b.write(self.geo_point.write())

        if self.address is not None:
            b.write(String(self.address))

        return b.getvalue()
