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


class ChannelParticipantAdmin(TLObject):  # type: ignore
    """Admin

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``34C3BB53``

    Parameters:
        user_id (``int`` ``64-bit``):
            Admin user ID

        promoted_by (``int`` ``64-bit``):
            User that promoted the user to admin

        date (``int`` ``32-bit``):
            When did the user join

        admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`):
            Admin rights

        can_edit (``bool``, *optional*):
            Can this admin promote other admins with the same permissions?

        is_self (``bool``, *optional*):
            N/A

        inviter_id (``int`` ``64-bit``, *optional*):
            User that invited the admin to the channel/group

        rank (``str``, *optional*):
            The role (rank) of the admin in the group: just an arbitrary string, admin by default

    """

    __slots__: List[str] = ["user_id", "promoted_by", "date", "admin_rights", "can_edit", "is_self", "inviter_id", "rank"]

    ID = 0x34c3bb53
    QUALNAME = "types.ChannelParticipantAdmin"

    def __init__(self, *, user_id: int, promoted_by: int, date: int, admin_rights: "raw.base.ChatAdminRights", can_edit: Optional[bool] = None, is_self: Optional[bool] = None, inviter_id: Optional[int] = None, rank: Optional[str] = None) -> None:
        self.user_id = user_id  # long
        self.promoted_by = promoted_by  # long
        self.date = date  # int
        self.admin_rights = admin_rights  # ChatAdminRights
        self.can_edit = can_edit  # flags.0?true
        self.is_self = is_self  # flags.1?true
        self.inviter_id = inviter_id  # flags.1?long
        self.rank = rank  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantAdmin":

        flags = Int.read(b)

        can_edit = True if flags & (1 << 0) else False
        is_self = True if flags & (1 << 1) else False
        user_id = Long.read(b)

        inviter_id = Long.read(b) if flags & (1 << 1) else None
        promoted_by = Long.read(b)

        date = Int.read(b)

        admin_rights = TLObject.read(b)

        rank = String.read(b) if flags & (1 << 2) else None
        return ChannelParticipantAdmin(user_id=user_id, promoted_by=promoted_by, date=date, admin_rights=admin_rights, can_edit=can_edit, is_self=is_self, inviter_id=inviter_id, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_edit else 0
        flags |= (1 << 1) if self.is_self else 0
        flags |= (1 << 1) if self.inviter_id is not None else 0
        flags |= (1 << 2) if self.rank is not None else 0
        b.write(Int(flags))

        b.write(Long(self.user_id))

        if self.inviter_id is not None:
            b.write(Long(self.inviter_id))

        b.write(Long(self.promoted_by))

        b.write(Int(self.date))

        b.write(self.admin_rights.write())

        if self.rank is not None:
            b.write(String(self.rank))

        return b.getvalue()
