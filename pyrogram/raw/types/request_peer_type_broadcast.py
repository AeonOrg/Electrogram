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


class RequestPeerTypeBroadcast(TLObject):  # type: ignore
    """Choose a channel

    Constructor of :obj:`~pyrogram.raw.base.RequestPeerType`.

    Details:
        - Layer: ``224``
        - ID: ``339BEF6C``

    Parameters:
        creator (``bool``, *optional*):
            Whether to allow only choosing channels that were created by the current user.

        user_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            If specified, allows only choosing channels where the current user is an admin with at least the specified admin rights.

        has_username (``bool``, *optional*):
            If specified, allows only choosing channels with or without a username, according to the value of Bool.

        bot_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            If specified, allows only choosing channels where the bot is an admin with at least the specified admin rights.

    """

    __slots__: List[str] = ["creator", "user_admin_rights", "has_username", "bot_admin_rights"]

    ID = 0x339bef6c
    QUALNAME = "types.RequestPeerTypeBroadcast"

    def __init__(self, *, creator: Optional[bool] = None, user_admin_rights: "raw.base.ChatAdminRights" = None, has_username: Optional[bool] = None, bot_admin_rights: "raw.base.ChatAdminRights" = None) -> None:
        self.creator = creator  # flags.0?true
        self.user_admin_rights = user_admin_rights  # flags.1?ChatAdminRights
        self.has_username = has_username  # flags.3?Bool
        self.bot_admin_rights = bot_admin_rights  # flags.2?ChatAdminRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPeerTypeBroadcast":

        flags = Int.read(b)

        creator = True if flags & (1 << 0) else False
        user_admin_rights = TLObject.read(b) if flags & (1 << 1) else None

        has_username = Bool.read(b) if flags & (1 << 3) else None
        bot_admin_rights = TLObject.read(b) if flags & (1 << 2) else None

        return RequestPeerTypeBroadcast(creator=creator, user_admin_rights=user_admin_rights, has_username=has_username, bot_admin_rights=bot_admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 1) if self.user_admin_rights is not None else 0
        flags |= (1 << 3) if self.has_username is not None else 0
        flags |= (1 << 2) if self.bot_admin_rights is not None else 0
        b.write(Int(flags))

        if self.user_admin_rights is not None:
            b.write(self.user_admin_rights.write())

        if self.has_username is not None:
            b.write(Bool(self.has_username))

        if self.bot_admin_rights is not None:
            b.write(self.bot_admin_rights.write())

        return b.getvalue()
