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


class StarsRating(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsRating`.

    Details:
        - Layer: ``224``
        - ID: ``1B0E4F07``

    Parameters:
        level (``int`` ``32-bit``):
            N/A

        current_level_stars (``int`` ``64-bit``):
            N/A

        stars (``int`` ``64-bit``):
            N/A

        next_level_stars (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["level", "current_level_stars", "stars", "next_level_stars"]

    ID = 0x1b0e4f07
    QUALNAME = "types.StarsRating"

    def __init__(self, *, level: int, current_level_stars: int, stars: int, next_level_stars: Optional[int] = None) -> None:
        self.level = level  # int
        self.current_level_stars = current_level_stars  # long
        self.stars = stars  # long
        self.next_level_stars = next_level_stars  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsRating":

        flags = Int.read(b)

        level = Int.read(b)

        current_level_stars = Long.read(b)

        stars = Long.read(b)

        next_level_stars = Long.read(b) if flags & (1 << 0) else None
        return StarsRating(level=level, current_level_stars=current_level_stars, stars=stars, next_level_stars=next_level_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_level_stars is not None else 0
        b.write(Int(flags))

        b.write(Int(self.level))

        b.write(Long(self.current_level_stars))

        b.write(Long(self.stars))

        if self.next_level_stars is not None:
            b.write(Long(self.next_level_stars))

        return b.getvalue()
