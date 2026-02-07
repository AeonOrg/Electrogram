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


class GetBotCommands(TLObject):  # type: ignore
    """Obtain a list of bot commands for the specified bot scope and language code


    Details:
        - Layer: ``224``
        - ID: ``E34C0DD6``

    Parameters:
        scope (:obj:`BotCommandScope <pyrogram.raw.base.BotCommandScope>`):
            Command scope

        lang_code (``str``):
            Language code

    Returns:
        List of :obj:`BotCommand <pyrogram.raw.base.BotCommand>`
    """

    __slots__: List[str] = ["scope", "lang_code"]

    ID = 0xe34c0dd6
    QUALNAME = "functions.bots.GetBotCommands"

    def __init__(self, *, scope: "raw.base.BotCommandScope", lang_code: str) -> None:
        self.scope = scope  # BotCommandScope
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotCommands":
        # No flags

        scope = TLObject.read(b)

        lang_code = String.read(b)

        return GetBotCommands(scope=scope, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.scope.write())

        b.write(String(self.lang_code))

        return b.getvalue()
