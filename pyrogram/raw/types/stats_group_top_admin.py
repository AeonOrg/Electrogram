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


class StatsGroupTopAdmin(TLObject):  # type: ignore
    """Information about an active admin in a supergroup

    Constructor of :obj:`~pyrogram.raw.base.StatsGroupTopAdmin`.

    Details:
        - Layer: ``224``
        - ID: ``D7584C87``

    Parameters:
        user_id (``int`` ``64-bit``):
            User ID

        deleted (``int`` ``32-bit``):
            Number of deleted messages for statistics period in consideration

        kicked (``int`` ``32-bit``):
            Number of kicked users for statistics period in consideration

        banned (``int`` ``32-bit``):
            Number of banned users for statistics period in consideration

    """

    __slots__: List[str] = ["user_id", "deleted", "kicked", "banned"]

    ID = 0xd7584c87
    QUALNAME = "types.StatsGroupTopAdmin"

    def __init__(self, *, user_id: int, deleted: int, kicked: int, banned: int) -> None:
        self.user_id = user_id  # long
        self.deleted = deleted  # int
        self.kicked = kicked  # int
        self.banned = banned  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGroupTopAdmin":
        # No flags

        user_id = Long.read(b)

        deleted = Int.read(b)

        kicked = Int.read(b)

        banned = Int.read(b)

        return StatsGroupTopAdmin(user_id=user_id, deleted=deleted, kicked=kicked, banned=banned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(Int(self.deleted))

        b.write(Int(self.kicked))

        b.write(Int(self.banned))

        return b.getvalue()
