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


class ForumTopics(TLObject):  # type: ignore
    """Contains information about multiple forum topics

    Constructor of :obj:`~pyrogram.raw.base.messages.ForumTopics`.

    Details:
        - Layer: ``224``
        - ID: ``367617D3``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of topics matching query; may be more than the topics contained in topics, in which case pagination is required.

        topics (List of :obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            Forum topics

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            Related messages (contains the messages mentioned by forumTopic.top_message).

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Related chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Related users

        pts (``int`` ``32-bit``):
            Event count after generation

        order_by_create_date (``bool``, *optional*):
            Whether the returned topics are ordered by creation date; if set, pagination by offset_date should use forumTopic.date; otherwise topics are ordered by the last message date, so paginate by the date of the message referenced by forumTopic.top_message.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetForumTopics
            messages.GetForumTopicsByID
    """

    __slots__: List[str] = ["count", "topics", "messages", "chats", "users", "pts", "order_by_create_date"]

    ID = 0x367617d3
    QUALNAME = "types.messages.ForumTopics"

    def __init__(self, *, count: int, topics: List["raw.base.ForumTopic"], messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"], pts: int, order_by_create_date: Optional[bool] = None) -> None:
        self.count = count  # int
        self.topics = topics  # Vector<ForumTopic>
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.pts = pts  # int
        self.order_by_create_date = order_by_create_date  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForumTopics":

        flags = Int.read(b)

        order_by_create_date = True if flags & (1 << 0) else False
        count = Int.read(b)

        topics = TLObject.read(b)

        messages = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        pts = Int.read(b)

        return ForumTopics(count=count, topics=topics, messages=messages, chats=chats, users=users, pts=pts, order_by_create_date=order_by_create_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.order_by_create_date else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Vector(self.topics))

        b.write(Vector(self.messages))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        b.write(Int(self.pts))

        return b.getvalue()
