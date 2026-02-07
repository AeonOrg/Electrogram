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


class BotVerification(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotVerification`.

    Details:
        - Layer: ``224``
        - ID: ``F93CD45C``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        icon (``int`` ``64-bit``):
            N/A

        description (``str``):
            N/A

    """

    __slots__: List[str] = ["bot_id", "icon", "description"]

    ID = 0xf93cd45c
    QUALNAME = "types.BotVerification"

    def __init__(self, *, bot_id: int, icon: int, description: str) -> None:
        self.bot_id = bot_id  # long
        self.icon = icon  # long
        self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotVerification":
        # No flags

        bot_id = Long.read(b)

        icon = Long.read(b)

        description = String.read(b)

        return BotVerification(bot_id=bot_id, icon=icon, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.bot_id))

        b.write(Long(self.icon))

        b.write(String(self.description))

        return b.getvalue()
