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


class PeerColorProfileSet(TLObject):  # type: ignore
    """Represents a color palette that can be used in profile pages ».

    Constructor of :obj:`~pyrogram.raw.base.help.PeerColorSet`.

    Details:
        - Layer: ``224``
        - ID: ``767D61EB``

    Parameters:
        palette_colors (List of ``int`` ``32-bit``):
            A list of 1-2 colors in RGB format, shown in the color palette settings to describe the current palette.

        bg_colors (List of ``int`` ``32-bit``):
            A list of 1-2 colors in RGB format describing the colors used to generate the actual background used in the profile page.

        story_colors (List of ``int`` ``32-bit``):
            A list of 2 colors in RGB format describing the colors of the gradient used for the unread active story indicator around the profile photo.

    """

    __slots__: List[str] = ["palette_colors", "bg_colors", "story_colors"]

    ID = 0x767d61eb
    QUALNAME = "types.help.PeerColorProfileSet"

    def __init__(self, *, palette_colors: List[int], bg_colors: List[int], story_colors: List[int]) -> None:
        self.palette_colors = palette_colors  # Vector<int>
        self.bg_colors = bg_colors  # Vector<int>
        self.story_colors = story_colors  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorProfileSet":
        # No flags

        palette_colors = TLObject.read(b, Int)

        bg_colors = TLObject.read(b, Int)

        story_colors = TLObject.read(b, Int)

        return PeerColorProfileSet(palette_colors=palette_colors, bg_colors=bg_colors, story_colors=story_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.palette_colors, Int))

        b.write(Vector(self.bg_colors, Int))

        b.write(Vector(self.story_colors, Int))

        return b.getvalue()
