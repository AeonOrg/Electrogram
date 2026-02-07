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


class ChatlistUpdates(TLObject):  # type: ignore
    """Updated information about a chat folder deep link ».

    Constructor of :obj:`~pyrogram.raw.base.chatlists.ChatlistUpdates`.

    Details:
        - Layer: ``224``
        - ID: ``93BD878D``

    Parameters:
        missing_peers (List of :obj:`Peer <pyrogram.raw.base.Peer>`):
            New peers to join

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Related chat information

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Related user information

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.GetChatlistUpdates
    """

    __slots__: List[str] = ["missing_peers", "chats", "users"]

    ID = 0x93bd878d
    QUALNAME = "types.chatlists.ChatlistUpdates"

    def __init__(self, *, missing_peers: List["raw.base.Peer"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.missing_peers = missing_peers  # Vector<Peer>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatlistUpdates":
        # No flags

        missing_peers = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return ChatlistUpdates(missing_peers=missing_peers, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.missing_peers))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
