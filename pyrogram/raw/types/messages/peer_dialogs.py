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


class PeerDialogs(TLObject):  # type: ignore
    """Dialog info of multiple peers

    Constructor of :obj:`~pyrogram.raw.base.messages.PeerDialogs`.

    Details:
        - Layer: ``224``
        - ID: ``3371C354``

    Parameters:
        dialogs (List of :obj:`Dialog <pyrogram.raw.base.Dialog>`):
            Dialog info

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            Messages mentioned in dialog info

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users

        state (:obj:`updates.State <pyrogram.raw.base.updates.State>`):
            Current update state of dialog

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetPeerDialogs
            messages.GetPinnedDialogs
    """

    __slots__: List[str] = ["dialogs", "messages", "chats", "users", "state"]

    ID = 0x3371c354
    QUALNAME = "types.messages.PeerDialogs"

    def __init__(self, *, dialogs: List["raw.base.Dialog"], messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"], state: "raw.base.updates.State") -> None:
        self.dialogs = dialogs  # Vector<Dialog>
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.state = state  # updates.State

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerDialogs":
        # No flags

        dialogs = TLObject.read(b)

        messages = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        state = TLObject.read(b)

        return PeerDialogs(dialogs=dialogs, messages=messages, chats=chats, users=users, state=state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.dialogs))

        b.write(Vector(self.messages))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        b.write(self.state.write())

        return b.getvalue()
