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


class GetBotMenuButton(TLObject):  # type: ignore
    """Gets the menu button action for a given user or for all users, previously set using bots.setBotMenuButton; users can see this information in the botInfo constructor.


    Details:
        - Layer: ``224``
        - ID: ``9C60EB28``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            User ID or empty for the default menu button.

    Returns:
        :obj:`BotMenuButton <pyrogram.raw.base.BotMenuButton>`
    """

    __slots__: List[str] = ["user_id"]

    ID = 0x9c60eb28
    QUALNAME = "functions.bots.GetBotMenuButton"

    def __init__(self, *, user_id: "raw.base.InputUser") -> None:
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotMenuButton":
        # No flags

        user_id = TLObject.read(b)

        return GetBotMenuButton(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.user_id.write())

        return b.getvalue()
