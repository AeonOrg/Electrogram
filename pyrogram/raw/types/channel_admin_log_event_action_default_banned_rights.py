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


class ChannelAdminLogEventActionDefaultBannedRights(TLObject):  # type: ignore
    """The default banned rights were modified

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``2DF5FC0A``

    Parameters:
        prev_banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            Previous global banned rights

        new_banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            New global banned rights.

    """

    __slots__: List[str] = ["prev_banned_rights", "new_banned_rights"]

    ID = 0x2df5fc0a
    QUALNAME = "types.ChannelAdminLogEventActionDefaultBannedRights"

    def __init__(self, *, prev_banned_rights: "raw.base.ChatBannedRights", new_banned_rights: "raw.base.ChatBannedRights") -> None:
        self.prev_banned_rights = prev_banned_rights  # ChatBannedRights
        self.new_banned_rights = new_banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionDefaultBannedRights":
        # No flags

        prev_banned_rights = TLObject.read(b)

        new_banned_rights = TLObject.read(b)

        return ChannelAdminLogEventActionDefaultBannedRights(prev_banned_rights=prev_banned_rights, new_banned_rights=new_banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.prev_banned_rights.write())

        b.write(self.new_banned_rights.write())

        return b.getvalue()
