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


class SetBotCommands(TLObject):  # type: ignore
    """Set bot command list


    Details:
        - Layer: ``224``
        - ID: ``517165A``

    Parameters:
        scope (:obj:`BotCommandScope <pyrogram.raw.base.BotCommandScope>`):
            Command scope

        lang_code (``str``):
            Language code

        commands (List of :obj:`BotCommand <pyrogram.raw.base.BotCommand>`):
            Bot commands

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["scope", "lang_code", "commands"]

    ID = 0x517165a
    QUALNAME = "functions.bots.SetBotCommands"

    def __init__(self, *, scope: "raw.base.BotCommandScope", lang_code: str, commands: List["raw.base.BotCommand"]) -> None:
        self.scope = scope  # BotCommandScope
        self.lang_code = lang_code  # string
        self.commands = commands  # Vector<BotCommand>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotCommands":
        # No flags

        scope = TLObject.read(b)

        lang_code = String.read(b)

        commands = TLObject.read(b)

        return SetBotCommands(scope=scope, lang_code=lang_code, commands=commands)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.scope.write())

        b.write(String(self.lang_code))

        b.write(Vector(self.commands))

        return b.getvalue()
