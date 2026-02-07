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


class ChannelAdminLogEventActionExportedInviteEdit(TLObject):  # type: ignore
    """A chat invite was edited

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``E90EBB59``

    Parameters:
        prev_invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            Previous chat invite information

        new_invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            New chat invite information

    """

    __slots__: List[str] = ["prev_invite", "new_invite"]

    ID = 0xe90ebb59
    QUALNAME = "types.ChannelAdminLogEventActionExportedInviteEdit"

    def __init__(self, *, prev_invite: "raw.base.ExportedChatInvite", new_invite: "raw.base.ExportedChatInvite") -> None:
        self.prev_invite = prev_invite  # ExportedChatInvite
        self.new_invite = new_invite  # ExportedChatInvite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionExportedInviteEdit":
        # No flags

        prev_invite = TLObject.read(b)

        new_invite = TLObject.read(b)

        return ChannelAdminLogEventActionExportedInviteEdit(prev_invite=prev_invite, new_invite=new_invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.prev_invite.write())

        b.write(self.new_invite.write())

        return b.getvalue()
