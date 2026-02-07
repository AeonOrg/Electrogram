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


class SearchEmojiStickerSets(TLObject):  # type: ignore
    """Search for custom emoji stickersets »


    Details:
        - Layer: ``224``
        - ID: ``92B4494C``

    Parameters:
        q (``str``):
            Query string

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.foundStickerSets.hash field returned by a previous call to the method, or pass 0 if this is the first call.

        exclude_featured (``bool``, *optional*):
            Exclude featured stickersets from results

    Returns:
        :obj:`messages.FoundStickerSets <pyrogram.raw.base.messages.FoundStickerSets>`
    """

    __slots__: List[str] = ["q", "hash", "exclude_featured"]

    ID = 0x92b4494c
    QUALNAME = "functions.messages.SearchEmojiStickerSets"

    def __init__(self, *, q: str, hash: int, exclude_featured: Optional[bool] = None) -> None:
        self.q = q  # string
        self.hash = hash  # long
        self.exclude_featured = exclude_featured  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchEmojiStickerSets":

        flags = Int.read(b)

        exclude_featured = True if flags & (1 << 0) else False
        q = String.read(b)

        hash = Long.read(b)

        return SearchEmojiStickerSets(q=q, hash=hash, exclude_featured=exclude_featured)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_featured else 0
        b.write(Int(flags))

        b.write(String(self.q))

        b.write(Long(self.hash))

        return b.getvalue()
