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


class PrivacyRules(TLObject):  # type: ignore
    """Privacy rules

    Constructor of :obj:`~pyrogram.raw.base.account.PrivacyRules`.

    Details:
        - Layer: ``224``
        - ID: ``50A04E45``

    Parameters:
        rules (List of :obj:`PrivacyRule <pyrogram.raw.base.PrivacyRule>`):
            Privacy rules

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            Chats to which the rules apply

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Users to which the rules apply

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPrivacy
            account.SetPrivacy
    """

    __slots__: List[str] = ["rules", "chats", "users"]

    ID = 0x50a04e45
    QUALNAME = "types.account.PrivacyRules"

    def __init__(self, *, rules: List["raw.base.PrivacyRule"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.rules = rules  # Vector<PrivacyRule>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyRules":
        # No flags

        rules = TLObject.read(b)

        chats = TLObject.read(b)

        users = TLObject.read(b)

        return PrivacyRules(rules=rules, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.rules))

        b.write(Vector(self.chats))

        b.write(Vector(self.users))

        return b.getvalue()
