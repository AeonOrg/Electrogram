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


class PrivacyValueDisallowUsers(TLObject):  # type: ignore
    """Disallow only certain users

    Constructor of :obj:`~pyrogram.raw.base.PrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``E4621141``

    Parameters:
        users (List of ``int`` ``64-bit``):
            Disallowed users

    """

    __slots__: List[str] = ["users"]

    ID = 0xe4621141
    QUALNAME = "types.PrivacyValueDisallowUsers"

    def __init__(self, *, users: List[int]) -> None:
        self.users = users  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyValueDisallowUsers":
        # No flags

        users = TLObject.read(b, Long)

        return PrivacyValueDisallowUsers(users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.users, Long))

        return b.getvalue()
