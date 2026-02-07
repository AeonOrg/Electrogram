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


class ImportedContacts(TLObject):  # type: ignore
    """Info on successfully imported contacts.

    Constructor of :obj:`~pyrogram.raw.base.contacts.ImportedContacts`.

    Details:
        - Layer: ``224``
        - ID: ``77D01C3B``

    Parameters:
        imported (List of :obj:`ImportedContact <pyrogram.raw.base.ImportedContact>`):
            List of successfully imported contacts

        popular_invites (List of :obj:`PopularContact <pyrogram.raw.base.PopularContact>`):
            Popular contacts

        retry_contacts (List of ``int`` ``64-bit``):
            List of contact ids that could not be imported due to system limitation and will need to be imported at a later date.

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            List of users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ImportContacts
    """

    __slots__: List[str] = ["imported", "popular_invites", "retry_contacts", "users"]

    ID = 0x77d01c3b
    QUALNAME = "types.contacts.ImportedContacts"

    def __init__(self, *, imported: List["raw.base.ImportedContact"], popular_invites: List["raw.base.PopularContact"], retry_contacts: List[int], users: List["raw.base.User"]) -> None:
        self.imported = imported  # Vector<ImportedContact>
        self.popular_invites = popular_invites  # Vector<PopularContact>
        self.retry_contacts = retry_contacts  # Vector<long>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportedContacts":
        # No flags

        imported = TLObject.read(b)

        popular_invites = TLObject.read(b)

        retry_contacts = TLObject.read(b, Long)

        users = TLObject.read(b)

        return ImportedContacts(imported=imported, popular_invites=popular_invites, retry_contacts=retry_contacts, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.imported))

        b.write(Vector(self.popular_invites))

        b.write(Vector(self.retry_contacts, Long))

        b.write(Vector(self.users))

        return b.getvalue()
