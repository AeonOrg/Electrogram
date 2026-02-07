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


class StarGiftAttributeBackdrop(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``9F2504E4``

    Parameters:
        name (``str``):
            N/A

        backdrop_id (``int`` ``32-bit``):
            N/A

        center_color (``int`` ``32-bit``):
            N/A

        edge_color (``int`` ``32-bit``):
            N/A

        pattern_color (``int`` ``32-bit``):
            N/A

        text_color (``int`` ``32-bit``):
            N/A

        rarity (:obj:`StarGiftAttributeRarity <pyrogram.raw.base.StarGiftAttributeRarity>`):
            N/A

    """

    __slots__: List[str] = ["name", "backdrop_id", "center_color", "edge_color", "pattern_color", "text_color", "rarity"]

    ID = 0x9f2504e4
    QUALNAME = "types.StarGiftAttributeBackdrop"

    def __init__(self, *, name: str, backdrop_id: int, center_color: int, edge_color: int, pattern_color: int, text_color: int, rarity: "raw.base.StarGiftAttributeRarity") -> None:
        self.name = name  # string
        self.backdrop_id = backdrop_id  # int
        self.center_color = center_color  # int
        self.edge_color = edge_color  # int
        self.pattern_color = pattern_color  # int
        self.text_color = text_color  # int
        self.rarity = rarity  # StarGiftAttributeRarity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeBackdrop":
        # No flags

        name = String.read(b)

        backdrop_id = Int.read(b)

        center_color = Int.read(b)

        edge_color = Int.read(b)

        pattern_color = Int.read(b)

        text_color = Int.read(b)

        rarity = TLObject.read(b)

        return StarGiftAttributeBackdrop(name=name, backdrop_id=backdrop_id, center_color=center_color, edge_color=edge_color, pattern_color=pattern_color, text_color=text_color, rarity=rarity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.name))

        b.write(Int(self.backdrop_id))

        b.write(Int(self.center_color))

        b.write(Int(self.edge_color))

        b.write(Int(self.pattern_color))

        b.write(Int(self.text_color))

        b.write(self.rarity.write())

        return b.getvalue()
