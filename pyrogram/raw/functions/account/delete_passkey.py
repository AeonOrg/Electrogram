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


class DeletePasskey(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F5B5563F``

    Parameters:
        id (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0xf5b5563f
    QUALNAME = "functions.account.DeletePasskey"

    def __init__(self, *, id: str) -> None:
        self.id = id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePasskey":
        # No flags

        id = String.read(b)

        return DeletePasskey(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.id))

        return b.getvalue()
