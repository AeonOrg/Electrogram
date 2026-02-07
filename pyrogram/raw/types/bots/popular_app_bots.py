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


class PopularAppBots(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.bots.PopularAppBots`.

    Details:
        - Layer: ``224``
        - ID: ``1991B13B``

    Parameters:
        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetPopularAppBots
    """

    __slots__: List[str] = ["users", "next_offset"]

    ID = 0x1991b13b
    QUALNAME = "types.bots.PopularAppBots"

    def __init__(self, *, users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PopularAppBots":

        flags = Int.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        users = TLObject.read(b)

        return PopularAppBots(users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        b.write(Vector(self.users))

        return b.getvalue()
