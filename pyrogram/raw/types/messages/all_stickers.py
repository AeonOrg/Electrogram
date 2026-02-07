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


class AllStickers(TLObject):  # type: ignore
    """Info about all installed stickers

    Constructor of :obj:`~pyrogram.raw.base.messages.AllStickers`.

    Details:
        - Layer: ``224``
        - ID: ``CDBBCEBB``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        sets (List of :obj:`StickerSet <pyrogram.raw.base.StickerSet>`):
            All stickersets

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAllStickers
            messages.GetMaskStickers
            messages.GetEmojiStickers
    """

    __slots__: List[str] = ["hash", "sets"]

    ID = 0xcdbbcebb
    QUALNAME = "types.messages.AllStickers"

    def __init__(self, *, hash: int, sets: List["raw.base.StickerSet"]) -> None:
        self.hash = hash  # long
        self.sets = sets  # Vector<StickerSet>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AllStickers":
        # No flags

        hash = Long.read(b)

        sets = TLObject.read(b)

        return AllStickers(hash=hash, sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        b.write(Vector(self.sets))

        return b.getvalue()
