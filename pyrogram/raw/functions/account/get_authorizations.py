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


class GetAuthorizations(TLObject):  # type: ignore
    """Get logged-in sessions


    Details:
        - Layer: ``224``
        - ID: ``E320C158``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.Authorizations <pyrogram.raw.base.account.Authorizations>`
    """

    __slots__: List[str] = []

    ID = 0xe320c158
    QUALNAME = "functions.account.GetAuthorizations"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAuthorizations":
        # No flags

        return GetAuthorizations()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
