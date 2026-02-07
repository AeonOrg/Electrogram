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


class ExportedChatInvite(TLObject):  # type: ignore
    """Info about a chat invite

    Constructor of :obj:`~pyrogram.raw.base.messages.ExportedChatInvite`.

    Details:
        - Layer: ``224``
        - ID: ``1871BE50``

    Parameters:
        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            Info about the chat invite

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

    __slots__: List[str] = ["invite", "users"]

    ID = 0x1871be50
    QUALNAME = "types.messages.ExportedChatInvite"

    def __init__(self, *, invite: "raw.base.ExportedChatInvite", users: List["raw.base.User"]) -> None:
        self.invite = invite  # ExportedChatInvite
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatInvite":
        # No flags

        invite = TLObject.read(b)

        users = TLObject.read(b)

        return ExportedChatInvite(invite=invite, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.invite.write())

        b.write(Vector(self.users))

        return b.getvalue()
