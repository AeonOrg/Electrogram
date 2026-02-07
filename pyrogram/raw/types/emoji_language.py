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


class EmojiLanguage(TLObject):  # type: ignore
    """Emoji language

    Constructor of :obj:`~pyrogram.raw.base.EmojiLanguage`.

    Details:
        - Layer: ``224``
        - ID: ``B3FB5361``

    Parameters:
        lang_code (``str``):
            Language code

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiKeywordsLanguages
    """

    __slots__: List[str] = ["lang_code"]

    ID = 0xb3fb5361
    QUALNAME = "types.EmojiLanguage"

    def __init__(self, *, lang_code: str) -> None:
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiLanguage":
        # No flags

        lang_code = String.read(b)

        return EmojiLanguage(lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.lang_code))

        return b.getvalue()
