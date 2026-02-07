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


class Contacts(TLObject):  # type: ignore
    """The current user's contact list and info on users.

    Constructor of :obj:`~pyrogram.raw.base.contacts.Contacts`.

    Details:
        - Layer: ``224``
        - ID: ``EAE87E42``

    Parameters:
        contacts (List of :obj:`Contact <pyrogram.raw.base.Contact>`):
            Contact list

        saved_count (``int`` ``32-bit``):
            Number of contacts that were saved successfully

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            User list

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetContacts
    """

    __slots__: List[str] = ["contacts", "saved_count", "users"]

    ID = 0xeae87e42
    QUALNAME = "types.contacts.Contacts"

    def __init__(self, *, contacts: List["raw.base.Contact"], saved_count: int, users: List["raw.base.User"]) -> None:
        self.contacts = contacts  # Vector<Contact>
        self.saved_count = saved_count  # int
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Contacts":
        # No flags

        contacts = TLObject.read(b)

        saved_count = Int.read(b)

        users = TLObject.read(b)

        return Contacts(contacts=contacts, saved_count=saved_count, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.contacts))

        b.write(Int(self.saved_count))

        b.write(Vector(self.users))

        return b.getvalue()
