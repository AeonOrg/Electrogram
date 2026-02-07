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


class DeleteStickerSet(TLObject):  # type: ignore
    """Deletes a stickerset we created, bots only.


    Details:
        - Layer: ``224``
        - ID: ``87704394``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            Stickerset to delete

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["stickerset"]

    ID = 0x87704394
    QUALNAME = "functions.stickers.DeleteStickerSet"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet") -> None:
        self.stickerset = stickerset  # InputStickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteStickerSet":
        # No flags

        stickerset = TLObject.read(b)

        return DeleteStickerSet(stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.stickerset.write())

        return b.getvalue()
