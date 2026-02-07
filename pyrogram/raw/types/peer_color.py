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


class PeerColor(TLObject):  # type: ignore
    """Represents a color palette ».

    Constructor of :obj:`~pyrogram.raw.base.PeerColor`.

    Details:
        - Layer: ``224``
        - ID: ``B54B5ACF``

    Parameters:
        color (``int`` ``32-bit``, *optional*):
            Color palette ID, see here » for more info; if not set, the default palette should be used.

        background_emoji_id (``int`` ``64-bit``, *optional*):
            Optional custom emoji ID used to generate the pattern.

    """

    __slots__: List[str] = ["color", "background_emoji_id"]

    ID = 0xb54b5acf
    QUALNAME = "types.PeerColor"

    def __init__(self, *, color: Optional[int] = None, background_emoji_id: Optional[int] = None) -> None:
        self.color = color  # flags.0?int
        self.background_emoji_id = background_emoji_id  # flags.1?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColor":

        flags = Int.read(b)

        color = Int.read(b) if flags & (1 << 0) else None
        background_emoji_id = Long.read(b) if flags & (1 << 1) else None
        return PeerColor(color=color, background_emoji_id=background_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.color is not None else 0
        flags |= (1 << 1) if self.background_emoji_id is not None else 0
        b.write(Int(flags))

        if self.color is not None:
            b.write(Int(self.color))

        if self.background_emoji_id is not None:
            b.write(Long(self.background_emoji_id))

        return b.getvalue()
