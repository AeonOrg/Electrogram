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


class AuctionBidLevel(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AuctionBidLevel`.

    Details:
        - Layer: ``224``
        - ID: ``310240CC``

    Parameters:
        pos (``int`` ``32-bit``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["pos", "amount", "date"]

    ID = 0x310240cc
    QUALNAME = "types.AuctionBidLevel"

    def __init__(self, *, pos: int, amount: int, date: int) -> None:
        self.pos = pos  # int
        self.amount = amount  # long
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AuctionBidLevel":
        # No flags

        pos = Int.read(b)

        amount = Long.read(b)

        date = Int.read(b)

        return AuctionBidLevel(pos=pos, amount=amount, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.pos))

        b.write(Long(self.amount))

        b.write(Int(self.date))

        return b.getvalue()
