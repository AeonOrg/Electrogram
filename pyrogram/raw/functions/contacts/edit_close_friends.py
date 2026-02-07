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


class EditCloseFriends(TLObject):  # type: ignore
    """Edit the close friends list, see here » for more info.


    Details:
        - Layer: ``224``
        - ID: ``BA6705F0``

    Parameters:
        id (List of ``int`` ``64-bit``):
            Full list of user IDs of close friends, see here for more info.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0xba6705f0
    QUALNAME = "functions.contacts.EditCloseFriends"

    def __init__(self, *, id: List[int]) -> None:
        self.id = id  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditCloseFriends":
        # No flags

        id = TLObject.read(b, Long)

        return EditCloseFriends(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.id, Long))

        return b.getvalue()
