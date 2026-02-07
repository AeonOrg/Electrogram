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


class MyBoosts(TLObject):  # type: ignore
    """A list of peers we are currently boosting, and how many boost slots we have left.

    Constructor of :obj:`~pyrogram.raw.base.premium.MyBoosts`.

    Details:
        - Layer: ``224``
        - ID: ``9AE228E2``

    Parameters:
        my_boosts (List of :obj:`MyBoost <pyrogram.raw.base.MyBoost>`):
            Info about boosted peers and remaining boost slots.

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Referenced chats

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Referenced users

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            premium.GetMyBoosts
            premium.ApplyBoost
    """

    __slots__: List[str] = ["my_boosts", "chats", "users"]

    ID = 0x9ae228e2
    QUALNAME = "types.premium.MyBoosts"

    def __init__(self, *, my_boosts: List["raw.base.MyBoost"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.my_boosts = my_boosts  # Vector<MyBoost>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MyBoosts":
        # No flags

        my_boosts = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return MyBoosts(my_boosts=my_boosts, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.my_boosts))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
