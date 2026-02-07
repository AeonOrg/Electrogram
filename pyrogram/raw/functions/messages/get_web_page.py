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


class GetWebPage(TLObject):  # type: ignore
    """Get instant view page


    Details:
        - Layer: ``224``
        - ID: ``8D9692A3``

    Parameters:
        url (``str``):
            URL of IV page to fetch

        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

    Returns:
        :obj:`messages.WebPage <pyrogram.raw.base.messages.WebPage>`
    """

    __slots__: List[str] = ["url", "hash"]

    ID = 0x8d9692a3
    QUALNAME = "functions.messages.GetWebPage"

    def __init__(self, *, url: str, hash: int) -> None:
        self.url = url  # string
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebPage":
        # No flags

        url = String.read(b)

        hash = Int.read(b)

        return GetWebPage(url=url, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.url))

        b.write(Int(self.hash))

        return b.getvalue()
