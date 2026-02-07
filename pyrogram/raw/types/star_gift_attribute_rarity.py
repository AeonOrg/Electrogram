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


class StarGiftAttributeRarity(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAttributeRarity`.

    Details:
        - Layer: ``224``
        - ID: ``36437737``

    Parameters:
        permille (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["permille"]

    ID = 0x36437737
    QUALNAME = "types.StarGiftAttributeRarity"

    def __init__(self, *, permille: int) -> None:
        self.permille = permille  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAttributeRarity":
        # No flags

        permille = Int.read(b)

        return StarGiftAttributeRarity(permille=permille)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.permille))

        return b.getvalue()
