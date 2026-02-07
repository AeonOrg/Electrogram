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


class ChatThemeUniqueGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatTheme`.

    Details:
        - Layer: ``224``
        - ID: ``3458F9C8``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        theme_settings (List of :obj:`ThemeSettings <pyrogram.raw.base.ThemeSettings>`):
            N/A

    """

    __slots__: List[str] = ["gift", "theme_settings"]

    ID = 0x3458f9c8
    QUALNAME = "types.ChatThemeUniqueGift"

    def __init__(self, *, gift: "raw.base.StarGift", theme_settings: List["raw.base.ThemeSettings"]) -> None:
        self.gift = gift  # StarGift
        self.theme_settings = theme_settings  # Vector<ThemeSettings>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatThemeUniqueGift":
        # No flags

        gift = TLObject.read(b)

        theme_settings = TLObject.read(b)

        return ChatThemeUniqueGift(gift=gift, theme_settings=theme_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.gift.write())

        b.write(Vector(self.theme_settings))

        return b.getvalue()
