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


class EditLocation(TLObject):  # type: ignore
    """Edit location of geogroup, see here » for more info on geogroups.


    Details:
        - Layer: ``224``
        - ID: ``58E63F6D``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Geogroup

        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`):
            New geolocation

        address (``str``):
            Address string

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "geo_point", "address"]

    ID = 0x58e63f6d
    QUALNAME = "functions.channels.EditLocation"

    def __init__(self, *, channel: "raw.base.InputChannel", geo_point: "raw.base.InputGeoPoint", address: str) -> None:
        self.channel = channel  # InputChannel
        self.geo_point = geo_point  # InputGeoPoint
        self.address = address  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditLocation":
        # No flags

        channel = TLObject.read(b)

        geo_point = TLObject.read(b)

        address = String.read(b)

        return EditLocation(channel=channel, geo_point=geo_point, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(self.geo_point.write())

        b.write(String(self.address))

        return b.getvalue()
