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


class BotPreparedInlineMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.BotPreparedInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``8ECF0511``

    Parameters:
        id (``str``):
            N/A

        expire_date (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SavePreparedInlineMessage
    """

    __slots__: List[str] = ["id", "expire_date"]

    ID = 0x8ecf0511
    QUALNAME = "types.messages.BotPreparedInlineMessage"

    def __init__(self, *, id: str, expire_date: int) -> None:
        self.id = id  # string
        self.expire_date = expire_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotPreparedInlineMessage":
        # No flags

        id = String.read(b)

        expire_date = Int.read(b)

        return BotPreparedInlineMessage(id=id, expire_date=expire_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.id))

        b.write(Int(self.expire_date))

        return b.getvalue()
