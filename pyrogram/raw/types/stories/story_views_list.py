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


class StoryViewsList(TLObject):  # type: ignore
    """Reaction and view counters for a story

    Constructor of :obj:`~pyrogram.raw.base.stories.StoryViewsList`.

    Details:
        - Layer: ``224``
        - ID: ``59D78FC5``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of results that can be fetched

        views_count (``int`` ``32-bit``):
            Total number of story views

        forwards_count (``int`` ``32-bit``):
            Total number of story forwards/reposts

        reactions_count (``int`` ``32-bit``):
            Number of reactions that were added to the story

        views (List of :obj:`StoryView <pyrogram.raw.base.StoryView>`):
            Story view date and reaction information

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Mentioned users

        next_offset (``str``, *optional*):
            Offset for pagination

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.GetStoryViewsList
    """

    __slots__: List[str] = ["count", "views_count", "forwards_count", "reactions_count", "views", "chats", "users", "next_offset"]

    ID = 0x59d78fc5
    QUALNAME = "types.stories.StoryViewsList"

    def __init__(self, *, count: int, views_count: int, forwards_count: int, reactions_count: int, views: List["raw.base.StoryView"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.views_count = views_count  # int
        self.forwards_count = forwards_count  # int
        self.reactions_count = reactions_count  # int
        self.views = views  # Vector<StoryView>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViewsList":

        flags = Int.read(b)

        count = Int.read(b)

        views_count = Int.read(b)

        forwards_count = Int.read(b)

        reactions_count = Int.read(b)

        views = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        return StoryViewsList(count=count, views_count=views_count, forwards_count=forwards_count, reactions_count=reactions_count, views=views, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Int(self.views_count))

        b.write(Int(self.forwards_count))

        b.write(Int(self.reactions_count))

        b.write(Vector(self.views))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        return b.getvalue()
