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


class InvitedUsers(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.messages.InvitedUsers`.

    Details:
        - Layer: ``224``
        - ID: ``7F5DEFA6``

    Parameters:
        updates (:obj:`Updates <pyrogram.raw.base.Updates>`):


        missing_invitees (List of :obj:`MissingInvitee <pyrogram.raw.base.MissingInvitee>`):


    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.AddChatUser
            messages.CreateChat
            channels.InviteToChannel
    """

    __slots__: List[str] = ["updates", "missing_invitees"]

    ID = 0x7f5defa6
    QUALNAME = "types.messages.InvitedUsers"

    def __init__(self, *, updates: "raw.base.Updates", missing_invitees: List["raw.base.MissingInvitee"]) -> None:
        self.updates = updates  # Updates
        self.missing_invitees = missing_invitees  # Vector<MissingInvitee>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvitedUsers":
        # No flags

        updates = TLObject.read(b)

        missing_invitees = TLObject.read(b)

        return InvitedUsers(updates=updates, missing_invitees=missing_invitees)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.updates.write())

        b.write(Vector(self.missing_invitees))

        return b.getvalue()
