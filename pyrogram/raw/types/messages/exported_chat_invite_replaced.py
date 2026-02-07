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


class ExportedChatInviteReplaced(TLObject):  # type: ignore
    """The specified chat invite was replaced with another one

    Constructor of :obj:`~pyrogram.raw.base.messages.ExportedChatInvite`.

    Details:
        - Layer: ``224``
        - ID: ``222600EF``

    Parameters:
        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            The replaced chat invite

        new_invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            The invite that replaces the previous invite

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Mentioned users

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetExportedChatInvite
            messages.EditExportedChatInvite
    """

    __slots__: List[str] = ["invite", "new_invite", "users"]

    ID = 0x222600ef
    QUALNAME = "types.messages.ExportedChatInviteReplaced"

    def __init__(self, *, invite: "raw.base.ExportedChatInvite", new_invite: "raw.base.ExportedChatInvite", users: List["raw.base.User"]) -> None:
        self.invite = invite  # ExportedChatInvite
        self.new_invite = new_invite  # ExportedChatInvite
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatInviteReplaced":
        # No flags

        invite = TLObject.read(b)

        new_invite = TLObject.read(b)

        users = TLObject.read(b)

        return ExportedChatInviteReplaced(invite=invite, new_invite=new_invite, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.invite.write())

        b.write(self.new_invite.write())

        b.write(Vector(self.users))

        return b.getvalue()
