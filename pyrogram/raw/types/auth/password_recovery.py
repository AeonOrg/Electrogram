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


class PasswordRecovery(TLObject):  # type: ignore
    """Recovery info of a 2FA password, only for accounts with a recovery email configured.

    Constructor of :obj:`~pyrogram.raw.base.auth.PasswordRecovery`.

    Details:
        - Layer: ``224``
        - ID: ``137948A5``

    Parameters:
        email_pattern (``str``):
            The email to which the recovery code was sent must match this pattern.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.RequestPasswordRecovery
    """

    __slots__: List[str] = ["email_pattern"]

    ID = 0x137948a5
    QUALNAME = "types.auth.PasswordRecovery"

    def __init__(self, *, email_pattern: str) -> None:
        self.email_pattern = email_pattern  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordRecovery":
        # No flags

        email_pattern = String.read(b)

        return PasswordRecovery(email_pattern=email_pattern)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.email_pattern))

        return b.getvalue()
