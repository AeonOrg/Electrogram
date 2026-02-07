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


class UpdateUserStatus(TLObject):  # type: ignore
    """Contact status update.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``E5BDF8DE``

    Parameters:
        user_id (``int`` ``64-bit``):
            User identifier

        status (:obj:`UserStatus <pyrogram.raw.base.UserStatus>`):
            New status

    """

    __slots__: List[str] = ["user_id", "status"]

    ID = 0xe5bdf8de
    QUALNAME = "types.UpdateUserStatus"

    def __init__(self, *, user_id: int, status: "raw.base.UserStatus") -> None:
        self.user_id = user_id  # long
        self.status = status  # UserStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserStatus":
        # No flags

        user_id = Long.read(b)

        status = TLObject.read(b)

        return UpdateUserStatus(user_id=user_id, status=status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(self.status.write())

        return b.getvalue()
