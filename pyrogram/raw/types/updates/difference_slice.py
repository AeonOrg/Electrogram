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


class DifferenceSlice(TLObject):  # type: ignore
    """Incomplete list of occurred events.

    Constructor of :obj:`~pyrogram.raw.base.updates.Difference`.

    Details:
        - Layer: ``224``
        - ID: ``A8FB1981``

    Parameters:
        new_messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            List of new messages

        new_encrypted_messages (List of :obj:`EncryptedMessage <pyrogram.raw.base.EncryptedMessage>`):
            New messages from the encrypted event sequence

        other_updates (List of :obj:`Update <pyrogram.raw.base.Update>`):
            List of updates

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            List of chats mentioned in events

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users mentioned in events

        intermediate_state (:obj:`updates.State <pyrogram.raw.base.updates.State>`):
            Intermediary state

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetDifference
    """

    __slots__: List[str] = ["new_messages", "new_encrypted_messages", "other_updates", "chats", "users", "intermediate_state"]

    ID = 0xa8fb1981
    QUALNAME = "types.updates.DifferenceSlice"

    def __init__(self, *, new_messages: List["raw.base.Message"], new_encrypted_messages: List["raw.base.EncryptedMessage"], other_updates: List["raw.base.Update"], chats: List["raw.base.Chat"], users: List["raw.base.User"], intermediate_state: "raw.base.updates.State") -> None:
        self.new_messages = new_messages  # Vector<Message>
        self.new_encrypted_messages = new_encrypted_messages  # Vector<EncryptedMessage>
        self.other_updates = other_updates  # Vector<Update>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.intermediate_state = intermediate_state  # updates.State

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DifferenceSlice":
        # No flags

        new_messages = TLObject.read(b)

        new_encrypted_messages = TLObject.read(b)

        other_updates = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        intermediate_state = TLObject.read(b)

        return DifferenceSlice(new_messages=new_messages, new_encrypted_messages=new_encrypted_messages, other_updates=other_updates, chats=chats, users=users, intermediate_state=intermediate_state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.new_messages))

        b.write(Vector(self.new_encrypted_messages))

        b.write(Vector(self.other_updates))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        b.write(self.intermediate_state.write())

        return b.getvalue()
