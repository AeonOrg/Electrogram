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


class GetFeaturedStickers(TLObject):  # type: ignore
    """Get featured stickers


    Details:
        - Layer: ``224``
        - ID: ``64780B14``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.featuredStickers.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`messages.FeaturedStickers <pyrogram.raw.base.messages.FeaturedStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x64780b14
    QUALNAME = "functions.messages.GetFeaturedStickers"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFeaturedStickers":
        # No flags

        hash = Long.read(b)

        return GetFeaturedStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        return b.getvalue()
