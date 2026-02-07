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


class RequestPasswordRecovery(TLObject):  # type: ignore
    """Request recovery code of a 2FA password, only for accounts with a recovery email configured.


    Details:
        - Layer: ``224``
        - ID: ``D897BC66``

    Parameters:
        No parameters required.

    Returns:
        :obj:`auth.PasswordRecovery <pyrogram.raw.base.auth.PasswordRecovery>`
    """

    __slots__: List[str] = []

    ID = 0xd897bc66
    QUALNAME = "functions.auth.RequestPasswordRecovery"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPasswordRecovery":
        # No flags

        return RequestPasswordRecovery()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
