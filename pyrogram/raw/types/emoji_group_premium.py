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


class EmojiGroupPremium(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.EmojiGroup`.

    Details:
        - Layer: ``224``
        - ID: ``93BCF34``

    Parameters:
        title (``str``):


        icon_emoji_id (``int`` ``64-bit``):


    """

    __slots__: List[str] = ["title", "icon_emoji_id"]

    ID = 0x93bcf34
    QUALNAME = "types.EmojiGroupPremium"

    def __init__(self, *, title: str, icon_emoji_id: int) -> None:
        self.title = title  # string
        self.icon_emoji_id = icon_emoji_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroupPremium":
        # No flags

        title = String.read(b)

        icon_emoji_id = Long.read(b)

        return EmojiGroupPremium(title=title, icon_emoji_id=icon_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.title))

        b.write(Long(self.icon_emoji_id))

        return b.getvalue()
