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


class ToggleUserEmojiStatusPermission(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6DE6392``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        enabled (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot", "enabled"]

    ID = 0x6de6392
    QUALNAME = "functions.bots.ToggleUserEmojiStatusPermission"

    def __init__(self, *, bot: "raw.base.InputUser", enabled: bool) -> None:
        self.bot = bot  # InputUser
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleUserEmojiStatusPermission":
        # No flags

        bot = TLObject.read(b)

        enabled = Bool.read(b)

        return ToggleUserEmojiStatusPermission(bot=bot, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot.write())

        b.write(Bool(self.enabled))

        return b.getvalue()
