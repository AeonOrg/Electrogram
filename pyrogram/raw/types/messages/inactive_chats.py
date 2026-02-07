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


class InactiveChats(TLObject):  # type: ignore
    """Inactive chat list

    Constructor of :obj:`~pyrogram.raw.base.messages.InactiveChats`.

    Details:
        - Layer: ``224``
        - ID: ``A927FEC5``

    Parameters:
        dates (List of ``int`` ``32-bit``):
            When was the chat last active

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chat list

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users mentioned in the chat list

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.GetInactiveChannels
    """

    __slots__: List[str] = ["dates", "chats", "users"]

    ID = 0xa927fec5
    QUALNAME = "types.messages.InactiveChats"

    def __init__(self, *, dates: List[int], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.dates = dates  # Vector<int>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InactiveChats":
        # No flags

        dates = TLObject.read(b, Int)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return InactiveChats(dates=dates, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.dates, Int))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
