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


class UpdateUserName(TLObject):  # type: ignore
    """Changes the user's first name, last name and username.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``A7848924``

    Parameters:
        user_id (``int`` ``64-bit``):
            User identifier

        first_name (``str``):
            New first name. Corresponds to the new value of real_first_name field of the userFull constructor.

        last_name (``str``):
            New last name. Corresponds to the new value of real_last_name field of the userFull constructor.

        usernames (List of :obj:`Username <pyrogram.raw.base.Username>`):
            Usernames.

    """

    __slots__: List[str] = ["user_id", "first_name", "last_name", "usernames"]

    ID = 0xa7848924
    QUALNAME = "types.UpdateUserName"

    def __init__(self, *, user_id: int, first_name: str, last_name: str, usernames: List["raw.base.Username"]) -> None:
        self.user_id = user_id  # long
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.usernames = usernames  # Vector<Username>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserName":
        # No flags

        user_id = Long.read(b)

        first_name = String.read(b)

        last_name = String.read(b)

        usernames = TLObject.read(b)

        return UpdateUserName(user_id=user_id, first_name=first_name, last_name=last_name, usernames=usernames)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.user_id))

        b.write(String(self.first_name))

        b.write(String(self.last_name))

        b.write(Vector(self.usernames))

        return b.getvalue()
