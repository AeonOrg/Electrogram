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


class DeleteChatUser(TLObject):  # type: ignore
    """Deletes a user from a chat and sends a service message on it.


    Details:
        - Layer: ``224``
        - ID: ``A2185CAB``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Chat ID

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            User ID to be deleted

        revoke_history (``bool``, *optional*):
            Remove the entire chat history of the specified user in this chat.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["chat_id", "user_id", "revoke_history"]

    ID = 0xa2185cab
    QUALNAME = "functions.messages.DeleteChatUser"

    def __init__(self, *, chat_id: int, user_id: "raw.base.InputUser", revoke_history: Optional[bool] = None) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # InputUser
        self.revoke_history = revoke_history  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteChatUser":

        flags = Int.read(b)

        revoke_history = True if flags & (1 << 0) else False
        chat_id = Long.read(b)

        user_id = TLObject.read(b)

        return DeleteChatUser(chat_id=chat_id, user_id=user_id, revoke_history=revoke_history)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke_history else 0
        b.write(Int(flags))

        b.write(Long(self.chat_id))

        b.write(self.user_id.write())

        return b.getvalue()
