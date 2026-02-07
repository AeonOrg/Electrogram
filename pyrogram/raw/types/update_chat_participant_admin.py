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


class UpdateChatParticipantAdmin(TLObject):  # type: ignore
    """Admin permissions of a user in a basic group were changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``D7CA61A2``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Chat ID

        user_id (``int`` ``64-bit``):
            ID of the (de)admined user

        is_admin (``bool``):
            Whether the user was rendered admin

        version (``int`` ``32-bit``):
            Used in basic groups to reorder updates and make sure that all of them was received.

    """

    __slots__: List[str] = ["chat_id", "user_id", "is_admin", "version"]

    ID = 0xd7ca61a2
    QUALNAME = "types.UpdateChatParticipantAdmin"

    def __init__(self, *, chat_id: int, user_id: int, is_admin: bool, version: int) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # long
        self.is_admin = is_admin  # Bool
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipantAdmin":
        # No flags

        chat_id = Long.read(b)

        user_id = Long.read(b)

        is_admin = Bool.read(b)

        version = Int.read(b)

        return UpdateChatParticipantAdmin(chat_id=chat_id, user_id=user_id, is_admin=is_admin, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.chat_id))

        b.write(Long(self.user_id))

        b.write(Bool(self.is_admin))

        b.write(Int(self.version))

        return b.getvalue()
