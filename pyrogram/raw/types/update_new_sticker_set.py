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


class UpdateNewStickerSet(TLObject):  # type: ignore
    """A new stickerset was installed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``688A30AA``

    Parameters:
        stickerset (:obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`):
            The installed stickerset

    """

    __slots__: List[str] = ["stickerset"]

    ID = 0x688a30aa
    QUALNAME = "types.UpdateNewStickerSet"

    def __init__(self, *, stickerset: "raw.base.messages.StickerSet") -> None:
        self.stickerset = stickerset  # messages.StickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewStickerSet":
        # No flags

        stickerset = TLObject.read(b)

        return UpdateNewStickerSet(stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.stickerset.write())

        return b.getvalue()
