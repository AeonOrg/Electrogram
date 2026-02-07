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


class EmailVerified(TLObject):  # type: ignore
    """The email was verified correctly.

    Constructor of :obj:`~pyrogram.raw.base.account.EmailVerified`.

    Details:
        - Layer: ``224``
        - ID: ``2B96CD1B``

    Parameters:
        email (``str``):
            The verified email address.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.VerifyEmail
    """

    __slots__: List[str] = ["email"]

    ID = 0x2b96cd1b
    QUALNAME = "types.account.EmailVerified"

    def __init__(self, *, email: str) -> None:
        self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmailVerified":
        # No flags

        email = String.read(b)

        return EmailVerified(email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.email))

        return b.getvalue()
