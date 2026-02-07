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


class ReplaceSticker(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``4696459A``

    Parameters:
        sticker (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):


        new_sticker (:obj:`InputStickerSetItem <pyrogram.raw.base.InputStickerSetItem>`):


    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker", "new_sticker"]

    ID = 0x4696459a
    QUALNAME = "functions.stickers.ReplaceSticker"

    def __init__(self, *, sticker: "raw.base.InputDocument", new_sticker: "raw.base.InputStickerSetItem") -> None:
        self.sticker = sticker  # InputDocument
        self.new_sticker = new_sticker  # InputStickerSetItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplaceSticker":
        # No flags

        sticker = TLObject.read(b)

        new_sticker = TLObject.read(b)

        return ReplaceSticker(sticker=sticker, new_sticker=new_sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.sticker.write())

        b.write(self.new_sticker.write())

        return b.getvalue()
