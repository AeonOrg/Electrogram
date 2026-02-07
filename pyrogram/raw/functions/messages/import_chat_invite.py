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


class ImportChatInvite(TLObject):  # type: ignore
    """Import a chat invite and join a private chat/supergroup/channel


    Details:
        - Layer: ``224``
        - ID: ``6C50051C``

    Parameters:
        hash (``str``):
            hash from a chat invite deep link

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x6c50051c
    QUALNAME = "functions.messages.ImportChatInvite"

    def __init__(self, *, hash: str) -> None:
        self.hash = hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportChatInvite":
        # No flags

        hash = String.read(b)

        return ImportChatInvite(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.hash))

        return b.getvalue()
