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


class ReportMissingCode(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``CB9DEFF6``

    Parameters:
        phone_number (``str``):


        phone_code_hash (``str``):


        mnc (``str``):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "mnc"]

    ID = 0xcb9deff6
    QUALNAME = "functions.auth.ReportMissingCode"

    def __init__(self, *, phone_number: str, phone_code_hash: str, mnc: str) -> None:
        self.phone_number = phone_number  # string
        self.phone_code_hash = phone_code_hash  # string
        self.mnc = mnc  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportMissingCode":
        # No flags

        phone_number = String.read(b)

        phone_code_hash = String.read(b)

        mnc = String.read(b)

        return ReportMissingCode(phone_number=phone_number, phone_code_hash=phone_code_hash, mnc=mnc)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.phone_number))

        b.write(String(self.phone_code_hash))

        b.write(String(self.mnc))

        return b.getvalue()
