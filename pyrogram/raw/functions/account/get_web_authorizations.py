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


class GetWebAuthorizations(TLObject):  # type: ignore
    """Get web login widget authorizations


    Details:
        - Layer: ``224``
        - ID: ``182E6D6F``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.WebAuthorizations <pyrogram.raw.base.account.WebAuthorizations>`
    """

    __slots__: List[str] = []

    ID = 0x182e6d6f
    QUALNAME = "functions.account.GetWebAuthorizations"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebAuthorizations":
        # No flags

        return GetWebAuthorizations()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
