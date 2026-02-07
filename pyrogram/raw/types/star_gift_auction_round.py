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


class StarGiftAuctionRound(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAuctionRound`.

    Details:
        - Layer: ``224``
        - ID: ``3AAE0528``

    Parameters:
        num (``int`` ``32-bit``):
            N/A

        duration (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["num", "duration"]

    ID = 0x3aae0528
    QUALNAME = "types.StarGiftAuctionRound"

    def __init__(self, *, num: int, duration: int) -> None:
        self.num = num  # int
        self.duration = duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionRound":
        # No flags

        num = Int.read(b)

        duration = Int.read(b)

        return StarGiftAuctionRound(num=num, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.num))

        b.write(Int(self.duration))

        return b.getvalue()
