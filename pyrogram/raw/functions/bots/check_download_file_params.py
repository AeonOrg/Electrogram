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


class CheckDownloadFileParams(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``50077589``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        file_name (``str``):
            N/A

        url (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot", "file_name", "url"]

    ID = 0x50077589
    QUALNAME = "functions.bots.CheckDownloadFileParams"

    def __init__(self, *, bot: "raw.base.InputUser", file_name: str, url: str) -> None:
        self.bot = bot  # InputUser
        self.file_name = file_name  # string
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckDownloadFileParams":
        # No flags

        bot = TLObject.read(b)

        file_name = String.read(b)

        url = String.read(b)

        return CheckDownloadFileParams(bot=bot, file_name=file_name, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot.write())

        b.write(String(self.file_name))

        b.write(String(self.url))

        return b.getvalue()
