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


class StarRefProgram(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarRefProgram`.

    Details:
        - Layer: ``224``
        - ID: ``DD0C66F2``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        commission_permille (``int`` ``32-bit``):
            N/A

        duration_months (``int`` ``32-bit``, *optional*):
            N/A

        end_date (``int`` ``32-bit``, *optional*):
            N/A

        daily_revenue_per_user (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.UpdateStarRefProgram
    """

    __slots__: List[str] = ["bot_id", "commission_permille", "duration_months", "end_date", "daily_revenue_per_user"]

    ID = 0xdd0c66f2
    QUALNAME = "types.StarRefProgram"

    def __init__(self, *, bot_id: int, commission_permille: int, duration_months: Optional[int] = None, end_date: Optional[int] = None, daily_revenue_per_user: "raw.base.StarsAmount" = None) -> None:
        self.bot_id = bot_id  # long
        self.commission_permille = commission_permille  # int
        self.duration_months = duration_months  # flags.0?int
        self.end_date = end_date  # flags.1?int
        self.daily_revenue_per_user = daily_revenue_per_user  # flags.2?StarsAmount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarRefProgram":

        flags = Int.read(b)

        bot_id = Long.read(b)

        commission_permille = Int.read(b)

        duration_months = Int.read(b) if flags & (1 << 0) else None
        end_date = Int.read(b) if flags & (1 << 1) else None
        daily_revenue_per_user = TLObject.read(b) if flags & (1 << 2) else None

        return StarRefProgram(bot_id=bot_id, commission_permille=commission_permille, duration_months=duration_months, end_date=end_date, daily_revenue_per_user=daily_revenue_per_user)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.duration_months is not None else 0
        flags |= (1 << 1) if self.end_date is not None else 0
        flags |= (1 << 2) if self.daily_revenue_per_user is not None else 0
        b.write(Int(flags))

        b.write(Long(self.bot_id))

        b.write(Int(self.commission_permille))

        if self.duration_months is not None:
            b.write(Int(self.duration_months))

        if self.end_date is not None:
            b.write(Int(self.end_date))

        if self.daily_revenue_per_user is not None:
            b.write(self.daily_revenue_per_user.write())

        return b.getvalue()
