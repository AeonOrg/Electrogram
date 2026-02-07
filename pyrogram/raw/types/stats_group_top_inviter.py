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


class StatsGroupTopInviter(TLObject):  # type: ignore
    """Information about an active supergroup inviter

    Constructor of :obj:`~pyrogram.raw.base.StatsGroupTopInviter`.

    Details:
        - Layer: ``224``
        - ID: ``535F779D``

    Parameters:
        user_id (``int`` ``64-bit``):
            User ID

        invitations (``int`` ``32-bit``):
            Number of invitations for statistics period in consideration

    """

    __slots__: List[str] = ["user_id", "invitations"]

    ID = 0x535f779d
    QUALNAME = "types.StatsGroupTopInviter"

    def __init__(self, *, user_id: int, invitations: int) -> None:
        self.user_id = user_id  # long
        self.invitations = invitations  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGroupTopInviter":
        # No flags

        user_id = Long.read(b)

        invitations = Int.read(b)

        return StatsGroupTopInviter(user_id=user_id, invitations=invitations)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(Int(self.invitations))

        return b.getvalue()
