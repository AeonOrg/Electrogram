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


class InputGameShortName(TLObject):  # type: ignore
    """Game by short name

    Constructor of :obj:`~pyrogram.raw.base.InputGame`.

    Details:
        - Layer: ``224``
        - ID: ``C331E80A``

    Parameters:
        bot_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            The bot that provides the game

        short_name (``str``):
            The game's short name, usually obtained from a game link »

    """

    __slots__: List[str] = ["bot_id", "short_name"]

    ID = 0xc331e80a
    QUALNAME = "types.InputGameShortName"

    def __init__(self, *, bot_id: "raw.base.InputUser", short_name: str) -> None:
        self.bot_id = bot_id  # InputUser
        self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGameShortName":
        # No flags

        bot_id = TLObject.read(b)

        short_name = String.read(b)

        return InputGameShortName(bot_id=bot_id, short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot_id.write())

        b.write(String(self.short_name))

        return b.getvalue()
