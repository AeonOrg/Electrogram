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


class AttachMenuBotsBot(TLObject):  # type: ignore
    """Represents a bot mini app that can be launched from the attachment menu »

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuBotsBot`.

    Details:
        - Layer: ``224``
        - ID: ``93BF667F``

    Parameters:
        bot (:obj:`AttachMenuBot <pyrogram.raw.base.AttachMenuBot>`):
            Represents a bot mini app that can be launched from the attachment menu »

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            Info about related users and bots

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBot
    """

    __slots__: List[str] = ["bot", "users"]

    ID = 0x93bf667f
    QUALNAME = "types.AttachMenuBotsBot"

    def __init__(self, *, bot: "raw.base.AttachMenuBot", users: List["raw.base.User"]) -> None:
        self.bot = bot  # AttachMenuBot
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotsBot":
        # No flags

        bot = TLObject.read(b)

        users = TLObject.read(b)

        return AttachMenuBotsBot(bot=bot, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot.write())

        b.write(Vector(self.users))

        return b.getvalue()
