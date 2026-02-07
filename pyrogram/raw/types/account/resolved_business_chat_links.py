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


class ResolvedBusinessChatLinks(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.account.ResolvedBusinessChatLinks`.

    Details:
        - Layer: ``224``
        - ID: ``9A23AF21``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):


        message (``str``):


        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):


        users (List of :obj:`User <pyrogram.raw.base.User>`):


        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResolveBusinessChatLink
    """

    __slots__: List[str] = ["peer", "message", "chats", "users", "entities"]

    ID = 0x9a23af21
    QUALNAME = "types.account.ResolvedBusinessChatLinks"

    def __init__(self, *, peer: "raw.base.Peer", message: str, chats: List["raw.base.Chat"], users: List["raw.base.User"], entities: Optional[List["raw.base.MessageEntity"]] = None) -> None:
        self.peer = peer  # Peer
        self.message = message  # string
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.entities = entities  # flags.0?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolvedBusinessChatLinks":

        flags = Int.read(b)

        peer = TLObject.read(b)

        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 0) else []

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return ResolvedBusinessChatLinks(peer=peer, message=message, chats=chats, users=users, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.entities else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(String(self.message))

        if self.entities is not None:
            b.write(Vector(self.entities))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
