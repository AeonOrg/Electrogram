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


class AdminLogResults(TLObject):  # type: ignore
    """Admin log events

    Constructor of :obj:`~pyrogram.raw.base.channels.AdminLogResults`.

    Details:
        - Layer: ``224``
        - ID: ``ED8AF74D``

    Parameters:
        events (List of :obj:`ChannelAdminLogEvent <pyrogram.raw.base.ChannelAdminLogEvent>`):
            Admin log events

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats mentioned in events

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users mentioned in events

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.GetAdminLog
    """

    __slots__: List[str] = ["events", "chats", "users"]

    ID = 0xed8af74d
    QUALNAME = "types.channels.AdminLogResults"

    def __init__(self, *, events: List["raw.base.ChannelAdminLogEvent"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.events = events  # Vector<ChannelAdminLogEvent>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AdminLogResults":
        # No flags

        events = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return AdminLogResults(events=events, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.events))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
