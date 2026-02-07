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


class MessageActionSuggestedPostApproval(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``EE7A1596``

    Parameters:
        rejected (``bool``, *optional*):
            N/A

        balance_too_low (``bool``, *optional*):
            N/A

        reject_comment (``str``, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

        price (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["rejected", "balance_too_low", "reject_comment", "schedule_date", "price"]

    ID = 0xee7a1596
    QUALNAME = "types.MessageActionSuggestedPostApproval"

    def __init__(self, *, rejected: Optional[bool] = None, balance_too_low: Optional[bool] = None, reject_comment: Optional[str] = None, schedule_date: Optional[int] = None, price: "raw.base.StarsAmount" = None) -> None:
        self.rejected = rejected  # flags.0?true
        self.balance_too_low = balance_too_low  # flags.1?true
        self.reject_comment = reject_comment  # flags.2?string
        self.schedule_date = schedule_date  # flags.3?int
        self.price = price  # flags.4?StarsAmount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSuggestedPostApproval":

        flags = Int.read(b)

        rejected = True if flags & (1 << 0) else False
        balance_too_low = True if flags & (1 << 1) else False
        reject_comment = String.read(b) if flags & (1 << 2) else None
        schedule_date = Int.read(b) if flags & (1 << 3) else None
        price = TLObject.read(b) if flags & (1 << 4) else None

        return MessageActionSuggestedPostApproval(rejected=rejected, balance_too_low=balance_too_low, reject_comment=reject_comment, schedule_date=schedule_date, price=price)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rejected else 0
        flags |= (1 << 1) if self.balance_too_low else 0
        flags |= (1 << 2) if self.reject_comment is not None else 0
        flags |= (1 << 3) if self.schedule_date is not None else 0
        flags |= (1 << 4) if self.price is not None else 0
        b.write(Int(flags))

        if self.reject_comment is not None:
            b.write(String(self.reject_comment))

        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))

        if self.price is not None:
            b.write(self.price.write())

        return b.getvalue()
