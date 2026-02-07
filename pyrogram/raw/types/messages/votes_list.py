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


class VotesList(TLObject):  # type: ignore
    """How users voted in a poll

    Constructor of :obj:`~pyrogram.raw.base.messages.VotesList`.

    Details:
        - Layer: ``224``
        - ID: ``4899484E``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of votes for all options (or only for the chosen option, if provided to messages.getPollVotes)

        votes (List of :obj:`MessagePeerVote <pyrogram.raw.base.MessagePeerVote>`):
            Vote info for each user

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Info about users that voted in the poll

        next_offset (``str``, *optional*):
            Offset to use with the next messages.getPollVotes request, empty string if no more results are available.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetPollVotes
    """

    __slots__: List[str] = ["count", "votes", "chats", "users", "next_offset"]

    ID = 0x4899484e
    QUALNAME = "types.messages.VotesList"

    def __init__(self, *, count: int, votes: List["raw.base.MessagePeerVote"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.votes = votes  # Vector<MessagePeerVote>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VotesList":

        flags = Int.read(b)

        count = Int.read(b)

        votes = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        return VotesList(count=count, votes=votes, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Vector(self.votes))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        return b.getvalue()
