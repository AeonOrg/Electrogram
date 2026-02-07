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


class InputStickerSetThumb(TLObject):  # type: ignore
    """Location of stickerset thumbnail (see files)

    Constructor of :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``9D84F3DB``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            Sticker set

        thumb_version (``int`` ``32-bit``):
            Thumbnail version

    """

    __slots__: List[str] = ["stickerset", "thumb_version"]

    ID = 0x9d84f3db
    QUALNAME = "types.InputStickerSetThumb"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", thumb_version: int) -> None:
        self.stickerset = stickerset  # InputStickerSet
        self.thumb_version = thumb_version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetThumb":
        # No flags

        stickerset = TLObject.read(b)

        thumb_version = Int.read(b)

        return InputStickerSetThumb(stickerset=stickerset, thumb_version=thumb_version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.stickerset.write())

        b.write(Int(self.thumb_version))

        return b.getvalue()
