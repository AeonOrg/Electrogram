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


class SignUp(TLObject):  # type: ignore
    """Registers a validated phone number in the system.


    Details:
        - Layer: ``224``
        - ID: ``AAC7B717``

    Parameters:
        phone_number (``str``):
            Phone number in the international format

        phone_code_hash (``str``):
            SMS-message ID

        first_name (``str``):
            New user first name

        last_name (``str``):
            New user last name

        no_joined_notifications (``bool``, *optional*):


    Returns:
        :obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "first_name", "last_name", "no_joined_notifications"]

    ID = 0xaac7b717
    QUALNAME = "functions.auth.SignUp"

    def __init__(self, *, phone_number: str, phone_code_hash: str, first_name: str, last_name: str, no_joined_notifications: Optional[bool] = None) -> None:
        self.phone_number = phone_number  # string
        self.phone_code_hash = phone_code_hash  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.no_joined_notifications = no_joined_notifications  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SignUp":

        flags = Int.read(b)

        no_joined_notifications = True if flags & (1 << 0) else False
        phone_number = String.read(b)

        phone_code_hash = String.read(b)

        first_name = String.read(b)

        last_name = String.read(b)

        return SignUp(phone_number=phone_number, phone_code_hash=phone_code_hash, first_name=first_name, last_name=last_name, no_joined_notifications=no_joined_notifications)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.no_joined_notifications else 0
        b.write(Int(flags))

        b.write(String(self.phone_number))

        b.write(String(self.phone_code_hash))

        b.write(String(self.first_name))

        b.write(String(self.last_name))

        return b.getvalue()
