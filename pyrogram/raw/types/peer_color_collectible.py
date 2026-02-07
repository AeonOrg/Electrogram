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


class PeerColorCollectible(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PeerColor`.

    Details:
        - Layer: ``224``
        - ID: ``B9C0639A``

    Parameters:
        collectible_id (``int`` ``64-bit``):
            N/A

        gift_emoji_id (``int`` ``64-bit``):
            N/A

        background_emoji_id (``int`` ``64-bit``):
            N/A

        accent_color (``int`` ``32-bit``):
            N/A

        colors (List of ``int`` ``32-bit``):
            N/A

        dark_accent_color (``int`` ``32-bit``, *optional*):
            N/A

        dark_colors (List of ``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["collectible_id", "gift_emoji_id", "background_emoji_id", "accent_color", "colors", "dark_accent_color", "dark_colors"]

    ID = 0xb9c0639a
    QUALNAME = "types.PeerColorCollectible"

    def __init__(self, *, collectible_id: int, gift_emoji_id: int, background_emoji_id: int, accent_color: int, colors: List[int], dark_accent_color: Optional[int] = None, dark_colors: Optional[List[int]] = None) -> None:
        self.collectible_id = collectible_id  # long
        self.gift_emoji_id = gift_emoji_id  # long
        self.background_emoji_id = background_emoji_id  # long
        self.accent_color = accent_color  # int
        self.colors = colors  # Vector<int>
        self.dark_accent_color = dark_accent_color  # flags.0?int
        self.dark_colors = dark_colors  # flags.1?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorCollectible":

        flags = Int.read(b)

        collectible_id = Long.read(b)

        gift_emoji_id = Long.read(b)

        background_emoji_id = Long.read(b)

        accent_color = Int.read(b)

        colors = TLObject.read(b, Int)

        dark_accent_color = Int.read(b) if flags & (1 << 0) else None
        dark_colors = TLObject.read(b, Int) if flags & (1 << 1) else []

        return PeerColorCollectible(collectible_id=collectible_id, gift_emoji_id=gift_emoji_id, background_emoji_id=background_emoji_id, accent_color=accent_color, colors=colors, dark_accent_color=dark_accent_color, dark_colors=dark_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark_accent_color is not None else 0
        flags |= (1 << 1) if self.dark_colors else 0
        b.write(Int(flags))

        b.write(Long(self.collectible_id))

        b.write(Long(self.gift_emoji_id))

        b.write(Long(self.background_emoji_id))

        b.write(Int(self.accent_color))

        b.write(Vector(self.colors, Int))

        if self.dark_accent_color is not None:
            b.write(Int(self.dark_accent_color))

        if self.dark_colors is not None:
            b.write(Vector(self.dark_colors, Int))

        return b.getvalue()
