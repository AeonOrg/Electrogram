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


class VerifyPhone(TLObject):  # type: ignore
    """Verify a phone number for telegram passport.


    Details:
        - Layer: ``224``
        - ID: ``4DD3A7F6``

    Parameters:
        phone_number (``str``):
            Phone number

        phone_code_hash (``str``):
            Phone code hash received from the call to account.sendVerifyPhoneCode

        phone_code (``str``):
            Code received after the call to account.sendVerifyPhoneCode

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "phone_code"]

    ID = 0x4dd3a7f6
    QUALNAME = "functions.account.VerifyPhone"

    def __init__(self, *, phone_number: str, phone_code_hash: str, phone_code: str) -> None:
        self.phone_number = phone_number  # string
        self.phone_code_hash = phone_code_hash  # string
        self.phone_code = phone_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VerifyPhone":
        # No flags

        phone_number = String.read(b)

        phone_code_hash = String.read(b)

        phone_code = String.read(b)

        return VerifyPhone(phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.phone_number))

        b.write(String(self.phone_code_hash))

        b.write(String(self.phone_code))

        return b.getvalue()
