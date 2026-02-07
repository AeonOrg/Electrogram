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


class StarGiftAttributeCounter(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttributeCounter`.

    Details:
        - Layer: ``224``
        - ID: ``2EB1B658``

    Parameters:
        attribute (:obj:`StarGiftAttributeId <pyrogram.raw.base.StarGiftAttributeId>`):
            N/A

        count (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["attribute", "count"]

    ID = 0x2eb1b658
    QUALNAME = "types.StarGiftAttributeCounter"

    def __init__(self, *, attribute: "raw.base.StarGiftAttributeId", count: int) -> None:
        self.attribute = attribute  # StarGiftAttributeId
        self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeCounter":
        # No flags

        attribute = TLObject.read(b)

        count = Int.read(b)

        return StarGiftAttributeCounter(attribute=attribute, count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.attribute.write())

        b.write(Int(self.count))

        return b.getvalue()
