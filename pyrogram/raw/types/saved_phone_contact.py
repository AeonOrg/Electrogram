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


class SavedPhoneContact(TLObject):  # type: ignore
    """Saved contact

    Constructor of :obj:`~pyrogram.raw.base.SavedContact`.

    Details:
        - Layer: ``224``
        - ID: ``1142BD56``

    Parameters:
        phone (``str``):
            Phone number

        first_name (``str``):
            First name

        last_name (``str``):
            Last name

        date (``int`` ``32-bit``):
            Date added

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetSaved
    """

    __slots__: List[str] = ["phone", "first_name", "last_name", "date"]

    ID = 0x1142bd56
    QUALNAME = "types.SavedPhoneContact"

    def __init__(self, *, phone: str, first_name: str, last_name: str, date: int) -> None:
        self.phone = phone  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedPhoneContact":
        # No flags

        phone = String.read(b)

        first_name = String.read(b)

        last_name = String.read(b)

        date = Int.read(b)

        return SavedPhoneContact(phone=phone, first_name=first_name, last_name=last_name, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.phone))

        b.write(String(self.first_name))

        b.write(String(self.last_name))

        b.write(Int(self.date))

        return b.getvalue()
