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


class Passkey(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Passkey`.

    Details:
        - Layer: ``224``
        - ID: ``98613EBF``

    Parameters:
        id (``str``):
            N/A

        name (``str``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        software_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

        last_usage_date (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.RegisterPasskey
    """

    __slots__: List[str] = ["id", "name", "date", "software_emoji_id", "last_usage_date"]

    ID = 0x98613ebf
    QUALNAME = "types.Passkey"

    def __init__(self, *, id: str, name: str, date: int, software_emoji_id: Optional[int] = None, last_usage_date: Optional[int] = None) -> None:
        self.id = id  # string
        self.name = name  # string
        self.date = date  # int
        self.software_emoji_id = software_emoji_id  # flags.0?long
        self.last_usage_date = last_usage_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Passkey":

        flags = Int.read(b)

        id = String.read(b)

        name = String.read(b)

        date = Int.read(b)

        software_emoji_id = Long.read(b) if flags & (1 << 0) else None
        last_usage_date = Int.read(b) if flags & (1 << 1) else None
        return Passkey(id=id, name=name, date=date, software_emoji_id=software_emoji_id, last_usage_date=last_usage_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.software_emoji_id is not None else 0
        flags |= (1 << 1) if self.last_usage_date is not None else 0
        b.write(Int(flags))

        b.write(String(self.id))

        b.write(String(self.name))

        b.write(Int(self.date))

        if self.software_emoji_id is not None:
            b.write(Long(self.software_emoji_id))

        if self.last_usage_date is not None:
            b.write(Int(self.last_usage_date))

        return b.getvalue()
