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


class ResolvePhone(TLObject):  # type: ignore
    """Resolve a phone number to get user info, if their privacy settings allow it.


    Details:
        - Layer: ``224``
        - ID: ``8AF94344``

    Parameters:
        phone (``str``):
            Phone number in international format, possibly obtained from a phone number deep link.

    Returns:
        :obj:`contacts.ResolvedPeer <pyrogram.raw.base.contacts.ResolvedPeer>`
    """

    __slots__: List[str] = ["phone"]

    ID = 0x8af94344
    QUALNAME = "functions.contacts.ResolvePhone"

    def __init__(self, *, phone: str) -> None:
        self.phone = phone  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolvePhone":
        # No flags

        phone = String.read(b)

        return ResolvePhone(phone=phone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.phone))

        return b.getvalue()
