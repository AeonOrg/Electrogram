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


class SetStickerSetThumb(TLObject):  # type: ignore
    """Set stickerset thumbnail


    Details:
        - Layer: ``224``
        - ID: ``A76A5392``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            Stickerset

        thumb (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            Thumbnail (only for normal stickersets, not custom emoji stickersets).

        thumb_document_id (``int`` ``64-bit``, *optional*):
            Only for custom emoji stickersets, ID of a custom emoji present in the set to use as thumbnail; pass 0 to fallback to the first custom emoji of the set.

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["stickerset", "thumb", "thumb_document_id"]

    ID = 0xa76a5392
    QUALNAME = "functions.stickers.SetStickerSetThumb"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", thumb: "raw.base.InputDocument" = None, thumb_document_id: Optional[int] = None) -> None:
        self.stickerset = stickerset  # InputStickerSet
        self.thumb = thumb  # flags.0?InputDocument
        self.thumb_document_id = thumb_document_id  # flags.1?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetStickerSetThumb":

        flags = Int.read(b)

        stickerset = TLObject.read(b)

        thumb = TLObject.read(b) if flags & (1 << 0) else None

        thumb_document_id = Long.read(b) if flags & (1 << 1) else None
        return SetStickerSetThumb(stickerset=stickerset, thumb=thumb, thumb_document_id=thumb_document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.thumb is not None else 0
        flags |= (1 << 1) if self.thumb_document_id is not None else 0
        b.write(Int(flags))

        b.write(self.stickerset.write())

        if self.thumb is not None:
            b.write(self.thumb.write())

        if self.thumb_document_id is not None:
            b.write(Long(self.thumb_document_id))

        return b.getvalue()
