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


class DeleteChat(TLObject):  # type: ignore
    """Delete a chat


    Details:
        - Layer: ``224``
        - ID: ``5BD0EE50``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Chat ID

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chat_id"]

    ID = 0x5bd0ee50
    QUALNAME = "functions.messages.DeleteChat"

    def __init__(self, *, chat_id: int) -> None:
        self.chat_id = chat_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteChat":
        # No flags

        chat_id = Long.read(b)

        return DeleteChat(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.chat_id))

        return b.getvalue()
