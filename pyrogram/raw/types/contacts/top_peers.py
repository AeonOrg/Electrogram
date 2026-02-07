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


class TopPeers(TLObject):  # type: ignore
    """Top peers

    Constructor of :obj:`~pyrogram.raw.base.contacts.TopPeers`.

    Details:
        - Layer: ``224``
        - ID: ``70B772A8``

    Parameters:
        categories (List of :obj:`TopPeerCategoryPeers <pyrogram.raw.base.TopPeerCategoryPeers>`):
            Top peers by top peer category

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetTopPeers
    """

    __slots__: List[str] = ["categories", "chats", "users"]

    ID = 0x70b772a8
    QUALNAME = "types.contacts.TopPeers"

    def __init__(self, *, categories: List["raw.base.TopPeerCategoryPeers"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.categories = categories  # Vector<TopPeerCategoryPeers>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeers":
        # No flags

        categories = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return TopPeers(categories=categories, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.categories))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
