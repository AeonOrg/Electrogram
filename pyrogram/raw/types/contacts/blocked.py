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


class Blocked(TLObject):  # type: ignore
    """Full list of blocked users.

    Constructor of :obj:`~pyrogram.raw.base.contacts.Blocked`.

    Details:
        - Layer: ``224``
        - ID: ``ADE1591``

    Parameters:
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

    __slots__: List[str] = ["blocked", "chats", "users"]

    ID = 0xade1591
    QUALNAME = "types.contacts.Blocked"

    def __init__(self, *, blocked: List["raw.base.PeerBlocked"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.blocked = blocked  # Vector<PeerBlocked>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Blocked":
        # No flags

        blocked = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return Blocked(blocked=blocked, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.blocked))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
