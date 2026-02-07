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


class ExportedChatInvites(TLObject):  # type: ignore
    """Info about chat invites exported by a certain admin.

    Constructor of :obj:`~pyrogram.raw.base.messages.ExportedChatInvites`.

    Details:
        - Layer: ``224``
        - ID: ``BDC62DCC``

    Parameters:
        count (``int`` ``32-bit``):
            Number of invites exported by the admin

        invites (List of :obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            Exported invites

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Info about the admin

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetExportedChatInvites
    """

    __slots__: List[str] = ["count", "invites", "users"]

    ID = 0xbdc62dcc
    QUALNAME = "types.messages.ExportedChatInvites"

    def __init__(self, *, count: int, invites: List["raw.base.ExportedChatInvite"], users: List["raw.base.User"]) -> None:
        self.count = count  # int
        self.invites = invites  # Vector<ExportedChatInvite>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatInvites":
        # No flags

        count = Int.read(b)

        invites = TLObject.read(b)

        users = TLObject.read(b)

        return ExportedChatInvites(count=count, invites=invites, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.count))

        b.write(Vector(self.invites))

        b.write(Vector(self.users))

        return b.getvalue()
