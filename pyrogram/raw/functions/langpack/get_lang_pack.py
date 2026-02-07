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


class GetLangPack(TLObject):  # type: ignore
    """Get localization pack strings


    Details:
        - Layer: ``224``
        - ID: ``F2F2330A``

    Parameters:
        lang_pack (``str``):
            Language pack name, usually obtained from a language pack link

        lang_code (``str``):
            Language code

    Returns:
        :obj:`LangPackDifference <pyrogram.raw.base.LangPackDifference>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code"]

    ID = 0xf2f2330a
    QUALNAME = "functions.langpack.GetLangPack"

    def __init__(self, *, lang_pack: str, lang_code: str) -> None:
        self.lang_pack = lang_pack  # string
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLangPack":
        # No flags

        lang_pack = String.read(b)

        lang_code = String.read(b)

        return GetLangPack(lang_pack=lang_pack, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.lang_pack))

        b.write(String(self.lang_code))

        return b.getvalue()
