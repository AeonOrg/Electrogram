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


class PeerColorSet(TLObject):  # type: ignore
    """Represents a color palette that can be used in message accents ».

    Constructor of :obj:`~pyrogram.raw.base.help.PeerColorSet`.

    Details:
        - Layer: ``224``
        - ID: ``26219A58``

    Parameters:
        colors (List of ``int`` ``32-bit``):
            A list of 1-3 colors in RGB format, describing the accent color.

    """

    __slots__: List[str] = ["colors"]

    ID = 0x26219a58
    QUALNAME = "types.help.PeerColorSet"

    def __init__(self, *, colors: List[int]) -> None:
        self.colors = colors  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorSet":
        # No flags

        colors = TLObject.read(b, Int)

        return PeerColorSet(colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.colors, Int))

        return b.getvalue()
