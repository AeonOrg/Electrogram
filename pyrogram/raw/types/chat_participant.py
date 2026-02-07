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


class ChatParticipant(TLObject):  # type: ignore
    """Group member.

    Constructor of :obj:`~pyrogram.raw.base.ChatParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``C02D4007``

    Parameters:
        user_id (``int`` ``64-bit``):
            Member user ID

        inviter_id (``int`` ``64-bit``):
            ID of the user that added the member to the group

        date (``int`` ``32-bit``):
            Date added to the group

    """

    __slots__: List[str] = ["user_id", "inviter_id", "date"]

    ID = 0xc02d4007
    QUALNAME = "types.ChatParticipant"

    def __init__(self, *, user_id: int, inviter_id: int, date: int) -> None:
        self.user_id = user_id  # long
        self.inviter_id = inviter_id  # long
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipant":
        # No flags

        user_id = Long.read(b)

        inviter_id = Long.read(b)

        date = Int.read(b)

        return ChatParticipant(user_id=user_id, inviter_id=inviter_id, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(Long(self.inviter_id))

        b.write(Int(self.date))

        return b.getvalue()
