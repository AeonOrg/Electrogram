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


class FoundStories(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stories.FoundStories`.

    Details:
        - Layer: ``224``
        - ID: ``E2DE7737``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        stories (List of :obj:`FoundStory <pyrogram.raw.base.FoundStory>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.SearchPosts
    """

    __slots__: List[str] = ["count", "stories", "chats", "users", "next_offset"]

    ID = 0xe2de7737
    QUALNAME = "types.stories.FoundStories"

    def __init__(self, *, count: int, stories: List["raw.base.FoundStory"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.stories = stories  # Vector<FoundStory>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FoundStories":

        flags = Int.read(b)

        count = Int.read(b)

        stories = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = TLObject.read(b)

        users = TLObject.read(b)

        return FoundStories(count=count, stories=stories, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Vector(self.stories))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
