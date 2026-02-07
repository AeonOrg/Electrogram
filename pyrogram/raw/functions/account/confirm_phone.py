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


class ConfirmPhone(TLObject):  # type: ignore
    """Confirm a phone number to cancel account deletion, for more info click here »


    Details:
        - Layer: ``224``
        - ID: ``5F2178C3``

    Parameters:
        phone_code_hash (``str``):
            Phone code hash, for more info click here »

        phone_code (``str``):
            SMS code, for more info click here »

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_code_hash", "phone_code"]

    ID = 0x5f2178c3
    QUALNAME = "functions.account.ConfirmPhone"

    def __init__(self, *, phone_code_hash: str, phone_code: str) -> None:
        self.phone_code_hash = phone_code_hash  # string
        self.phone_code = phone_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfirmPhone":
        # No flags

        phone_code_hash = String.read(b)

        phone_code = String.read(b)

        return ConfirmPhone(phone_code_hash=phone_code_hash, phone_code=phone_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.phone_code_hash))

        b.write(String(self.phone_code))

        return b.getvalue()
