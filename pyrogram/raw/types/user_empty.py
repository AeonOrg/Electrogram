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


class UserEmpty(TLObject):  # type: ignore
    """Empty constructor, non-existent user.

    Constructor of :obj:`~pyrogram.raw.base.User`.

    Details:
        - Layer: ``224``
        - ID: ``D3BC4B7A``

    Parameters:
        id (``int`` ``64-bit``):
            User identifier or 0

    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.UpdateProfile
            account.UpdateUsername
            account.ChangePhone
            users.GetUsers
            contacts.ImportContactToken
            contacts.ImportCard
            channels.GetMessageAuthor
            channels.GetFutureCreatorAfterLeave
            bots.GetAdminedBots
    """

    __slots__: List[str] = ["id"]

    ID = 0xd3bc4b7a
    QUALNAME = "types.UserEmpty"

    def __init__(self, *, id: int) -> None:
        self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserEmpty":
        # No flags

        id = Long.read(b)

        return UserEmpty(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        return b.getvalue()
