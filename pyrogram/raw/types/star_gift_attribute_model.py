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


class StarGiftAttributeModel(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``565251E2``

    Parameters:
        name (``str``):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        rarity (:obj:`StarGiftAttributeRarity <pyrogram.raw.base.StarGiftAttributeRarity>`):
            N/A

        crafted (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["name", "document", "rarity", "crafted"]

    ID = 0x565251e2
    QUALNAME = "types.StarGiftAttributeModel"

    def __init__(self, *, name: str, document: "raw.base.Document", rarity: "raw.base.StarGiftAttributeRarity", crafted: Optional[bool] = None) -> None:
        self.name = name  # string
        self.document = document  # Document
        self.rarity = rarity  # StarGiftAttributeRarity
        self.crafted = crafted  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeModel":

        flags = Int.read(b)

        crafted = True if flags & (1 << 0) else False
        name = String.read(b)

        document = TLObject.read(b)

        rarity = TLObject.read(b)

        return StarGiftAttributeModel(name=name, document=document, rarity=rarity, crafted=crafted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.crafted else 0
        b.write(Int(flags))

        b.write(String(self.name))

        b.write(self.document.write())

        b.write(self.rarity.write())

        return b.getvalue()
