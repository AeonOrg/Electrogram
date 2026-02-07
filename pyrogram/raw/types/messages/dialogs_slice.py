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


class DialogsSlice(TLObject):  # type: ignore
    """Incomplete list of dialogs with messages and auxiliary data.

    Constructor of :obj:`~pyrogram.raw.base.messages.Dialogs`.

    Details:
        - Layer: ``224``
        - ID: ``71E094F3``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of dialogs

        dialogs (List of :obj:`Dialog <pyrogram.raw.base.Dialog>`):
            List of dialogs

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            List of last messages from dialogs

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            List of chats mentioned in dialogs

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users mentioned in messages and chats

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDialogs
    """

    __slots__: List[str] = ["count", "dialogs", "messages", "chats", "users"]

    ID = 0x71e094f3
    QUALNAME = "types.messages.DialogsSlice"

    def __init__(self, *, count: int, dialogs: List["raw.base.Dialog"], messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.count = count  # int
        self.dialogs = dialogs  # Vector<Dialog>
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogsSlice":
        # No flags

        count = Int.read(b)

        dialogs = TLObject.read(b)

        messages = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return DialogsSlice(count=count, dialogs=dialogs, messages=messages, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.count))

        b.write(Vector(self.dialogs))

        b.write(Vector(self.messages))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
