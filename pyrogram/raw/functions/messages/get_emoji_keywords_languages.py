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


class GetEmojiKeywordsLanguages(TLObject):  # type: ignore
    """Obtain a list of related languages that must be used when fetching emoji keyword lists ».


    Details:
        - Layer: ``224``
        - ID: ``4E9963B2``

    Parameters:
        lang_codes (List of ``str``):
            The user's language codes

    Returns:
        List of :obj:`EmojiLanguage <pyrogram.raw.base.EmojiLanguage>`
    """

    __slots__: List[str] = ["lang_codes"]

    ID = 0x4e9963b2
    QUALNAME = "functions.messages.GetEmojiKeywordsLanguages"

    def __init__(self, *, lang_codes: List[str]) -> None:
        self.lang_codes = lang_codes  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiKeywordsLanguages":
        # No flags

        lang_codes = TLObject.read(b, String)

        return GetEmojiKeywordsLanguages(lang_codes=lang_codes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.lang_codes, String))

        return b.getvalue()
