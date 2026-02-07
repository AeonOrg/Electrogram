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


class GetCountriesList(TLObject):  # type: ignore
    """Get name, ISO code, localized name and phone codes/patterns of all available countries


    Details:
        - Layer: ``224``
        - ID: ``735787A8``

    Parameters:
        lang_code (``str``):
            Language code of the current user

        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the help.countriesList.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`help.CountriesList <pyrogram.raw.base.help.CountriesList>`
    """

    __slots__: List[str] = ["lang_code", "hash"]

    ID = 0x735787a8
    QUALNAME = "functions.help.GetCountriesList"

    def __init__(self, *, lang_code: str, hash: int) -> None:
        self.lang_code = lang_code  # string
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCountriesList":
        # No flags

        lang_code = String.read(b)

        hash = Int.read(b)

        return GetCountriesList(lang_code=lang_code, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.lang_code))

        b.write(Int(self.hash))

        return b.getvalue()
