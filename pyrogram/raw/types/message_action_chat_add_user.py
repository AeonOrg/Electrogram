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


class MessageActionChatAddUser(TLObject):  # type: ignore
    """New member in the group

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``15CEFD00``

    Parameters:
        users (List of ``int`` ``64-bit``):
            Users that were invited to the chat

    """

    __slots__: List[str] = ["users"]

    ID = 0x15cefd00
    QUALNAME = "types.MessageActionChatAddUser"

    def __init__(self, *, users: List[int]) -> None:
        self.users = users  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionChatAddUser":
        # No flags

        users = TLObject.read(b, Long)

        return MessageActionChatAddUser(users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.users, Long))

        return b.getvalue()
