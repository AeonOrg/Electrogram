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


class MediaAreaStarGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``224``
        - ID: ``5787686D``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        slug (``str``):
            N/A

    """

    __slots__: List[str] = ["coordinates", "slug"]

    ID = 0x5787686d
    QUALNAME = "types.MediaAreaStarGift"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", slug: str) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaStarGift":
        # No flags

        coordinates = TLObject.read(b)

        slug = String.read(b)

        return MediaAreaStarGift(coordinates=coordinates, slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.coordinates.write())

        b.write(String(self.slug))

        return b.getvalue()
