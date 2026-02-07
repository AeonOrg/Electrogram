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


class GroupCall(TLObject):  # type: ignore
    """Contains info about a group call, and partial info about its participants.

    Constructor of :obj:`~pyrogram.raw.base.phone.GroupCall`.

    Details:
        - Layer: ``224``
        - ID: ``9E727AAD``

    Parameters:
        call (:obj:`GroupCall <pyrogram.raw.base.GroupCall>`):
            Info about the group call

        participants (List of :obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            A partial list of participants.

        participants_next_offset (``str``):
            Next offset to use when fetching the remaining participants using phone.getGroupParticipants

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats mentioned in the participants vector

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users mentioned in the participants vector

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCall
    """

    __slots__: List[str] = ["call", "participants", "participants_next_offset", "chats", "users"]

    ID = 0x9e727aad
    QUALNAME = "types.phone.GroupCall"

    def __init__(self, *, call: "raw.base.GroupCall", participants: List["raw.base.GroupCallParticipant"], participants_next_offset: str, chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.call = call  # GroupCall
        self.participants = participants  # Vector<GroupCallParticipant>
        self.participants_next_offset = participants_next_offset  # string
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCall":
        # No flags

        call = TLObject.read(b)

        participants = TLObject.read(b)

        participants_next_offset = String.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return GroupCall(call=call, participants=participants, participants_next_offset=participants_next_offset, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Vector(self.participants))

        b.write(String(self.participants_next_offset))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
