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


class CheckUsername(TLObject):  # type: ignore
    """Validates a username and checks availability.


    Details:
        - Layer: ``224``
        - ID: ``2714D86C``

    Parameters:
        username (``str``):
            usernameAccepted characters: A-z (case-insensitive), 0-9 and underscores.Length: 5-32 characters.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["username"]

    ID = 0x2714d86c
    QUALNAME = "functions.account.CheckUsername"

    def __init__(self, *, username: str) -> None:
        self.username = username  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckUsername":
        # No flags

        username = String.read(b)

        return CheckUsername(username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.username))

        return b.getvalue()
