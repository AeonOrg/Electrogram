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


class GetContactIDs(TLObject):  # type: ignore
    """Get the telegram IDs of all contacts.
Returns an array of Telegram user IDs for all contacts (0 if a contact does not have an associated Telegram account or have hidden their account using privacy settings).


    Details:
        - Layer: ``224``
        - ID: ``7ADC669D``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["hash"]

    ID = 0x7adc669d
    QUALNAME = "functions.contacts.GetContactIDs"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetContactIDs":
        # No flags

        hash = Long.read(b)

        return GetContactIDs(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        return b.getvalue()
