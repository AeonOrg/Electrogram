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


class WebPagePreview(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.WebPagePreview`.

    Details:
        - Layer: ``224``
        - ID: ``8C9A88AC``

    Parameters:
        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPagePreview
    """

    __slots__: List[str] = ["media", "chats", "users"]

    ID = 0x8c9a88ac
    QUALNAME = "types.messages.WebPagePreview"

    def __init__(self, *, media: "raw.base.MessageMedia", chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.media = media  # MessageMedia
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPagePreview":
        # No flags

        media = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return WebPagePreview(media=media, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.media.write())

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
