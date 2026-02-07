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


class ChannelParticipantCreator(TLObject):  # type: ignore
    """Channel/supergroup creator

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``2FE601D3``

    Parameters:
        user_id (``int`` ``64-bit``):
            User ID

        admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`):
            Creator admin rights

        rank (``str``, *optional*):
            The role (rank) of the group creator in the group: just an arbitrary string, admin by default

    """

    __slots__: List[str] = ["user_id", "admin_rights", "rank"]

    ID = 0x2fe601d3
    QUALNAME = "types.ChannelParticipantCreator"

    def __init__(self, *, user_id: int, admin_rights: "raw.base.ChatAdminRights", rank: Optional[str] = None) -> None:
        self.user_id = user_id  # long
        self.admin_rights = admin_rights  # ChatAdminRights
        self.rank = rank  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantCreator":

        flags = Int.read(b)

        user_id = Long.read(b)

        admin_rights = TLObject.read(b)

        rank = String.read(b) if flags & (1 << 0) else None
        return ChannelParticipantCreator(user_id=user_id, admin_rights=admin_rights, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rank is not None else 0
        b.write(Int(flags))

        b.write(Long(self.user_id))

        b.write(self.admin_rights.write())

        if self.rank is not None:
            b.write(String(self.rank))

        return b.getvalue()
