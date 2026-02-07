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


class Boost(TLObject):  # type: ignore
    """Info about one or more boosts applied by a specific user.

    Constructor of :obj:`~pyrogram.raw.base.Boost`.

    Details:
        - Layer: ``224``
        - ID: ``4B3E14D6``

    Parameters:
        id (``str``):
            Unique ID for this set of boosts.

        date (``int`` ``32-bit``):
            When was the boost applied

        expires (``int`` ``32-bit``):
            When does the boost expire

        gift (``bool``, *optional*):
            Whether this boost was applied because the channel directly gifted a subscription to the user.

        giveaway (``bool``, *optional*):
            Whether this boost was applied because the user was chosen in a giveaway started by the channel.

        unclaimed (``bool``, *optional*):
            If set, the user hasn't yet invoked payments.applyGiftCode to claim a subscription gifted directly or in a giveaway by the channel.

        user_id (``int`` ``64-bit``, *optional*):
            ID of the user that applied the boost.

        giveaway_msg_id (``int`` ``32-bit``, *optional*):
            The message ID of the giveaway

        used_gift_slug (``str``, *optional*):
            The created Telegram Premium gift code, only set if either gift or giveaway are set AND it is either a gift code for the currently logged in user or if it was already claimed.

        multiplier (``int`` ``32-bit``, *optional*):
            If set, this boost counts as multiplier boosts, otherwise it counts as a single boost.

        stars (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "date", "expires", "gift", "giveaway", "unclaimed", "user_id", "giveaway_msg_id", "used_gift_slug", "multiplier", "stars"]

    ID = 0x4b3e14d6
    QUALNAME = "types.Boost"

    def __init__(self, *, id: str, date: int, expires: int, gift: Optional[bool] = None, giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, user_id: Optional[int] = None, giveaway_msg_id: Optional[int] = None, used_gift_slug: Optional[str] = None, multiplier: Optional[int] = None, stars: Optional[int] = None) -> None:
        self.id = id  # string
        self.date = date  # int
        self.expires = expires  # int
        self.gift = gift  # flags.1?true
        self.giveaway = giveaway  # flags.2?true
        self.unclaimed = unclaimed  # flags.3?true
        self.user_id = user_id  # flags.0?long
        self.giveaway_msg_id = giveaway_msg_id  # flags.2?int
        self.used_gift_slug = used_gift_slug  # flags.4?string
        self.multiplier = multiplier  # flags.5?int
        self.stars = stars  # flags.6?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Boost":

        flags = Int.read(b)

        gift = True if flags & (1 << 1) else False
        giveaway = True if flags & (1 << 2) else False
        unclaimed = True if flags & (1 << 3) else False
        id = String.read(b)

        user_id = Long.read(b) if flags & (1 << 0) else None
        giveaway_msg_id = Int.read(b) if flags & (1 << 2) else None
        date = Int.read(b)

        expires = Int.read(b)

        used_gift_slug = String.read(b) if flags & (1 << 4) else None
        multiplier = Int.read(b) if flags & (1 << 5) else None
        stars = Long.read(b) if flags & (1 << 6) else None
        return Boost(id=id, date=date, expires=expires, gift=gift, giveaway=giveaway, unclaimed=unclaimed, user_id=user_id, giveaway_msg_id=giveaway_msg_id, used_gift_slug=used_gift_slug, multiplier=multiplier, stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.gift else 0
        flags |= (1 << 2) if self.giveaway else 0
        flags |= (1 << 3) if self.unclaimed else 0
        flags |= (1 << 0) if self.user_id is not None else 0
        flags |= (1 << 2) if self.giveaway_msg_id is not None else 0
        flags |= (1 << 4) if self.used_gift_slug is not None else 0
        flags |= (1 << 5) if self.multiplier is not None else 0
        flags |= (1 << 6) if self.stars is not None else 0
        b.write(Int(flags))

        b.write(String(self.id))

        if self.user_id is not None:
            b.write(Long(self.user_id))

        if self.giveaway_msg_id is not None:
            b.write(Int(self.giveaway_msg_id))

        b.write(Int(self.date))

        b.write(Int(self.expires))

        if self.used_gift_slug is not None:
            b.write(String(self.used_gift_slug))

        if self.multiplier is not None:
            b.write(Int(self.multiplier))

        if self.stars is not None:
            b.write(Long(self.stars))

        return b.getvalue()
