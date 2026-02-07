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


class ToggleUsername(TLObject):  # type: ignore
    """Activate or deactivate a purchased fragment.com username associated to a bot we own.


    Details:
        - Layer: ``224``
        - ID: ``53CA973``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            The bot

        username (``str``):
            Username

        active (``bool``):
            Whether to activate or deactivate it

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot", "username", "active"]

    ID = 0x53ca973
    QUALNAME = "functions.bots.ToggleUsername"

    def __init__(self, *, bot: "raw.base.InputUser", username: str, active: bool) -> None:
        self.bot = bot  # InputUser
        self.username = username  # string
        self.active = active  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleUsername":
        # No flags

        bot = TLObject.read(b)

        username = String.read(b)

        active = Bool.read(b)

        return ToggleUsername(bot=bot, username=username, active=active)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot.write())

        b.write(String(self.username))

        b.write(Bool(self.active))

        return b.getvalue()
