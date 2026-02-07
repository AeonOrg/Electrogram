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


class EmojiKeywordDeleted(TLObject):  # type: ignore
    """Deleted emoji keyword

    Constructor of :obj:`~pyrogram.raw.base.EmojiKeyword`.

    Details:
        - Layer: ``224``
        - ID: ``236DF622``

    Parameters:
        keyword (``str``):
            Keyword

        emoticons (List of ``str``):
            Emojis that were associated to keyword

    """

    __slots__: List[str] = ["keyword", "emoticons"]

    ID = 0x236df622
    QUALNAME = "types.EmojiKeywordDeleted"

    def __init__(self, *, keyword: str, emoticons: List[str]) -> None:
        self.keyword = keyword  # string
        self.emoticons = emoticons  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiKeywordDeleted":
        # No flags

        keyword = String.read(b)

        emoticons = TLObject.read(b, String)

        return EmojiKeywordDeleted(keyword=keyword, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.keyword))

        b.write(Vector(self.emoticons, String))

        return b.getvalue()
