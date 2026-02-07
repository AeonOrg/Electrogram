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


class StarGiftAttributeRarityUncommon(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttributeRarity`.

    Details:
        - Layer: ``224``
        - ID: ``DBCE6389``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xdbce6389
    QUALNAME = "types.StarGiftAttributeRarityUncommon"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeRarityUncommon":
        # No flags

        return StarGiftAttributeRarityUncommon()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
