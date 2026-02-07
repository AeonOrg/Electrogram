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


class ConnectedBotStarRef(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ConnectedBotStarRef`.

    Details:
        - Layer: ``224``
        - ID: ``19A13F71``

    Parameters:
        url (``str``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        bot_id (``int`` ``64-bit``):
            N/A

        commission_permille (``int`` ``32-bit``):
            N/A

        participants (``int`` ``64-bit``):
            N/A

        revenue (``int`` ``64-bit``):
            N/A

        revoked (``bool``, *optional*):
            N/A

        duration_months (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["url", "date", "bot_id", "commission_permille", "participants", "revenue", "revoked", "duration_months"]

    ID = 0x19a13f71
    QUALNAME = "types.ConnectedBotStarRef"

    def __init__(self, *, url: str, date: int, bot_id: int, commission_permille: int, participants: int, revenue: int, revoked: Optional[bool] = None, duration_months: Optional[int] = None) -> None:
        self.url = url  # string
        self.date = date  # int
        self.bot_id = bot_id  # long
        self.commission_permille = commission_permille  # int
        self.participants = participants  # long
        self.revenue = revenue  # long
        self.revoked = revoked  # flags.1?true
        self.duration_months = duration_months  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConnectedBotStarRef":

        flags = Int.read(b)

        revoked = True if flags & (1 << 1) else False
        url = String.read(b)

        date = Int.read(b)

        bot_id = Long.read(b)

        commission_permille = Int.read(b)

        duration_months = Int.read(b) if flags & (1 << 0) else None
        participants = Long.read(b)

        revenue = Long.read(b)

        return ConnectedBotStarRef(url=url, date=date, bot_id=bot_id, commission_permille=commission_permille, participants=participants, revenue=revenue, revoked=revoked, duration_months=duration_months)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.revoked else 0
        flags |= (1 << 0) if self.duration_months is not None else 0
        b.write(Int(flags))

        b.write(String(self.url))

        b.write(Int(self.date))

        b.write(Long(self.bot_id))

        b.write(Int(self.commission_permille))

        if self.duration_months is not None:
            b.write(Int(self.duration_months))

        b.write(Long(self.participants))

        b.write(Long(self.revenue))

        return b.getvalue()
