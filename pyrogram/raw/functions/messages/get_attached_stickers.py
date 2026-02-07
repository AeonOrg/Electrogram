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


class GetAttachedStickers(TLObject):  # type: ignore
    """Get stickers attached to a photo or video


    Details:
        - Layer: ``224``
        - ID: ``CC5B67CC``

    Parameters:
        media (:obj:`InputStickeredMedia <pyrogram.raw.base.InputStickeredMedia>`):
            Stickered media

    Returns:
        List of :obj:`StickerSetCovered <pyrogram.raw.base.StickerSetCovered>`
    """

    __slots__: List[str] = ["media"]

    ID = 0xcc5b67cc
    QUALNAME = "functions.messages.GetAttachedStickers"

    def __init__(self, *, media: "raw.base.InputStickeredMedia") -> None:
        self.media = media  # InputStickeredMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAttachedStickers":
        # No flags

        media = TLObject.read(b)

        return GetAttachedStickers(media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.media.write())

        return b.getvalue()
