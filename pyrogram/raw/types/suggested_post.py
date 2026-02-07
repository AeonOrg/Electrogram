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


class SuggestedPost(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SuggestedPost`.

    Details:
        - Layer: ``224``
        - ID: ``E8E37E5``

    Parameters:
        accepted (``bool``, *optional*):
            N/A

        rejected (``bool``, *optional*):
            N/A

        price (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["accepted", "rejected", "price", "schedule_date"]

    ID = 0xe8e37e5
    QUALNAME = "types.SuggestedPost"

    def __init__(self, *, accepted: Optional[bool] = None, rejected: Optional[bool] = None, price: "raw.base.StarsAmount" = None, schedule_date: Optional[int] = None) -> None:
        self.accepted = accepted  # flags.1?true
        self.rejected = rejected  # flags.2?true
        self.price = price  # flags.3?StarsAmount
        self.schedule_date = schedule_date  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SuggestedPost":

        flags = Int.read(b)

        accepted = True if flags & (1 << 1) else False
        rejected = True if flags & (1 << 2) else False
        price = TLObject.read(b) if flags & (1 << 3) else None

        schedule_date = Int.read(b) if flags & (1 << 0) else None
        return SuggestedPost(accepted=accepted, rejected=rejected, price=price, schedule_date=schedule_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.accepted else 0
        flags |= (1 << 2) if self.rejected else 0
        flags |= (1 << 3) if self.price is not None else 0
        flags |= (1 << 0) if self.schedule_date is not None else 0
        b.write(Int(flags))

        if self.price is not None:
            b.write(self.price.write())

        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))

        return b.getvalue()
