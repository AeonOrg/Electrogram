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


class ChannelAdminLogEventActionChangeStickerSet(TLObject):  # type: ignore
    """The supergroup's stickerset was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``B1C3CAA7``

    Parameters:
        prev_stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            Previous stickerset

        new_stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            New stickerset

    """

    __slots__: List[str] = ["prev_stickerset", "new_stickerset"]

    ID = 0xb1c3caa7
    QUALNAME = "types.ChannelAdminLogEventActionChangeStickerSet"

    def __init__(self, *, prev_stickerset: "raw.base.InputStickerSet", new_stickerset: "raw.base.InputStickerSet") -> None:
        self.prev_stickerset = prev_stickerset  # InputStickerSet
        self.new_stickerset = new_stickerset  # InputStickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeStickerSet":
        # No flags

        prev_stickerset = TLObject.read(b)

        new_stickerset = TLObject.read(b)

        return ChannelAdminLogEventActionChangeStickerSet(prev_stickerset=prev_stickerset, new_stickerset=new_stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.prev_stickerset.write())

        b.write(self.new_stickerset.write())

        return b.getvalue()
