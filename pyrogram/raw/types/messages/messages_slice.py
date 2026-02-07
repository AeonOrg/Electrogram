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


class MessagesSlice(TLObject):  # type: ignore
    """Incomplete list of messages and auxiliary data.

    Constructor of :obj:`~pyrogram.raw.base.messages.Messages`.

    Details:
        - Layer: ``224``
        - ID: ``5F206716``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of messages in the list

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            List of messages

        topics (List of :obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            List of chats mentioned in messages

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users mentioned in messages and chats

        inexact (``bool``, *optional*):
            If set, indicates that the results may be inexact

        next_rate (``int`` ``32-bit``, *optional*):
            Rate to use in the offset_rate parameter in the next call to messages.searchGlobal

        offset_id_offset (``int`` ``32-bit``, *optional*):
            Indicates the absolute position of messages[0] within the total result set with count count. This is useful, for example, if the result was fetched using offset_id, and we need to display a progress/total counter (like photo 134 of 200, for all media in a chat, we could simply use photo ${offset_id_offset} of ${count}.

        search_flood (:obj:`SearchPostsFlood <pyrogram.raw.base.SearchPostsFlood>`, *optional*):
            N/A

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

    __slots__: List[str] = ["count", "messages", "topics", "chats", "users", "inexact", "next_rate", "offset_id_offset", "search_flood"]

    ID = 0x5f206716
    QUALNAME = "types.messages.MessagesSlice"

    def __init__(self, *, count: int, messages: List["raw.base.Message"], topics: List["raw.base.ForumTopic"], chats: List["raw.base.Chat"], users: List["raw.base.User"], inexact: Optional[bool] = None, next_rate: Optional[int] = None, offset_id_offset: Optional[int] = None, search_flood: "raw.base.SearchPostsFlood" = None) -> None:
        self.count = count  # int
        self.messages = messages  # Vector<Message>
        self.topics = topics  # Vector<ForumTopic>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.inexact = inexact  # flags.1?true
        self.next_rate = next_rate  # flags.0?int
        self.offset_id_offset = offset_id_offset  # flags.2?int
        self.search_flood = search_flood  # flags.3?SearchPostsFlood

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagesSlice":

        flags = Int.read(b)

        inexact = True if flags & (1 << 1) else False
        count = Int.read(b)

        next_rate = Int.read(b) if flags & (1 << 0) else None
        offset_id_offset = Int.read(b) if flags & (1 << 2) else None
        search_flood = TLObject.read(b) if flags & (1 << 3) else None

        messages = TLObject.read(b)

        topics = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return MessagesSlice(count=count, messages=messages, topics=topics, chats=chats, users=users, inexact=inexact, next_rate=next_rate, offset_id_offset=offset_id_offset, search_flood=search_flood)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact else 0
        flags |= (1 << 0) if self.next_rate is not None else 0
        flags |= (1 << 2) if self.offset_id_offset is not None else 0
        flags |= (1 << 3) if self.search_flood is not None else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        if self.next_rate is not None:
            b.write(Int(self.next_rate))

        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))

        if self.search_flood is not None:
            b.write(self.search_flood.write())

        b.write(Vector(self.messages))

        b.write(Vector(self.topics))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
