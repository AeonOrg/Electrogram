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


class RequestPeerTypeChat(TLObject):  # type: ignore
    """Choose a chat or supergroup

    Constructor of :obj:`~pyrogram.raw.base.RequestPeerType`.

    Details:
        - Layer: ``224``
        - ID: ``C9F06E1B``

    Parameters:
        creator (``bool``, *optional*):
            Whether to allow only choosing chats or supergroups that were created by the current user.

        user_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            If specified, allows only choosing chats or supergroups where the current user is an admin with at least the specified admin rights.

        bot_participant (``bool``, *optional*):
            Whether to allow only choosing chats or supergroups where the bot is a participant.

        bot_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            If specified, allows only choosing chats or supergroups where the bot is an admin with at least the specified admin rights.

        has_username (``bool``, *optional*):
            If specified, allows only choosing channels with or without a username, according to the value of Bool.

        forum (``bool``, *optional*):
            If specified, allows only choosing chats or supergroups that are or aren't forums, according to the value of Bool.

    """

    __slots__: List[str] = ["creator", "user_admin_rights", "bot_participant", "bot_admin_rights", "has_username", "forum"]

    ID = 0xc9f06e1b
    QUALNAME = "types.RequestPeerTypeChat"

    def __init__(self, *, creator: Optional[bool] = None, user_admin_rights: "raw.base.ChatAdminRights" = None, bot_participant: Optional[bool] = None, bot_admin_rights: "raw.base.ChatAdminRights" = None, has_username: Optional[bool] = None, forum: Optional[bool] = None) -> None:
        self.creator = creator  # flags.0?true
        self.user_admin_rights = user_admin_rights  # flags.1?ChatAdminRights
        self.bot_participant = bot_participant  # flags.5?true
        self.bot_admin_rights = bot_admin_rights  # flags.2?ChatAdminRights
        self.has_username = has_username  # flags.3?Bool
        self.forum = forum  # flags.4?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPeerTypeChat":

        flags = Int.read(b)

        creator = True if flags & (1 << 0) else False
        user_admin_rights = TLObject.read(b) if flags & (1 << 1) else None

        bot_participant = True if flags & (1 << 5) else False
        bot_admin_rights = TLObject.read(b) if flags & (1 << 2) else None

        has_username = Bool.read(b) if flags & (1 << 3) else None
        forum = Bool.read(b) if flags & (1 << 4) else None
        return RequestPeerTypeChat(creator=creator, user_admin_rights=user_admin_rights, bot_participant=bot_participant, bot_admin_rights=bot_admin_rights, has_username=has_username, forum=forum)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 1) if self.user_admin_rights is not None else 0
        flags |= (1 << 5) if self.bot_participant else 0
        flags |= (1 << 2) if self.bot_admin_rights is not None else 0
        flags |= (1 << 3) if self.has_username is not None else 0
        flags |= (1 << 4) if self.forum is not None else 0
        b.write(Int(flags))

        if self.user_admin_rights is not None:
            b.write(self.user_admin_rights.write())

        if self.bot_admin_rights is not None:
            b.write(self.bot_admin_rights.write())

        if self.has_username is not None:
            b.write(Bool(self.has_username))

        if self.forum is not None:
            b.write(Bool(self.forum))

        return b.getvalue()
