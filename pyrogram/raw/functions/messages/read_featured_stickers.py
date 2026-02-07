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


class ReadFeaturedStickers(TLObject):  # type: ignore
    """Mark new featured stickers as read


    Details:
        - Layer: ``224``
        - ID: ``5B118126``

    Parameters:
        id (List of ``int`` ``64-bit``):
            IDs of stickersets to mark as read

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0x5b118126
    QUALNAME = "functions.messages.ReadFeaturedStickers"

    def __init__(self, *, id: List[int]) -> None:
        self.id = id  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadFeaturedStickers":
        # No flags

        id = TLObject.read(b, Long)

        return ReadFeaturedStickers(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.id, Long))

        return b.getvalue()
