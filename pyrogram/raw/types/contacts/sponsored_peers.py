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


class SponsoredPeers(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.SponsoredPeers`.

    Details:
        - Layer: ``224``
        - ID: ``EB032884``

    Parameters:
        peers (List of :obj:`SponsoredPeer <pyrogram.raw.base.SponsoredPeer>`):
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

            contacts.GetSponsoredPeers
    """

    __slots__: List[str] = ["peers", "chats", "users"]

    ID = 0xeb032884
    QUALNAME = "types.contacts.SponsoredPeers"

    def __init__(self, *, peers: List["raw.base.SponsoredPeer"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.peers = peers  # Vector<SponsoredPeer>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredPeers":
        # No flags

        peers = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return SponsoredPeers(peers=peers, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.peers))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
