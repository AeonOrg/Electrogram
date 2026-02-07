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


class UpdateEncryptedMessagesRead(TLObject):  # type: ignore
    """Communication history in an encrypted chat was marked as read.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``38FE25B7``

    Parameters:
        chat_id (``int`` ``32-bit``):
            Chat ID

        max_date (``int`` ``32-bit``):
            Maximum value of data for read messages

        date (``int`` ``32-bit``):
            Time when messages were read

    """

    __slots__: List[str] = ["chat_id", "max_date", "date"]

    ID = 0x38fe25b7
    QUALNAME = "types.UpdateEncryptedMessagesRead"

    def __init__(self, *, chat_id: int, max_date: int, date: int) -> None:
        self.chat_id = chat_id  # int
        self.max_date = max_date  # int
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEncryptedMessagesRead":
        # No flags

        chat_id = Int.read(b)

        max_date = Int.read(b)

        date = Int.read(b)

        return UpdateEncryptedMessagesRead(chat_id=chat_id, max_date=max_date, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.chat_id))

        b.write(Int(self.max_date))

        b.write(Int(self.date))

        return b.getvalue()
