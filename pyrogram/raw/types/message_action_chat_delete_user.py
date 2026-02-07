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


class MessageActionChatDeleteUser(TLObject):  # type: ignore
    """User left the group.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``A43F30CC``

    Parameters:
        user_id (``int`` ``64-bit``):
            Leaving user ID

    """

    __slots__: List[str] = ["user_id"]

    ID = 0xa43f30cc
    QUALNAME = "types.MessageActionChatDeleteUser"

    def __init__(self, *, user_id: int) -> None:
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatDeleteUser":
        # No flags

        user_id = Long.read(b)

        return MessageActionChatDeleteUser(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        return b.getvalue()
