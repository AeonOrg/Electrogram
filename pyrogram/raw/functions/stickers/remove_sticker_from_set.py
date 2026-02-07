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


class RemoveStickerFromSet(TLObject):  # type: ignore
    """Remove a sticker from the set where it belongs, bots only. The sticker set must have been created by the bot.


    Details:
        - Layer: ``224``
        - ID: ``F7760F51``

    Parameters:
        sticker (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            The sticker to remove

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker"]

    ID = 0xf7760f51
    QUALNAME = "functions.stickers.RemoveStickerFromSet"

    def __init__(self, *, sticker: "raw.base.InputDocument") -> None:
        self.sticker = sticker  # InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RemoveStickerFromSet":
        # No flags

        sticker = TLObject.read(b)

        return RemoveStickerFromSet(sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.sticker.write())

        return b.getvalue()
