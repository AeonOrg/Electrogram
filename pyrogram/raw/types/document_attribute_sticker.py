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


class DocumentAttributeSticker(TLObject):  # type: ignore
    """Defines a sticker

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``6319D612``

    Parameters:
        alt (``str``):
            Alternative emoji representation of sticker

        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            Associated stickerset

        mask (``bool``, *optional*):
            Whether this is a mask sticker

        mask_coords (:obj:`MaskCoords <pyrogram.raw.base.MaskCoords>`, *optional*):
            Mask coordinates (if this is a mask sticker, attached to a photo)

    """

    __slots__: List[str] = ["alt", "stickerset", "mask", "mask_coords"]

    ID = 0x6319d612
    QUALNAME = "types.DocumentAttributeSticker"

    def __init__(self, *, alt: str, stickerset: "raw.base.InputStickerSet", mask: Optional[bool] = None, mask_coords: "raw.base.MaskCoords" = None) -> None:
        self.alt = alt  # string
        self.stickerset = stickerset  # InputStickerSet
        self.mask = mask  # flags.1?true
        self.mask_coords = mask_coords  # flags.0?MaskCoords

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeSticker":

        flags = Int.read(b)

        mask = True if flags & (1 << 1) else False
        alt = String.read(b)

        stickerset = TLObject.read(b)

        mask_coords = TLObject.read(b) if flags & (1 << 0) else None

        return DocumentAttributeSticker(alt=alt, stickerset=stickerset, mask=mask, mask_coords=mask_coords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.mask else 0
        flags |= (1 << 0) if self.mask_coords is not None else 0
        b.write(Int(flags))

        b.write(String(self.alt))

        b.write(self.stickerset.write())

        if self.mask_coords is not None:
            b.write(self.mask_coords.write())

        return b.getvalue()
