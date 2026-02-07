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


class BoostsList(TLObject):  # type: ignore
    """List of boosts that were applied to a peer by multiple users.

    Constructor of :obj:`~pyrogram.raw.base.premium.BoostsList`.

    Details:
        - Layer: ``224``
        - ID: ``86F8613C``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of results

        boosts (List of :obj:`Boost <pyrogram.raw.base.Boost>`):
            Boosts

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Mentioned users

        next_offset (``str``, *optional*):
            Offset that can be used for pagination.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            premium.GetBoostsList
            premium.GetUserBoosts
    """

    __slots__: List[str] = ["count", "boosts", "users", "next_offset"]

    ID = 0x86f8613c
    QUALNAME = "types.premium.BoostsList"

    def __init__(self, *, count: int, boosts: List["raw.base.Boost"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.boosts = boosts  # Vector<Boost>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BoostsList":

        flags = Int.read(b)

        count = Int.read(b)

        boosts = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        users = TLObject.read(b)

        return BoostsList(count=count, boosts=boosts, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Vector(self.boosts))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        b.write(Vector(self.users))

        return b.getvalue()
