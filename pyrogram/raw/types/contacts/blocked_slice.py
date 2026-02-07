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


class BlockedSlice(TLObject):  # type: ignore
    """Incomplete list of blocked users.

    Constructor of :obj:`~pyrogram.raw.base.contacts.Blocked`.

    Details:
        - Layer: ``224``
        - ID: ``E1664194``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of elements in the list

        blocked (List of :obj:`PeerBlocked <pyrogram.raw.base.PeerBlocked>`):
            List of blocked users

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Blocked chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetBlocked
    """

    __slots__: List[str] = ["count", "blocked", "chats", "users"]

    ID = 0xe1664194
    QUALNAME = "types.contacts.BlockedSlice"

    def __init__(self, *, count: int, blocked: List["raw.base.PeerBlocked"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.count = count  # int
        self.blocked = blocked  # Vector<PeerBlocked>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BlockedSlice":
        # No flags

        count = Int.read(b)

        blocked = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return BlockedSlice(count=count, blocked=blocked, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.count))

        b.write(Vector(self.blocked))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
