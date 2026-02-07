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


class BotInfo(TLObject):  # type: ignore
    """Localized information about a bot.

    Constructor of :obj:`~pyrogram.raw.base.bots.BotInfo`.

    Details:
        - Layer: ``224``
        - ID: ``E8A775B0``

    Parameters:
        name (``str``):
            Bot name

        about (``str``):
            Bot about text

        description (``str``):
            Bot description

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotInfo
    """

    __slots__: List[str] = ["name", "about", "description"]

    ID = 0xe8a775b0
    QUALNAME = "types.bots.BotInfo"

    def __init__(self, *, name: str, about: str, description: str) -> None:
        self.name = name  # string
        self.about = about  # string
        self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInfo":
        # No flags

        name = String.read(b)

        about = String.read(b)

        description = String.read(b)

        return BotInfo(name=name, about=about, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.name))

        b.write(String(self.about))

        b.write(String(self.description))

        return b.getvalue()
