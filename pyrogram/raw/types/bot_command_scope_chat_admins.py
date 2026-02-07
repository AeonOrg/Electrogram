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


class BotCommandScopeChatAdmins(TLObject):  # type: ignore
    """The specified bot commands will be valid only for chat administrators, in all groups and supergroups.

    Constructor of :obj:`~pyrogram.raw.base.BotCommandScope`.

    Details:
        - Layer: ``224``
        - ID: ``B9AA606A``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xb9aa606a
    QUALNAME = "types.BotCommandScopeChatAdmins"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCommandScopeChatAdmins":
        # No flags

        return BotCommandScopeChatAdmins()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
