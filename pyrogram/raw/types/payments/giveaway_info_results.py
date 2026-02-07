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


class GiveawayInfoResults(TLObject):  # type: ignore
    """A giveaway has ended.

    Constructor of :obj:`~pyrogram.raw.base.payments.GiveawayInfo`.

    Details:
        - Layer: ``224``
        - ID: ``E175E66F``

    Parameters:
        start_date (``int`` ``32-bit``):
            Start date of the giveaway

        finish_date (``int`` ``32-bit``):
            End date of the giveaway. May be bigger than the end date specified in parameters of the giveaway.

        winners_count (``int`` ``32-bit``):
            Number of winners in the giveaway

        winner (``bool``, *optional*):
            Whether we're one of the winners of this giveaway.

        refunded (``bool``, *optional*):
            Whether the giveaway was canceled and was fully refunded.

        gift_code_slug (``str``, *optional*):
            If we're one of the winners of this giveaway, contains the Premium gift code, see here » for more info on the full giveaway flow.

        stars_prize (``int`` ``64-bit``, *optional*):
            N/A

        activated_count (``int`` ``32-bit``, *optional*):
            Number of winners, which activated their gift codes.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetGiveawayInfo
    """

    __slots__: List[str] = ["start_date", "finish_date", "winners_count", "winner", "refunded", "gift_code_slug", "stars_prize", "activated_count"]

    ID = 0xe175e66f
    QUALNAME = "types.payments.GiveawayInfoResults"

    def __init__(self, *, start_date: int, finish_date: int, winners_count: int, winner: Optional[bool] = None, refunded: Optional[bool] = None, gift_code_slug: Optional[str] = None, stars_prize: Optional[int] = None, activated_count: Optional[int] = None) -> None:
        self.start_date = start_date  # int
        self.finish_date = finish_date  # int
        self.winners_count = winners_count  # int
        self.winner = winner  # flags.0?true
        self.refunded = refunded  # flags.1?true
        self.gift_code_slug = gift_code_slug  # flags.3?string
        self.stars_prize = stars_prize  # flags.4?long
        self.activated_count = activated_count  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GiveawayInfoResults":

        flags = Int.read(b)

        winner = True if flags & (1 << 0) else False
        refunded = True if flags & (1 << 1) else False
        start_date = Int.read(b)

        gift_code_slug = String.read(b) if flags & (1 << 3) else None
        stars_prize = Long.read(b) if flags & (1 << 4) else None
        finish_date = Int.read(b)

        winners_count = Int.read(b)

        activated_count = Int.read(b) if flags & (1 << 2) else None
        return GiveawayInfoResults(start_date=start_date, finish_date=finish_date, winners_count=winners_count, winner=winner, refunded=refunded, gift_code_slug=gift_code_slug, stars_prize=stars_prize, activated_count=activated_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.winner else 0
        flags |= (1 << 1) if self.refunded else 0
        flags |= (1 << 3) if self.gift_code_slug is not None else 0
        flags |= (1 << 4) if self.stars_prize is not None else 0
        flags |= (1 << 2) if self.activated_count is not None else 0
        b.write(Int(flags))

        b.write(Int(self.start_date))

        if self.gift_code_slug is not None:
            b.write(String(self.gift_code_slug))

        if self.stars_prize is not None:
            b.write(Long(self.stars_prize))

        b.write(Int(self.finish_date))

        b.write(Int(self.winners_count))

        if self.activated_count is not None:
            b.write(Int(self.activated_count))

        return b.getvalue()
