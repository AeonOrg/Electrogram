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


class CodeTypeFragmentSms(TLObject):  # type: ignore
    """The next time, the authentication code will be delivered via fragment.com

    Constructor of :obj:`~pyrogram.raw.base.auth.CodeType`.

    Details:
        - Layer: ``224``
        - ID: ``6ED998C``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x6ed998c
    QUALNAME = "types.auth.CodeTypeFragmentSms"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CodeTypeFragmentSms":
        # No flags

        return CodeTypeFragmentSms()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
