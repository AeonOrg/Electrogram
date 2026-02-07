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


class InputPhoneContact(TLObject):  # type: ignore
    """Phone contact.

    Constructor of :obj:`~pyrogram.raw.base.InputContact`.

    Details:
        - Layer: ``224``
        - ID: ``6A1DC4BE``

    Parameters:
        client_id (``int`` ``64-bit``):
            An arbitrary 64-bit integer: it should be set, for example, to an incremental number when using contacts.importContacts, in order to retry importing only the contacts that weren't imported successfully, according to the client_ids returned in contacts.importedContacts.retry_contacts.

        phone (``str``):
            Phone number

        first_name (``str``):
            Contact's first name

        last_name (``str``):
            Contact's last name

        note (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["client_id", "phone", "first_name", "last_name", "note"]

    ID = 0x6a1dc4be
    QUALNAME = "types.InputPhoneContact"

    def __init__(self, *, client_id: int, phone: str, first_name: str, last_name: str, note: "raw.base.TextWithEntities" = None) -> None:
        self.client_id = client_id  # long
        self.phone = phone  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.note = note  # flags.0?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhoneContact":

        flags = Int.read(b)

        client_id = Long.read(b)

        phone = String.read(b)

        first_name = String.read(b)

        last_name = String.read(b)

        note = TLObject.read(b) if flags & (1 << 0) else None

        return InputPhoneContact(client_id=client_id, phone=phone, first_name=first_name, last_name=last_name, note=note)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.note is not None else 0
        b.write(Int(flags))

        b.write(Long(self.client_id))

        b.write(String(self.phone))

        b.write(String(self.first_name))

        b.write(String(self.last_name))

        if self.note is not None:
            b.write(self.note.write())

        return b.getvalue()
