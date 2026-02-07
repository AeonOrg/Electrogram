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


class UpdateUser(TLObject):  # type: ignore
    """User information was updated, it must be refetched using users.getFullUser.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``20529438``

    Parameters:
        user_id (``int`` ``64-bit``):
            User ID

    """

    __slots__: List[str] = ["user_id"]

    ID = 0x20529438
    QUALNAME = "types.UpdateUser"

    def __init__(self, *, user_id: int) -> None:
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUser":
        # No flags

        user_id = Long.read(b)

        return UpdateUser(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        return b.getvalue()
