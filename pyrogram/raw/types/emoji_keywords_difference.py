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


class EmojiKeywordsDifference(TLObject):  # type: ignore
    """Changes to emoji keywords

    Constructor of :obj:`~pyrogram.raw.base.EmojiKeywordsDifference`.

    Details:
        - Layer: ``224``
        - ID: ``5CC761BD``

    Parameters:
        lang_code (``str``):
            Language code for keywords

        from_version (``int`` ``32-bit``):
            Previous emoji keyword list version

        version (``int`` ``32-bit``):
            Current version of emoji keyword list

        keywords (List of :obj:`EmojiKeyword <pyrogram.raw.base.EmojiKeyword>`):
            Emojis associated to keywords

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiKeywords
            messages.GetEmojiKeywordsDifference
    """

    __slots__: List[str] = ["lang_code", "from_version", "version", "keywords"]

    ID = 0x5cc761bd
    QUALNAME = "types.EmojiKeywordsDifference"

    def __init__(self, *, lang_code: str, from_version: int, version: int, keywords: List["raw.base.EmojiKeyword"]) -> None:
        self.lang_code = lang_code  # string
        self.from_version = from_version  # int
        self.version = version  # int
        self.keywords = keywords  # Vector<EmojiKeyword>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiKeywordsDifference":
        # No flags

        lang_code = String.read(b)

        from_version = Int.read(b)

        version = Int.read(b)

        keywords = TLObject.read(b)

        return EmojiKeywordsDifference(lang_code=lang_code, from_version=from_version, version=version, keywords=keywords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.lang_code))

        b.write(Int(self.from_version))

        b.write(Int(self.version))

        b.write(Vector(self.keywords))

        return b.getvalue()
