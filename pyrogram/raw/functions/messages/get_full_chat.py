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


class GetFullChat(TLObject):  # type: ignore
    """Get full info about a basic group.


    Details:
        - Layer: ``224``
        - ID: ``AEB00B34``

    Parameters:
        chat_id (``int`` ``64-bit``):
            Basic group ID.

    Returns:
        :obj:`messages.ChatFull <pyrogram.raw.base.messages.ChatFull>`
    """

    __slots__: List[str] = ["chat_id"]

    ID = 0xaeb00b34
    QUALNAME = "functions.messages.GetFullChat"

    def __init__(self, *, chat_id: int) -> None:
        self.chat_id = chat_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFullChat":
        # No flags

        chat_id = Long.read(b)

        return GetFullChat(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.chat_id))

        return b.getvalue()
