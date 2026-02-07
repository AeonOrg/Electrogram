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


class MessageMediaContact(TLObject):  # type: ignore
    """Attached contact.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``70322949``

    Parameters:
        phone_number (``str``):
            Phone number

        first_name (``str``):
            Contact's first name

        last_name (``str``):
            Contact's last name

        vcard (``str``):
            VCARD of contact

        user_id (``int`` ``64-bit``):
            User identifier or 0, if the user with the given phone number is not registered

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["phone_number", "first_name", "last_name", "vcard", "user_id"]

    ID = 0x70322949
    QUALNAME = "types.MessageMediaContact"

    def __init__(self, *, phone_number: str, first_name: str, last_name: str, vcard: str, user_id: int) -> None:
        self.phone_number = phone_number  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.vcard = vcard  # string
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaContact":
        # No flags

        phone_number = String.read(b)

        first_name = String.read(b)

        last_name = String.read(b)

        vcard = String.read(b)

        user_id = Long.read(b)

        return MessageMediaContact(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.phone_number))

        b.write(String(self.first_name))

        b.write(String(self.last_name))

        b.write(String(self.vcard))

        b.write(Long(self.user_id))

        return b.getvalue()
