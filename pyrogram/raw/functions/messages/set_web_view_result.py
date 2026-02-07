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


class SetWebViewResult(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E41CD11D``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id"]

    ID = 0xe41cd11d
    QUALNAME = "functions.messages.SetWebViewResult"

    def __init__(self, *, query_id: int) -> None:
        self.query_id = query_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetWebViewResult":
        # No flags

        query_id = Long.read(b)

        return SetWebViewResult(query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.query_id))

        return b.getvalue()
