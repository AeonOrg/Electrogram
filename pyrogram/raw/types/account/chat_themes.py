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


class ChatThemes(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.ChatThemes`.

    Details:
        - Layer: ``224``
        - ID: ``BE098173``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        themes (List of :obj:`ChatTheme <pyrogram.raw.base.ChatTheme>`):
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

            account.GetUniqueGiftChatThemes
    """

    __slots__: List[str] = ["hash", "themes", "chats", "users", "next_offset"]

    ID = 0xbe098173
    QUALNAME = "types.account.ChatThemes"

    def __init__(self, *, hash: int, themes: List["raw.base.ChatTheme"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.hash = hash  # long
        self.themes = themes  # Vector<ChatTheme>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatThemes":

        flags = Int.read(b)

        hash = Long.read(b)

        themes = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        next_offset = String.read(b) if flags & (1 << 0) else None
        return ChatThemes(hash=hash, themes=themes, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        b.write(Long(self.hash))

        b.write(Vector(self.themes))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        if self.next_offset is not None:
            b.write(String(self.next_offset))

        return b.getvalue()
