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


class ChangeSticker(TLObject):  # type: ignore
    """Update the keywords, emojis or mask coordinates of a sticker, bots only.


    Details:
        - Layer: ``224``
        - ID: ``F5537EBC``

    Parameters:
        sticker (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            The sticker

        emoji (``str``, *optional*):
            If set, updates the emoji list associated to the sticker

        mask_coords (:obj:`MaskCoords <pyrogram.raw.base.MaskCoords>`, *optional*):
            If set, updates the mask coordinates

        keywords (``str``, *optional*):
            If set, updates the sticker keywords (separated by commas). Can't be provided for mask stickers.

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker", "emoji", "mask_coords", "keywords"]

    ID = 0xf5537ebc
    QUALNAME = "functions.stickers.ChangeSticker"

    def __init__(self, *, sticker: "raw.base.InputDocument", emoji: Optional[str] = None, mask_coords: "raw.base.MaskCoords" = None, keywords: Optional[str] = None) -> None:
        self.sticker = sticker  # InputDocument
        self.emoji = emoji  # flags.0?string
        self.mask_coords = mask_coords  # flags.1?MaskCoords
        self.keywords = keywords  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeSticker":

        flags = Int.read(b)

        sticker = TLObject.read(b)

        emoji = String.read(b) if flags & (1 << 0) else None
        mask_coords = TLObject.read(b) if flags & (1 << 1) else None

        keywords = String.read(b) if flags & (1 << 2) else None
        return ChangeSticker(sticker=sticker, emoji=emoji, mask_coords=mask_coords, keywords=keywords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.emoji is not None else 0
        flags |= (1 << 1) if self.mask_coords is not None else 0
        flags |= (1 << 2) if self.keywords is not None else 0
        b.write(Int(flags))

        b.write(self.sticker.write())

        if self.emoji is not None:
            b.write(String(self.emoji))

        if self.mask_coords is not None:
            b.write(self.mask_coords.write())

        if self.keywords is not None:
            b.write(String(self.keywords))

        return b.getvalue()
