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


class MessageMediaGeo(TLObject):  # type: ignore
    """Attached map.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``56E0D474``

    Parameters:
        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`):
            GeoPoint

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["geo"]

    ID = 0x56e0d474
    QUALNAME = "types.MessageMediaGeo"

    def __init__(self, *, geo: "raw.base.GeoPoint") -> None:
        self.geo = geo  # GeoPoint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGeo":
        # No flags

        geo = TLObject.read(b)

        return MessageMediaGeo(geo=geo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.geo.write())

        return b.getvalue()
