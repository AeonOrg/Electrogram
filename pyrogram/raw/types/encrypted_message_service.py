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


class EncryptedMessageService(TLObject):  # type: ignore
    """Encrypted service message

    Constructor of :obj:`~pyrogram.raw.base.EncryptedMessage`.

    Details:
        - Layer: ``224``
        - ID: ``23734B06``

    Parameters:
        random_id (``int`` ``64-bit``):
            Random message ID, assigned by the author of message

        chat_id (``int`` ``32-bit``):
            ID of encrypted chat

        date (``int`` ``32-bit``):
            Date of sending

        bytes (``bytes``):
            TL-serialization of the DecryptedMessage type, encrypted with the key created at chat initialization

    """

    __slots__: List[str] = ["random_id", "chat_id", "date", "bytes"]

    ID = 0x23734b06
    QUALNAME = "types.EncryptedMessageService"

    def __init__(self, *, random_id: int, chat_id: int, date: int, bytes: bytes) -> None:
        self.random_id = random_id  # long
        self.chat_id = chat_id  # int
        self.date = date  # int
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedMessageService":
        # No flags

        random_id = Long.read(b)

        chat_id = Int.read(b)

        date = Int.read(b)

        bytes = Bytes.read(b)

        return EncryptedMessageService(random_id=random_id, chat_id=chat_id, date=date, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.random_id))

        b.write(Int(self.chat_id))

        b.write(Int(self.date))

        b.write(Bytes(self.bytes))

        return b.getvalue()
