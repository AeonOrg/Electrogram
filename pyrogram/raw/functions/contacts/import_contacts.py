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


class ImportContacts(TLObject):  # type: ignore
    """Imports contacts: saves a full list on the server, adds already registered contacts to the contact list, returns added contacts and their info.


    Details:
        - Layer: ``224``
        - ID: ``2C800BE5``

    Parameters:
        contacts (List of :obj:`InputContact <pyrogram.raw.base.InputContact>`):
            List of contacts to import

    Returns:
        :obj:`contacts.ImportedContacts <pyrogram.raw.base.contacts.ImportedContacts>`
    """

    __slots__: List[str] = ["contacts"]

    ID = 0x2c800be5
    QUALNAME = "functions.contacts.ImportContacts"

    def __init__(self, *, contacts: List["raw.base.InputContact"]) -> None:
        self.contacts = contacts  # Vector<InputContact>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportContacts":
        # No flags

        contacts = TLObject.read(b)

        return ImportContacts(contacts=contacts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.contacts))

        return b.getvalue()
