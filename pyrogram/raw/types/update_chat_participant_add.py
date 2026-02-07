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


class UpdateChatParticipantAdd(TLObject):  # type: ignore
    """New group member.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``3DDA5451``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Group ID

        user_id (``int`` ``64-bit``):
            ID of the new member

        inviter_id (``int`` ``64-bit``):
            ID of the user, who added member to the group

        date (``int`` ``32-bit``):
            When was the participant added

        version (``int`` ``32-bit``):
            Chat version number

    """

    __slots__: List[str] = ["chat_id", "user_id", "inviter_id", "date", "version"]

    ID = 0x3dda5451
    QUALNAME = "types.UpdateChatParticipantAdd"

    def __init__(self, *, chat_id: int, user_id: int, inviter_id: int, date: int, version: int) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # long
        self.inviter_id = inviter_id  # long
        self.date = date  # int
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipantAdd":
        # No flags

        chat_id = Long.read(b)

        user_id = Long.read(b)

        inviter_id = Long.read(b)

        date = Int.read(b)

        version = Int.read(b)

        return UpdateChatParticipantAdd(chat_id=chat_id, user_id=user_id, inviter_id=inviter_id, date=date, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.chat_id))

        b.write(Long(self.user_id))

        b.write(Long(self.inviter_id))

        b.write(Int(self.date))

        b.write(Int(self.version))

        return b.getvalue()
