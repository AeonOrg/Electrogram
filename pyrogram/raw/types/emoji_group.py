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


class EmojiGroup(TLObject):  # type: ignore
    """Represents an emoji category.

    Constructor of :obj:`~pyrogram.raw.base.EmojiGroup`.

    Details:
        - Layer: ``224``
        - ID: ``7A9ABDA9``

    Parameters:
        title (``str``):
            Category name, i.e. "Animals", "Flags", "Faces" and so on...

        icon_emoji_id (``int`` ``64-bit``):
            A single custom emoji used as preview for the category.

        emoticons (List of ``str``):
            A list of UTF-8 emojis, matching the category.

    """

    __slots__: List[str] = ["title", "icon_emoji_id", "emoticons"]

    ID = 0x7a9abda9
    QUALNAME = "types.EmojiGroup"

    def __init__(self, *, title: str, icon_emoji_id: int, emoticons: List[str]) -> None:
        self.title = title  # string
        self.icon_emoji_id = icon_emoji_id  # long
        self.emoticons = emoticons  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroup":
        # No flags

        title = String.read(b)

        icon_emoji_id = Long.read(b)

        emoticons = TLObject.read(b, String)

        return EmojiGroup(title=title, icon_emoji_id=icon_emoji_id, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.title))

        b.write(Long(self.icon_emoji_id))

        b.write(Vector(self.emoticons, String))

        return b.getvalue()
