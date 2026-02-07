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


class SavedDialogs(TLObject):  # type: ignore
    """Represents some saved message dialogs ».

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedDialogs`.

    Details:
        - Layer: ``224``
        - ID: ``F83AE221``

    Parameters:
        dialogs (List of :obj:`SavedDialog <pyrogram.raw.base.SavedDialog>`):
            Saved message dialogs ».

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            List of last messages from each saved dialog

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Mentioned users

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedDialogs
            messages.GetPinnedSavedDialogs
            messages.GetSavedDialogsByID
    """

    __slots__: List[str] = ["dialogs", "messages", "chats", "users"]

    ID = 0xf83ae221
    QUALNAME = "types.messages.SavedDialogs"

    def __init__(self, *, dialogs: List["raw.base.SavedDialog"], messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.dialogs = dialogs  # Vector<SavedDialog>
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedDialogs":
        # No flags

        dialogs = TLObject.read(b)

        messages = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return SavedDialogs(dialogs=dialogs, messages=messages, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.dialogs))

        b.write(Vector(self.messages))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
