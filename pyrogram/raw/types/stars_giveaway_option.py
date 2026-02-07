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


class StarsGiveawayOption(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsGiveawayOption`.

    Details:
        - Layer: ``224``
        - ID: ``94CE852A``

    Parameters:
        stars (``int`` ``64-bit``):
            N/A

        yearly_boosts (``int`` ``32-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        winners (List of :obj:`StarsGiveawayWinnersOption <pyrogram.raw.base.StarsGiveawayWinnersOption>`):
            N/A

        extended (``bool``, *optional*):
            N/A

        default (``bool``, *optional*):
            N/A

        store_product (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarsGiveawayOptions
    """

    __slots__: List[str] = ["stars", "yearly_boosts", "currency", "amount", "winners", "extended", "default", "store_product"]

    ID = 0x94ce852a
    QUALNAME = "types.StarsGiveawayOption"

    def __init__(self, *, stars: int, yearly_boosts: int, currency: str, amount: int, winners: List["raw.base.StarsGiveawayWinnersOption"], extended: Optional[bool] = None, default: Optional[bool] = None, store_product: Optional[str] = None) -> None:
        self.stars = stars  # long
        self.yearly_boosts = yearly_boosts  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.winners = winners  # Vector<StarsGiveawayWinnersOption>
        self.extended = extended  # flags.0?true
        self.default = default  # flags.1?true
        self.store_product = store_product  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsGiveawayOption":

        flags = Int.read(b)

        extended = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        stars = Long.read(b)

        yearly_boosts = Int.read(b)

        store_product = String.read(b) if flags & (1 << 2) else None
        currency = String.read(b)

        amount = Long.read(b)

        winners = TLObject.read(b)

        return StarsGiveawayOption(stars=stars, yearly_boosts=yearly_boosts, currency=currency, amount=amount, winners=winners, extended=extended, default=default, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.extended else 0
        flags |= (1 << 1) if self.default else 0
        flags |= (1 << 2) if self.store_product is not None else 0
        b.write(Int(flags))

        b.write(Long(self.stars))

        b.write(Int(self.yearly_boosts))

        if self.store_product is not None:
            b.write(String(self.store_product))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        b.write(Vector(self.winners))

        return b.getvalue()
