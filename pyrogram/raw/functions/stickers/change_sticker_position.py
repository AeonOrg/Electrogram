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


class ChangeStickerPosition(TLObject):  # type: ignore
    """Changes the absolute position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot


    Details:
        - Layer: ``224``
        - ID: ``FFB6D4CA``

    Parameters:
        sticker (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            The sticker

        position (``int`` ``32-bit``):
            The new position of the sticker, zero-based

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker", "position"]

    ID = 0xffb6d4ca
    QUALNAME = "functions.stickers.ChangeStickerPosition"

    def __init__(self, *, sticker: "raw.base.InputDocument", position: int) -> None:
        self.sticker = sticker  # InputDocument
        self.position = position  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeStickerPosition":
        # No flags

        sticker = TLObject.read(b)

        position = Int.read(b)

        return ChangeStickerPosition(sticker=sticker, position=position)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.sticker.write())

        b.write(Int(self.position))

        return b.getvalue()
