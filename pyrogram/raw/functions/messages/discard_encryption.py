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


class DiscardEncryption(TLObject):  # type: ignore
    """Cancels a request for creation and/or delete info on secret chat.


    Details:
        - Layer: ``224``
        - ID: ``F393AEA0``

    Parameters:
        chat_id (``int`` ``32-bit``):
            Secret chat ID

        delete_history (``bool``, *optional*):
            Whether to delete the entire chat history for the other user as well

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chat_id", "delete_history"]

    ID = 0xf393aea0
    QUALNAME = "functions.messages.DiscardEncryption"

    def __init__(self, *, chat_id: int, delete_history: Optional[bool] = None) -> None:
        self.chat_id = chat_id  # int
        self.delete_history = delete_history  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DiscardEncryption":

        flags = Int.read(b)

        delete_history = True if flags & (1 << 0) else False
        chat_id = Int.read(b)

        return DiscardEncryption(chat_id=chat_id, delete_history=delete_history)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.delete_history else 0
        b.write(Int(flags))

        b.write(Int(self.chat_id))

        return b.getvalue()
