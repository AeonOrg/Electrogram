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


class BotMenuButtonCommands(TLObject):  # type: ignore
    """Bot menu button that opens the bot command list when clicked.

    Constructor of :obj:`~pyrogram.raw.base.BotMenuButton`.

    Details:
        - Layer: ``224``
        - ID: ``4258C205``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotMenuButton
    """

    __slots__: List[str] = []

    ID = 0x4258c205
    QUALNAME = "types.BotMenuButtonCommands"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotMenuButtonCommands":
        # No flags

        return BotMenuButtonCommands()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
