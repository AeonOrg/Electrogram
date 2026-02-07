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


class GetPreviewInfo(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``423AB3AD``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        lang_code (``str``):
            N/A

    Returns:
        :obj:`bots.PreviewInfo <pyrogram.raw.base.bots.PreviewInfo>`
    """

    __slots__: List[str] = ["bot", "lang_code"]

    ID = 0x423ab3ad
    QUALNAME = "functions.bots.GetPreviewInfo"

    def __init__(self, *, bot: "raw.base.InputUser", lang_code: str) -> None:
        self.bot = bot  # InputUser
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPreviewInfo":
        # No flags

        bot = TLObject.read(b)

        lang_code = String.read(b)

        return GetPreviewInfo(bot=bot, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot.write())

        b.write(String(self.lang_code))

        return b.getvalue()
