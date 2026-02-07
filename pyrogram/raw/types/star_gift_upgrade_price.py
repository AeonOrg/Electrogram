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


class StarGiftUpgradePrice(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftUpgradePrice`.

    Details:
        - Layer: ``224``
        - ID: ``99EA331D``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        upgrade_stars (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["date", "upgrade_stars"]

    ID = 0x99ea331d
    QUALNAME = "types.StarGiftUpgradePrice"

    def __init__(self, *, date: int, upgrade_stars: int) -> None:
        self.date = date  # int
        self.upgrade_stars = upgrade_stars  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftUpgradePrice":
        # No flags

        date = Int.read(b)

        upgrade_stars = Long.read(b)

        return StarGiftUpgradePrice(date=date, upgrade_stars=upgrade_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.date))

        b.write(Long(self.upgrade_stars))

        return b.getvalue()
