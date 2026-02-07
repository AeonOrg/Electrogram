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


class PhotoCachedSize(TLObject):  # type: ignore
    """Description of an image and its content.

    Constructor of :obj:`~pyrogram.raw.base.PhotoSize`.

    Details:
        - Layer: ``224``
        - ID: ``21E1AD6``

    Parameters:
        type (``str``):
            Thumbnail type

        w (``int`` ``32-bit``):
            Image width

        h (``int`` ``32-bit``):
            Image height

        bytes (``bytes``):
            Binary data, file content

    """

    __slots__: List[str] = ["type", "w", "h", "bytes"]

    ID = 0x21e1ad6
    QUALNAME = "types.PhotoCachedSize"

    def __init__(self, *, type: str, w: int, h: int, bytes: bytes) -> None:
        self.type = type  # string
        self.w = w  # int
        self.h = h  # int
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhotoCachedSize":
        # No flags

        type = String.read(b)

        w = Int.read(b)

        h = Int.read(b)

        bytes = Bytes.read(b)

        return PhotoCachedSize(type=type, w=w, h=h, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.type))

        b.write(Int(self.w))

        b.write(Int(self.h))

        b.write(Bytes(self.bytes))

        return b.getvalue()
