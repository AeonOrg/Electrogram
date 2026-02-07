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


class MessageViews(TLObject):  # type: ignore
    """View, forward counter + info about replies

    Constructor of :obj:`~pyrogram.raw.base.messages.MessageViews`.

    Details:
        - Layer: ``224``
        - ID: ``B6C4F543``

    Parameters:
        views (List of :obj:`MessageViews <pyrogram.raw.base.MessageViews>`):
            View, forward counter + info about replies

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats mentioned in constructor

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users mentioned in constructor

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessagesViews
    """

    __slots__: List[str] = ["views", "chats", "users"]

    ID = 0xb6c4f543
    QUALNAME = "types.messages.MessageViews"

    def __init__(self, *, views: List["raw.base.MessageViews"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.views = views  # Vector<MessageViews>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageViews":
        # No flags

        views = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return MessageViews(views=views, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.views))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
