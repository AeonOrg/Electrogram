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


class ImportContactToken(TLObject):  # type: ignore
    """Obtain user info from a temporary profile link.


    Details:
        - Layer: ``224``
        - ID: ``13005788``

    Parameters:
        token (``str``):
            The token extracted from the temporary profile link.

    Returns:
        :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["token"]

    ID = 0x13005788
    QUALNAME = "functions.contacts.ImportContactToken"

    def __init__(self, *, token: str) -> None:
        self.token = token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportContactToken":
        # No flags

        token = String.read(b)

        return ImportContactToken(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.token))

        return b.getvalue()
