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


class GroupCallStars(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.phone.GroupCallStars`.

    Details:
        - Layer: ``224``
        - ID: ``9D1DBD26``

    Parameters:
        total_stars (``int`` ``64-bit``):
            N/A

        top_donors (List of :obj:`GroupCallDonor <pyrogram.raw.base.GroupCallDonor>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallStars
    """

    __slots__: List[str] = ["total_stars", "top_donors", "chats", "users"]

    ID = 0x9d1dbd26
    QUALNAME = "types.phone.GroupCallStars"

    def __init__(self, *, total_stars: int, top_donors: List["raw.base.GroupCallDonor"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.total_stars = total_stars  # long
        self.top_donors = top_donors  # Vector<GroupCallDonor>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStars":
        # No flags

        total_stars = Long.read(b)

        top_donors = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return GroupCallStars(total_stars=total_stars, top_donors=top_donors, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.total_stars))

        b.write(Vector(self.top_donors))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
