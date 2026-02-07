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


class SuggestedStarRefBots(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.SuggestedStarRefBots`.

    Details:
        - Layer: ``224``
        - ID: ``B4D5D859``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        suggested_bots (List of :obj:`StarRefProgram <pyrogram.raw.base.StarRefProgram>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetSuggestedStarRefBots
    """

    __slots__: List[str] = ["count", "suggested_bots", "users", "next_offset"]

    ID = 0xb4d5d859
    QUALNAME = "types.payments.SuggestedStarRefBots"

    def __init__(self, *, count: int, suggested_bots: List["raw.base.StarRefProgram"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.suggested_bots = suggested_bots  # Vector<StarRefProgram>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SuggestedStarRefBots":

        flags = Int.read(b)

        count = Int.read(b)

        suggested_bots = TLObject.read(b)

        users = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        return SuggestedStarRefBots(count=count, suggested_bots=suggested_bots, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Vector(self.suggested_bots))

        b.write(Vector(self.users))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        return b.getvalue()
