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


class GetBotInfo(TLObject):  # type: ignore
    """Get localized name, about text and description of a bot (or of the current account, if called by a bot).


    Details:
        - Layer: ``224``
        - ID: ``DCD914FD``

    Parameters:
        lang_code (``str``):
            Language code, if left empty this method will return the fallback about text and description.

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            If called by a user, must contain the peer of a bot we own.

    Returns:
        :obj:`bots.BotInfo <pyrogram.raw.base.bots.BotInfo>`
    """

    __slots__: List[str] = ["lang_code", "bot"]

    ID = 0xdcd914fd
    QUALNAME = "functions.bots.GetBotInfo"

    def __init__(self, *, lang_code: str, bot: "raw.base.InputUser" = None) -> None:
        self.lang_code = lang_code  # string
        self.bot = bot  # flags.0?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotInfo":

        flags = Int.read(b)

        bot = TLObject.read(b) if flags & (1 << 0) else None

        lang_code = String.read(b)

        return GetBotInfo(lang_code=lang_code, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.bot is not None else 0
        b.write(Int(flags))

        if self.bot is not None:
            b.write(self.bot.write())

        b.write(String(self.lang_code))

        return b.getvalue()
