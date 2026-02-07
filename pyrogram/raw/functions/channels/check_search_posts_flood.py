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


class CheckSearchPostsFlood(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``22567115``

    Parameters:
        query (``str``, *optional*):
            N/A

    Returns:
        :obj:`SearchPostsFlood <pyrogram.raw.base.SearchPostsFlood>`
    """

    __slots__: List[str] = ["query"]

    ID = 0x22567115
    QUALNAME = "functions.channels.CheckSearchPostsFlood"

    def __init__(self, *, query: Optional[str] = None) -> None:
        self.query = query  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckSearchPostsFlood":

        flags = Int.read(b)

        query = String.read(b) if flags & (1 << 0) else None
        return CheckSearchPostsFlood(query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.query is not None else 0
        b.write(Int(flags))

        if self.query is not None:
            b.write(String(self.query))

        return b.getvalue()
