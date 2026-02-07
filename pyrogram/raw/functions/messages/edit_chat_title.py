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


class EditChatTitle(TLObject):  # type: ignore
    """Changes chat name and sends a service message on it.


    Details:
        - Layer: ``224``
        - ID: ``73783FFD``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Chat ID

        title (``str``):
            New chat name, different from the old one

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["chat_id", "title"]

    ID = 0x73783ffd
    QUALNAME = "functions.messages.EditChatTitle"

    def __init__(self, *, chat_id: int, title: str) -> None:
        self.chat_id = chat_id  # long
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatTitle":
        # No flags

        chat_id = Long.read(b)

        title = String.read(b)

        return EditChatTitle(chat_id=chat_id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.chat_id))

        b.write(String(self.title))

        return b.getvalue()
