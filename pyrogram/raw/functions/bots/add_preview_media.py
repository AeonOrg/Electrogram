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


class AddPreviewMedia(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``17AEB75A``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        lang_code (``str``):
            N/A

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            N/A

    Returns:
        :obj:`BotPreviewMedia <pyrogram.raw.base.BotPreviewMedia>`
    """

    __slots__: List[str] = ["bot", "lang_code", "media"]

    ID = 0x17aeb75a
    QUALNAME = "functions.bots.AddPreviewMedia"

    def __init__(self, *, bot: "raw.base.InputUser", lang_code: str, media: "raw.base.InputMedia") -> None:
        self.bot = bot  # InputUser
        self.lang_code = lang_code  # string
        self.media = media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddPreviewMedia":
        # No flags

        bot = TLObject.read(b)

        lang_code = String.read(b)

        media = TLObject.read(b)

        return AddPreviewMedia(bot=bot, lang_code=lang_code, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot.write())

        b.write(String(self.lang_code))

        b.write(self.media.write())

        return b.getvalue()
