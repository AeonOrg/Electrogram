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


class CheckChatInvite(TLObject):  # type: ignore
    """Check the validity of a chat invite link and get basic info about it


    Details:
        - Layer: ``224``
        - ID: ``3EADB1BB``

    Parameters:
        hash (``str``):
            Invite hash from chat invite deep link ».

    Returns:
        :obj:`ChatInvite <pyrogram.raw.base.ChatInvite>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x3eadb1bb
    QUALNAME = "functions.messages.CheckChatInvite"

    def __init__(self, *, hash: str) -> None:
        self.hash = hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckChatInvite":
        # No flags

        hash = String.read(b)

        return CheckChatInvite(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.hash))

        return b.getvalue()
