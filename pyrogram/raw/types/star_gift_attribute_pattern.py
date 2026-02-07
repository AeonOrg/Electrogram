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


class StarGiftAttributePattern(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttribute`.

    Details:
        - Layer: ``224``
        - ID: ``4E7085EA``

    Parameters:
        name (``str``):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        rarity (:obj:`StarGiftAttributeRarity <pyrogram.raw.base.StarGiftAttributeRarity>`):
            N/A

    """

    __slots__: List[str] = ["name", "document", "rarity"]

    ID = 0x4e7085ea
    QUALNAME = "types.StarGiftAttributePattern"

    def __init__(self, *, name: str, document: "raw.base.Document", rarity: "raw.base.StarGiftAttributeRarity") -> None:
        self.name = name  # string
        self.document = document  # Document
        self.rarity = rarity  # StarGiftAttributeRarity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributePattern":
        # No flags

        name = String.read(b)

        document = TLObject.read(b)

        rarity = TLObject.read(b)

        return StarGiftAttributePattern(name=name, document=document, rarity=rarity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.name))

        b.write(self.document.write())

        b.write(self.rarity.write())

        return b.getvalue()
