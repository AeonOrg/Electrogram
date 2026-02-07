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


class EmailVerifyPurposePassport(TLObject):  # type: ignore
    """Verify an email for use in telegram passport

    Constructor of :obj:`~pyrogram.raw.base.EmailVerifyPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``BBF51685``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xbbf51685
    QUALNAME = "types.EmailVerifyPurposePassport"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmailVerifyPurposePassport":
        # No flags

        return EmailVerifyPurposePassport()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
