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


class InputBotAppShortName(TLObject):  # type: ignore
    """Used to fetch information about a direct link Mini App by its short name

    Constructor of :obj:`~pyrogram.raw.base.InputBotApp`.

    Details:
        - Layer: ``224``
        - ID: ``908C0407``

    Parameters:
        bot_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            ID of the bot that owns the bot mini app

        short_name (``str``):
            Short name, obtained from a Direct Mini App deep link

    """

    __slots__: List[str] = ["bot_id", "short_name"]

    ID = 0x908c0407
    QUALNAME = "types.InputBotAppShortName"

    def __init__(self, *, bot_id: "raw.base.InputUser", short_name: str) -> None:
        self.bot_id = bot_id  # InputUser
        self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotAppShortName":
        # No flags

        bot_id = TLObject.read(b)

        short_name = String.read(b)

        return InputBotAppShortName(bot_id=bot_id, short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot_id.write())

        b.write(String(self.short_name))

        return b.getvalue()
