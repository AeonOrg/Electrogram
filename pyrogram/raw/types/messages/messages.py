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


class Messages(TLObject):  # type: ignore
    """Full list of messages with auxiliary data.

    Constructor of :obj:`~pyrogram.raw.base.messages.Messages`.

    Details:
        - Layer: ``224``
        - ID: ``1D73E7EA``

    Parameters:
        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            List of messages

        topics (List of :obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            List of chats mentioned in dialogs

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users mentioned in messages and chats

    Functions:
        This object can be returned by 15 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessages
            messages.GetHistory
            messages.Search
            messages.SearchGlobal
            messages.GetUnreadMentions
            messages.GetRecentLocations
            messages.GetScheduledHistory
            messages.GetScheduledMessages
            messages.GetReplies
            messages.GetUnreadReactions
            messages.SearchSentMedia
            messages.GetSavedHistory
            messages.GetQuickReplyMessages
            channels.GetMessages
            channels.SearchPosts
    """

    __slots__: List[str] = ["messages", "topics", "chats", "users"]

    ID = 0x1d73e7ea
    QUALNAME = "types.messages.Messages"

    def __init__(self, *, messages: List["raw.base.Message"], topics: List["raw.base.ForumTopic"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.messages = messages  # Vector<Message>
        self.topics = topics  # Vector<ForumTopic>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Messages":
        # No flags

        messages = TLObject.read(b)

        topics = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return Messages(messages=messages, topics=topics, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.messages))

        b.write(Vector(self.topics))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
