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


class SponsoredMessages(TLObject):  # type: ignore
    """A set of sponsored messages associated to a channel

    Constructor of :obj:`~pyrogram.raw.base.messages.SponsoredMessages`.

    Details:
        - Layer: ``224``
        - ID: ``FFDA656D``

    Parameters:
        messages (List of :obj:`SponsoredMessage <pyrogram.raw.base.SponsoredMessage>`):
            Sponsored messages

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats mentioned in the sponsored messages

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users mentioned in the sponsored messages

        posts_between (``int`` ``32-bit``, *optional*):
            If set, specifies the minimum number of messages between shown sponsored messages; otherwise, only one sponsored message must be shown after all ordinary messages.

        start_delay (``int`` ``32-bit``, *optional*):
            N/A

        between_delay (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSponsoredMessages
    """

    __slots__: List[str] = ["messages", "chats", "users", "posts_between", "start_delay", "between_delay"]

    ID = 0xffda656d
    QUALNAME = "types.messages.SponsoredMessages"

    def __init__(self, *, messages: List["raw.base.SponsoredMessage"], chats: List["raw.base.Chat"], users: List["raw.base.User"], posts_between: Optional[int] = None, start_delay: Optional[int] = None, between_delay: Optional[int] = None) -> None:
        self.messages = messages  # Vector<SponsoredMessage>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.posts_between = posts_between  # flags.0?int
        self.start_delay = start_delay  # flags.1?int
        self.between_delay = between_delay  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessages":

        flags = Int.read(b)

        posts_between = Int.read(b) if flags & (1 << 0) else None
        start_delay = Int.read(b) if flags & (1 << 1) else None
        between_delay = Int.read(b) if flags & (1 << 2) else None
        messages = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return SponsoredMessages(messages=messages, chats=chats, users=users, posts_between=posts_between, start_delay=start_delay, between_delay=between_delay)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.posts_between is not None else 0
        flags |= (1 << 1) if self.start_delay is not None else 0
        flags |= (1 << 2) if self.between_delay is not None else 0
        b.write(Int(flags))

        if self.posts_between is not None:
            b.write(Int(self.posts_between))

        if self.start_delay is not None:
            b.write(Int(self.start_delay))

        if self.between_delay is not None:
            b.write(Int(self.between_delay))

        b.write(Vector(self.messages))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
