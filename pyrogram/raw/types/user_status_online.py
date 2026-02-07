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


class UserStatusOnline(TLObject):  # type: ignore
    """Online status of the user.

    Constructor of :obj:`~pyrogram.raw.base.UserStatus`.

    Details:
        - Layer: ``224``
        - ID: ``EDB93949``

    Parameters:
        expires (``int`` ``32-bit``):
            Time to expiration of the current online status

    """

    __slots__: List[str] = ["expires"]

    ID = 0xedb93949
    QUALNAME = "types.UserStatusOnline"

    def __init__(self, *, expires: int) -> None:
        self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserStatusOnline":
        # No flags

        expires = Int.read(b)

        return UserStatusOnline(expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.expires))

        return b.getvalue()
