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


class ToggleBotInAttachMenu(TLObject):  # type: ignore
    """Enable or disable web bot attachment menu »


    Details:
        - Layer: ``224``
        - ID: ``69F59D69``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Bot ID

        enabled (``bool``):
            Toggle

        write_allowed (``bool``, *optional*):
            Whether the user authorizes the bot to write messages to them, if requested by attachMenuBot.request_write_access

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot", "enabled", "write_allowed"]

    ID = 0x69f59d69
    QUALNAME = "functions.messages.ToggleBotInAttachMenu"

    def __init__(self, *, bot: "raw.base.InputUser", enabled: bool, write_allowed: Optional[bool] = None) -> None:
        self.bot = bot  # InputUser
        self.enabled = enabled  # Bool
        self.write_allowed = write_allowed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleBotInAttachMenu":

        flags = Int.read(b)

        write_allowed = True if flags & (1 << 0) else False
        bot = TLObject.read(b)

        enabled = Bool.read(b)

        return ToggleBotInAttachMenu(bot=bot, enabled=enabled, write_allowed=write_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.write_allowed else 0
        b.write(Int(flags))

        b.write(self.bot.write())

        b.write(Bool(self.enabled))

        return b.getvalue()
