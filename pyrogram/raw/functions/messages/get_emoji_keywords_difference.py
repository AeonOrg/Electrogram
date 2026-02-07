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


class GetEmojiKeywordsDifference(TLObject):  # type: ignore
    """Get changed emoji keywords ».


    Details:
        - Layer: ``224``
        - ID: ``1508B6AF``

    Parameters:
        lang_code (``str``):
            Language code

        from_version (``int`` ``32-bit``):
            Previous stored emoji keyword list version

    Returns:
        :obj:`EmojiKeywordsDifference <pyrogram.raw.base.EmojiKeywordsDifference>`
    """

    __slots__: List[str] = ["lang_code", "from_version"]

    ID = 0x1508b6af
    QUALNAME = "functions.messages.GetEmojiKeywordsDifference"

    def __init__(self, *, lang_code: str, from_version: int) -> None:
        self.lang_code = lang_code  # string
        self.from_version = from_version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiKeywordsDifference":
        # No flags

        lang_code = String.read(b)

        from_version = Int.read(b)

        return GetEmojiKeywordsDifference(lang_code=lang_code, from_version=from_version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.lang_code))

        b.write(Int(self.from_version))

        return b.getvalue()
