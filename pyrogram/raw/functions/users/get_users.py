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


class GetUsers(TLObject):  # type: ignore
    """Returns basic user info according to their identifiers.


    Details:
        - Layer: ``224``
        - ID: ``D91A548``

    Parameters:
        id (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            List of user identifiers

    Returns:
        List of :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xd91a548
    QUALNAME = "functions.users.GetUsers"

    def __init__(self, *, id: List["raw.base.InputUser"]) -> None:
        self.id = id  # Vector<InputUser>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUsers":
        # No flags

        id = TLObject.read(b)

        return GetUsers(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.id))

        return b.getvalue()
