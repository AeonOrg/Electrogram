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


class GetStickers(TLObject):  # type: ignore
    """Get stickers by emoji


    Details:
        - Layer: ``224``
        - ID: ``D5A5D3A1``

    Parameters:
        emoticon (``str``):
            The emoji

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.stickers.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`messages.Stickers <pyrogram.raw.base.messages.Stickers>`
    """

    __slots__: List[str] = ["emoticon", "hash"]

    ID = 0xd5a5d3a1
    QUALNAME = "functions.messages.GetStickers"

    def __init__(self, *, emoticon: str, hash: int) -> None:
        self.emoticon = emoticon  # string
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStickers":
        # No flags

        emoticon = String.read(b)

        hash = Long.read(b)

        return GetStickers(emoticon=emoticon, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.emoticon))

        b.write(Long(self.hash))

        return b.getvalue()
