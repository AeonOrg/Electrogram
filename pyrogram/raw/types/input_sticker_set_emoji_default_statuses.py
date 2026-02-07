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


class InputStickerSetEmojiDefaultStatuses(TLObject):  # type: ignore
    """Default custom emoji status stickerset

    Constructor of :obj:`~pyrogram.raw.base.InputStickerSet`.

    Details:
        - Layer: ``224``
        - ID: ``29D0F5EE``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x29d0f5ee
    QUALNAME = "types.InputStickerSetEmojiDefaultStatuses"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetEmojiDefaultStatuses":
        # No flags

        return InputStickerSetEmojiDefaultStatuses()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
