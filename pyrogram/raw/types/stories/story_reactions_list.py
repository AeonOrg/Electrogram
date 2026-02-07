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


class StoryReactionsList(TLObject):  # type: ignore
    """List of peers that reacted to or intercated with a specific story

    Constructor of :obj:`~pyrogram.raw.base.stories.StoryReactionsList`.

    Details:
        - Layer: ``224``
        - ID: ``AA5F789C``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of reactions matching query

        reactions (List of :obj:`StoryReaction <pyrogram.raw.base.StoryReaction>`):
            List of peers that reacted to or interacted with a specific story

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Mentioned users

        next_offset (``str``, *optional*):
            If set, indicates the next offset to use to load more results by invoking stories.getStoryReactionsList.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetStoryReactionsList
    """

    __slots__: List[str] = ["count", "reactions", "chats", "users", "next_offset"]

    ID = 0xaa5f789c
    QUALNAME = "types.stories.StoryReactionsList"

    def __init__(self, *, count: int, reactions: List["raw.base.StoryReaction"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.reactions = reactions  # Vector<StoryReaction>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryReactionsList":

        flags = Int.read(b)

        count = Int.read(b)

        reactions = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        return StoryReactionsList(count=count, reactions=reactions, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Vector(self.reactions))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        return b.getvalue()
