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


class InputEncryptedChat(TLObject):  # type: ignore
    """Creates an encrypted chat.

    Constructor of :obj:`~pyrogram.raw.base.InputEncryptedChat`.

    Details:
        - Layer: ``224``
        - ID: ``F141B5E1``

    Parameters:
        chat_id (``int`` ``32-bit``):
            Chat ID

        access_hash (``int`` ``64-bit``):
            Checking sum from constructor encryptedChat, encryptedChatWaiting or encryptedChatRequested

    """

    __slots__: List[str] = ["chat_id", "access_hash"]

    ID = 0xf141b5e1
    QUALNAME = "types.InputEncryptedChat"

    def __init__(self, *, chat_id: int, access_hash: int) -> None:
        self.chat_id = chat_id  # int
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputEncryptedChat":
        # No flags

        chat_id = Int.read(b)

        access_hash = Long.read(b)

        return InputEncryptedChat(chat_id=chat_id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.chat_id))

        b.write(Long(self.access_hash))

        return b.getvalue()
