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


class InputStickerSetItem(TLObject):  # type: ignore
    """Sticker in a stickerset

    Constructor of :obj:`~pyrogram.raw.base.InputStickerSetItem`.

    Details:
        - Layer: ``224``
        - ID: ``32DA9E9C``

    Parameters:
        document (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            The sticker

        emoji (``str``):
            Associated emoji

        mask_coords (:obj:`MaskCoords <pyrogram.raw.base.MaskCoords>`, *optional*):
            Coordinates for mask sticker

        keywords (``str``, *optional*):
            Set of keywords, separated by commas (can't be provided for mask stickers)

    """

    __slots__: List[str] = ["document", "emoji", "mask_coords", "keywords"]

    ID = 0x32da9e9c
    QUALNAME = "types.InputStickerSetItem"

    def __init__(self, *, document: "raw.base.InputDocument", emoji: str, mask_coords: "raw.base.MaskCoords" = None, keywords: Optional[str] = None) -> None:
        self.document = document  # InputDocument
        self.emoji = emoji  # string
        self.mask_coords = mask_coords  # flags.0?MaskCoords
        self.keywords = keywords  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetItem":

        flags = Int.read(b)

        document = TLObject.read(b)

        emoji = String.read(b)

        mask_coords = TLObject.read(b) if flags & (1 << 0) else None

        keywords = String.read(b) if flags & (1 << 1) else None
        return InputStickerSetItem(document=document, emoji=emoji, mask_coords=mask_coords, keywords=keywords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.mask_coords is not None else 0
        flags |= (1 << 1) if self.keywords is not None else 0
        b.write(Int(flags))

        b.write(self.document.write())

        b.write(String(self.emoji))

        if self.mask_coords is not None:
            b.write(self.mask_coords.write())

        if self.keywords is not None:
            b.write(String(self.keywords))

        return b.getvalue()
