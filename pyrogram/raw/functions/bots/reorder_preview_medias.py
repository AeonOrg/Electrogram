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


class ReorderPreviewMedias(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B627F3AA``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        lang_code (``str``):
            N/A

        order (List of :obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot", "lang_code", "order"]

    ID = 0xb627f3aa
    QUALNAME = "functions.bots.ReorderPreviewMedias"

    def __init__(self, *, bot: "raw.base.InputUser", lang_code: str, order: List["raw.base.InputMedia"]) -> None:
        self.bot = bot  # InputUser
        self.lang_code = lang_code  # string
        self.order = order  # Vector<InputMedia>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderPreviewMedias":
        # No flags

        bot = TLObject.read(b)

        lang_code = String.read(b)

        order = TLObject.read(b)

        return ReorderPreviewMedias(bot=bot, lang_code=lang_code, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot.write())

        b.write(String(self.lang_code))

        b.write(Vector(self.order))

        return b.getvalue()
