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


class Dialogs(TLObject):  # type: ignore
    """Full list of chats with messages and auxiliary data.

    Constructor of :obj:`~pyrogram.raw.base.messages.Dialogs`.

    Details:
        - Layer: ``224``
        - ID: ``15BA6C40``

    Parameters:
        dialogs (List of :obj:`Dialog <pyrogram.raw.base.Dialog>`):
            List of chats

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            List of last messages from each chat

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            List of groups mentioned in the chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users mentioned in messages and groups

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDialogs
    """

    __slots__: List[str] = ["dialogs", "messages", "chats", "users"]

    ID = 0x15ba6c40
    QUALNAME = "types.messages.Dialogs"

    def __init__(self, *, dialogs: List["raw.base.Dialog"], messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.dialogs = dialogs  # Vector<Dialog>
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Dialogs":
        # No flags

        dialogs = TLObject.read(b)

        messages = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return Dialogs(dialogs=dialogs, messages=messages, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.dialogs))

        b.write(Vector(self.messages))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
