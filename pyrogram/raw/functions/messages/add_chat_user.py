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


class AddChatUser(TLObject):  # type: ignore
    """Adds a user to a chat and sends a service message on it.


    Details:
        - Layer: ``224``
        - ID: ``CBC6D107``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Chat ID

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            User ID to be added

        fwd_limit (``int`` ``32-bit``):
            Number of last messages to be forwarded

    Returns:
        :obj:`messages.InvitedUsers <pyrogram.raw.base.messages.InvitedUsers>`
    """

    __slots__: List[str] = ["chat_id", "user_id", "fwd_limit"]

    ID = 0xcbc6d107
    QUALNAME = "functions.messages.AddChatUser"

    def __init__(self, *, chat_id: int, user_id: "raw.base.InputUser", fwd_limit: int) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # InputUser
        self.fwd_limit = fwd_limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddChatUser":
        # No flags

        chat_id = Long.read(b)

        user_id = TLObject.read(b)

        fwd_limit = Int.read(b)

        return AddChatUser(chat_id=chat_id, user_id=user_id, fwd_limit=fwd_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.chat_id))

        b.write(self.user_id.write())

        b.write(Int(self.fwd_limit))

        return b.getvalue()
