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


class CodeTypeMissedCall(TLObject):  # type: ignore
    """The next time, the authentication code will be delivered via an immediately canceled incoming call, handled manually by the user.

    Constructor of :obj:`~pyrogram.raw.base.auth.CodeType`.

    Details:
        - Layer: ``224``
        - ID: ``D61AD6EE``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xd61ad6ee
    QUALNAME = "types.auth.CodeTypeMissedCall"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CodeTypeMissedCall":
        # No flags

        return CodeTypeMissedCall()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
