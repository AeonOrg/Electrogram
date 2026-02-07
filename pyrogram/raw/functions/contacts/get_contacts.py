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


class GetContacts(TLObject):  # type: ignore
    """Returns the current user's contact list.


    Details:
        - Layer: ``224``
        - ID: ``5DD69E12``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note that the hash is computed using the usual algorithm, passing to the algorithm first the previously returned contacts.contacts.saved_count field, then max 100000 sorted user IDs from the contact list, including the ID of the currently logged in user if it is saved as a contact. Example: tdlib implementation.

    Returns:
        :obj:`contacts.Contacts <pyrogram.raw.base.contacts.Contacts>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x5dd69e12
    QUALNAME = "functions.contacts.GetContacts"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetContacts":
        # No flags

        hash = Long.read(b)

        return GetContacts(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        return b.getvalue()
