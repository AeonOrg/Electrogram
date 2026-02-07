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


class EditChatAdmin(TLObject):  # type: ignore
    """Make a user admin in a basic group.


    Details:
        - Layer: ``224``
        - ID: ``A85BD1C2``

    Parameters:
        chat_id (``int`` ``64-bit``):
            The ID of the group

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            The user to make admin

        is_admin (``bool``):
            Whether to make them admin

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chat_id", "user_id", "is_admin"]

    ID = 0xa85bd1c2
    QUALNAME = "functions.messages.EditChatAdmin"

    def __init__(self, *, chat_id: int, user_id: "raw.base.InputUser", is_admin: bool) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # InputUser
        self.is_admin = is_admin  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatAdmin":
        # No flags

        chat_id = Long.read(b)

        user_id = TLObject.read(b)

        is_admin = Bool.read(b)

        return EditChatAdmin(chat_id=chat_id, user_id=user_id, is_admin=is_admin)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.chat_id))

        b.write(self.user_id.write())

        b.write(Bool(self.is_admin))

        return b.getvalue()
