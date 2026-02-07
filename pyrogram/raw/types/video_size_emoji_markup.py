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


class VideoSizeEmojiMarkup(TLObject):  # type: ignore
    """An animated profile picture based on a custom emoji sticker.

    Constructor of :obj:`~pyrogram.raw.base.VideoSize`.

    Details:
        - Layer: ``224``
        - ID: ``F85C413C``

    Parameters:
        emoji_id (``int`` ``64-bit``):
            Custom emoji ID: the custom emoji sticker is shown at the center of the profile picture and occupies at most 67% of it.

        background_colors (List of ``int`` ``32-bit``):
            1, 2, 3 or 4 RBG-24 colors used to generate a solid (1), gradient (2) or freeform gradient (3, 4) background, similar to how fill wallpapers are generated. The rotation angle for gradient backgrounds is 0.

    """

    __slots__: List[str] = ["emoji_id", "background_colors"]

    ID = 0xf85c413c
    QUALNAME = "types.VideoSizeEmojiMarkup"

    def __init__(self, *, emoji_id: int, background_colors: List[int]) -> None:
        self.emoji_id = emoji_id  # long
        self.background_colors = background_colors  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VideoSizeEmojiMarkup":
        # No flags

        emoji_id = Long.read(b)

        background_colors = TLObject.read(b, Int)

        return VideoSizeEmojiMarkup(emoji_id=emoji_id, background_colors=background_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.emoji_id))

        b.write(Vector(self.background_colors, Int))

        return b.getvalue()
