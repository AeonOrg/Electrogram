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


class ImportLoginToken(TLObject):  # type: ignore
    """Login using a redirected login token, generated in case of DC mismatch during QR code login.


    Details:
        - Layer: ``224``
        - ID: ``95AC5CE4``

    Parameters:
        token (``bytes``):
            Login token

    Returns:
        :obj:`auth.LoginToken <pyrogram.raw.base.auth.LoginToken>`
    """

    __slots__: List[str] = ["token"]

    ID = 0x95ac5ce4
    QUALNAME = "functions.auth.ImportLoginToken"

    def __init__(self, *, token: bytes) -> None:
        self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportLoginToken":
        # No flags

        token = Bytes.read(b)

        return ImportLoginToken(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.token))

        return b.getvalue()
