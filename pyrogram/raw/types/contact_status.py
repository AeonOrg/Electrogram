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


class ContactStatus(TLObject):  # type: ignore
    """Contact status: online / offline.

    Constructor of :obj:`~pyrogram.raw.base.ContactStatus`.

    Details:
        - Layer: ``224``
        - ID: ``16D9703B``

    Parameters:
        user_id (``int`` ``64-bit``):
            User identifier

        status (:obj:`UserStatus <pyrogram.raw.base.UserStatus>`):
            Online status

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetStatuses
    """

    __slots__: List[str] = ["user_id", "status"]

    ID = 0x16d9703b
    QUALNAME = "types.ContactStatus"

    def __init__(self, *, user_id: int, status: "raw.base.UserStatus") -> None:
        self.user_id = user_id  # long
        self.status = status  # UserStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContactStatus":
        # No flags

        user_id = Long.read(b)

        status = TLObject.read(b)

        return ContactStatus(user_id=user_id, status=status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(self.status.write())

        return b.getvalue()
