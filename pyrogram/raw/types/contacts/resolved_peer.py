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


class ResolvedPeer(TLObject):  # type: ignore
    """Resolved peer

    Constructor of :obj:`~pyrogram.raw.base.contacts.ResolvedPeer`.

    Details:
        - Layer: ``224``
        - ID: ``7F077AD9``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ResolveUsername
            contacts.ResolvePhone
    """

    __slots__: List[str] = ["peer", "chats", "users"]

    ID = 0x7f077ad9
    QUALNAME = "types.contacts.ResolvedPeer"

    def __init__(self, *, peer: "raw.base.Peer", chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.peer = peer  # Peer
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolvedPeer":
        # No flags

        peer = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return ResolvedPeer(peer=peer, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
