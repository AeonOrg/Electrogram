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


class PhotoPathSize(TLObject):  # type: ignore
    """Messages with animated stickers can have a compressed svg (< 300 bytes) to show the outline of the sticker before fetching the actual lottie animation.

    Constructor of :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``224``
        - ID: ``D8214D41``

    Parameters:
        type (``str``):
            Always j

        bytes (``bytes``):
            Compressed SVG path payload, see here for decompression instructions

    """

    __slots__: List[str] = ["type", "bytes"]

    ID = 0xd8214d41
    QUALNAME = "types.PhotoPathSize"

    def __init__(self, *, type: str, bytes: bytes) -> None:
        self.type = type  # string
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoPathSize":
        # No flags

        type = String.read(b)

        bytes = Bytes.read(b)

        return PhotoPathSize(type=type, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.type))

        b.write(Bytes(self.bytes))

        return b.getvalue()
