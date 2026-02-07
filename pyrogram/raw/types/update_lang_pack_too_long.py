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


class UpdateLangPackTooLong(TLObject):  # type: ignore
    """A language pack has changed, the client should manually fetch the changed strings using langpack.getDifference

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``46560264``

    Parameters:
        lang_code (``str``):
            Language code

    """

    __slots__: List[str] = ["lang_code"]

    ID = 0x46560264
    QUALNAME = "types.UpdateLangPackTooLong"

    def __init__(self, *, lang_code: str) -> None:
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateLangPackTooLong":
        # No flags

        lang_code = String.read(b)

        return UpdateLangPackTooLong(lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.lang_code))

        return b.getvalue()
