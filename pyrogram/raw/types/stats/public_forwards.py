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


class PublicForwards(TLObject):  # type: ignore
    """Contains info about the forwards of a story as a message to public chats and reposts by public channels.

    Constructor of :obj:`~pyrogram.raw.base.stats.PublicForwards`.

    Details:
        - Layer: ``224``
        - ID: ``93037E20``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of results

        forwards (List of :obj:`PublicForward <pyrogram.raw.base.PublicForward>`):
            Info about the forwards of a story.

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Mentioned users

        next_offset (``str``, *optional*):
            Offset used for pagination.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetMessagePublicForwards
            stats.GetStoryPublicForwards
    """

    __slots__: List[str] = ["count", "forwards", "chats", "users", "next_offset"]

    ID = 0x93037e20
    QUALNAME = "types.stats.PublicForwards"

    def __init__(self, *, count: int, forwards: List["raw.base.PublicForward"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.forwards = forwards  # Vector<PublicForward>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PublicForwards":

        flags = Int.read(b)

        count = Int.read(b)

        forwards = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = TLObject.read(b)

        users = TLObject.read(b)

        return PublicForwards(count=count, forwards=forwards, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Int(self.count))

        b.write(Vector(self.forwards))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
