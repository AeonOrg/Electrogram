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


class StarGiftAuctionState(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAuctionState`.

    Details:
        - Layer: ``224``
        - ID: ``771A4E66``

    Parameters:
        version (``int`` ``32-bit``):
            N/A

        start_date (``int`` ``32-bit``):
            N/A

        end_date (``int`` ``32-bit``):
            N/A

        min_bid_amount (``int`` ``64-bit``):
            N/A

        bid_levels (List of :obj:`AuctionBidLevel <pyrogram.raw.base.AuctionBidLevel>`):
            N/A

        top_bidders (List of ``int`` ``64-bit``):
            N/A

        next_round_at (``int`` ``32-bit``):
            N/A

        last_gift_num (``int`` ``32-bit``):
            N/A

        gifts_left (``int`` ``32-bit``):
            N/A

        current_round (``int`` ``32-bit``):
            N/A

        total_rounds (``int`` ``32-bit``):
            N/A

        rounds (List of :obj:`StarGiftAuctionRound <pyrogram.raw.base.StarGiftAuctionRound>`):
            N/A

    """

    __slots__: List[str] = ["version", "start_date", "end_date", "min_bid_amount", "bid_levels", "top_bidders", "next_round_at", "last_gift_num", "gifts_left", "current_round", "total_rounds", "rounds"]

    ID = 0x771a4e66
    QUALNAME = "types.StarGiftAuctionState"

    def __init__(self, *, version: int, start_date: int, end_date: int, min_bid_amount: int, bid_levels: List["raw.base.AuctionBidLevel"], top_bidders: List[int], next_round_at: int, last_gift_num: int, gifts_left: int, current_round: int, total_rounds: int, rounds: List["raw.base.StarGiftAuctionRound"]) -> None:
        self.version = version  # int
        self.start_date = start_date  # int
        self.end_date = end_date  # int
        self.min_bid_amount = min_bid_amount  # long
        self.bid_levels = bid_levels  # Vector<AuctionBidLevel>
        self.top_bidders = top_bidders  # Vector<long>
        self.next_round_at = next_round_at  # int
        self.last_gift_num = last_gift_num  # int
        self.gifts_left = gifts_left  # int
        self.current_round = current_round  # int
        self.total_rounds = total_rounds  # int
        self.rounds = rounds  # Vector<StarGiftAuctionRound>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionState":
        # No flags

        version = Int.read(b)

        start_date = Int.read(b)

        end_date = Int.read(b)

        min_bid_amount = Long.read(b)

        bid_levels = TLObject.read(b)

        top_bidders = TLObject.read(b, Long)

        next_round_at = Int.read(b)

        last_gift_num = Int.read(b)

        gifts_left = Int.read(b)

        current_round = Int.read(b)

        total_rounds = Int.read(b)

        rounds = TLObject.read(b)

        return StarGiftAuctionState(version=version, start_date=start_date, end_date=end_date, min_bid_amount=min_bid_amount, bid_levels=bid_levels, top_bidders=top_bidders, next_round_at=next_round_at, last_gift_num=last_gift_num, gifts_left=gifts_left, current_round=current_round, total_rounds=total_rounds, rounds=rounds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.version))

        b.write(Int(self.start_date))

        b.write(Int(self.end_date))

        b.write(Long(self.min_bid_amount))

        b.write(Vector(self.bid_levels))

        b.write(Vector(self.top_bidders, Long))

        b.write(Int(self.next_round_at))

        b.write(Int(self.last_gift_num))

        b.write(Int(self.gifts_left))

        b.write(Int(self.current_round))

        b.write(Int(self.total_rounds))

        b.write(Vector(self.rounds))

        return b.getvalue()
