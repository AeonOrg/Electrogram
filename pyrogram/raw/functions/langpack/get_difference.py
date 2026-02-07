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


class GetDifference(TLObject):  # type: ignore
    """Get new strings in language pack


    Details:
        - Layer: ``224``
        - ID: ``CD984AA5``

    Parameters:
        lang_pack (``str``):
            Language pack

        lang_code (``str``):
            Language code

        from_version (``int`` ``32-bit``):
            Previous localization pack version

    Returns:
        :obj:`LangPackDifference <pyrogram.raw.base.LangPackDifference>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code", "from_version"]

    ID = 0xcd984aa5
    QUALNAME = "functions.langpack.GetDifference"

    def __init__(self, *, lang_pack: str, lang_code: str, from_version: int) -> None:
        self.lang_pack = lang_pack  # string
        self.lang_code = lang_code  # string
        self.from_version = from_version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDifference":
        # No flags

        lang_pack = String.read(b)

        lang_code = String.read(b)

        from_version = Int.read(b)

        return GetDifference(lang_pack=lang_pack, lang_code=lang_code, from_version=from_version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.lang_pack))

        b.write(String(self.lang_code))

        b.write(Int(self.from_version))

        return b.getvalue()
