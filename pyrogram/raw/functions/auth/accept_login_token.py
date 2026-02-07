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


class AcceptLoginToken(TLObject):  # type: ignore
    """Accept QR code login token, logging in the app that generated it.


    Details:
        - Layer: ``224``
        - ID: ``E894AD4D``

    Parameters:
        token (``bytes``):
            Login token embedded in QR code, for more info, see login via QR code.

    Returns:
        :obj:`Authorization <pyrogram.raw.base.Authorization>`
    """

    __slots__: List[str] = ["token"]

    ID = 0xe894ad4d
    QUALNAME = "functions.auth.AcceptLoginToken"

    def __init__(self, *, token: bytes) -> None:
        self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptLoginToken":
        # No flags

        token = Bytes.read(b)

        return AcceptLoginToken(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.token))

        return b.getvalue()
