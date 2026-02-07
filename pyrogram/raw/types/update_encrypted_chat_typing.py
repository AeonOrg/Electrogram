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


class UpdateEncryptedChatTyping(TLObject):  # type: ignore
    """Interlocutor is typing a message in an encrypted chat. Update period is 6 second. If upon this time there is no repeated update, it shall be considered that the interlocutor stopped typing.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``1710F156``

    Parameters:
        chat_id (``int`` ``32-bit``):
            Chat ID

    """

    __slots__: List[str] = ["chat_id"]

    ID = 0x1710f156
    QUALNAME = "types.UpdateEncryptedChatTyping"

    def __init__(self, *, chat_id: int) -> None:
        self.chat_id = chat_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEncryptedChatTyping":
        # No flags

        chat_id = Int.read(b)

        return UpdateEncryptedChatTyping(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.chat_id))

        return b.getvalue()
