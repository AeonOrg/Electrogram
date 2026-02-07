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


class GetStrings(TLObject):  # type: ignore
    """Get strings from a language pack


    Details:
        - Layer: ``224``
        - ID: ``EFEA3803``

    Parameters:
        lang_pack (``str``):
            Language pack name, usually obtained from a language pack link

        lang_code (``str``):
            Language code

        keys (List of ``str``):
            Strings to get

    Returns:
        List of :obj:`LangPackString <pyrogram.raw.base.LangPackString>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code", "keys"]

    ID = 0xefea3803
    QUALNAME = "functions.langpack.GetStrings"

    def __init__(self, *, lang_pack: str, lang_code: str, keys: List[str]) -> None:
        self.lang_pack = lang_pack  # string
        self.lang_code = lang_code  # string
        self.keys = keys  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStrings":
        # No flags

        lang_pack = String.read(b)

        lang_code = String.read(b)

        keys = TLObject.read(b, String)

        return GetStrings(lang_pack=lang_pack, lang_code=lang_code, keys=keys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.lang_pack))

        b.write(String(self.lang_code))

        b.write(Vector(self.keys, String))

        return b.getvalue()
