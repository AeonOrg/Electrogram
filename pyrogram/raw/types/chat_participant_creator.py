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


class ChatParticipantCreator(TLObject):  # type: ignore
    """Represents the creator of the group

    Constructor of :obj:`~pyrogram.raw.base.ChatParticipant`.

    Details:
        - Layer: ``224``
        - ID: ``E46BCEE4``

    Parameters:
        user_id (``int`` ``64-bit``):
            ID of the user that created the group

    """

    __slots__: List[str] = ["user_id"]

    ID = 0xe46bcee4
    QUALNAME = "types.ChatParticipantCreator"

    def __init__(self, *, user_id: int) -> None:
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantCreator":
        # No flags

        user_id = Long.read(b)

        return ChatParticipantCreator(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        return b.getvalue()
