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


class StarGiftAuctionRoundExtendable(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAuctionRound`.

    Details:
        - Layer: ``224``
        - ID: ``AA021E5``

    Parameters:
        num (``int`` ``32-bit``):
            N/A

        duration (``int`` ``32-bit``):
            N/A

        extend_top (``int`` ``32-bit``):
            N/A

        extend_window (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["num", "duration", "extend_top", "extend_window"]

    ID = 0xaa021e5
    QUALNAME = "types.StarGiftAuctionRoundExtendable"

    def __init__(self, *, num: int, duration: int, extend_top: int, extend_window: int) -> None:
        self.num = num  # int
        self.duration = duration  # int
        self.extend_top = extend_top  # int
        self.extend_window = extend_window  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionRoundExtendable":
        # No flags

        num = Int.read(b)

        duration = Int.read(b)

        extend_top = Int.read(b)

        extend_window = Int.read(b)

        return StarGiftAuctionRoundExtendable(num=num, duration=duration, extend_top=extend_top, extend_window=extend_window)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.num))

        b.write(Int(self.duration))

        b.write(Int(self.extend_top))

        b.write(Int(self.extend_window))

        return b.getvalue()
