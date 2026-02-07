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


class SendAsPeers(TLObject):  # type: ignore
    """A list of peers that can be used to send messages in a specific group

    Constructor of :obj:`~pyrogram.raw.base.channels.SendAsPeers`.

    Details:
        - Layer: ``224``
        - ID: ``F496B0C6``

    Parameters:
        peers (List of :obj:`SendAsPeer <pyrogram.raw.base.SendAsPeer>`):
            Peers that can be used to send messages to the group

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Mentioned users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.GetSendAs
    """

    __slots__: List[str] = ["peers", "chats", "users"]

    ID = 0xf496b0c6
    QUALNAME = "types.channels.SendAsPeers"

    def __init__(self, *, peers: List["raw.base.SendAsPeer"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.peers = peers  # Vector<SendAsPeer>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendAsPeers":
        # No flags

        peers = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return SendAsPeers(peers=peers, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.peers))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
