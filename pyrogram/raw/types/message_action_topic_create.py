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


class MessageActionTopicCreate(TLObject):  # type: ignore
    """A forum topic was created.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``D999256``

    Parameters:
        title (``str``):
            Topic name.

        icon_color (``int`` ``32-bit``):
            If no custom emoji icon is specified, specifies the color of the fallback topic icon (RGB), one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F.

        title_missing (``bool``, *optional*):
            N/A

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            ID of the custom emoji used as topic icon.

    """

    __slots__: List[str] = ["title", "icon_color", "title_missing", "icon_emoji_id"]

    ID = 0xd999256
    QUALNAME = "types.MessageActionTopicCreate"

    def __init__(self, *, title: str, icon_color: int, title_missing: Optional[bool] = None, icon_emoji_id: Optional[int] = None) -> None:
        self.title = title  # string
        self.icon_color = icon_color  # int
        self.title_missing = title_missing  # flags.1?true
        self.icon_emoji_id = icon_emoji_id  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTopicCreate":

        flags = Int.read(b)

        title_missing = True if flags & (1 << 1) else False
        title = String.read(b)

        icon_color = Int.read(b)

        icon_emoji_id = Long.read(b) if flags & (1 << 0) else None
        return MessageActionTopicCreate(title=title, icon_color=icon_color, title_missing=title_missing, icon_emoji_id=icon_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.title_missing else 0
        flags |= (1 << 0) if self.icon_emoji_id is not None else 0
        b.write(Int(flags))

        b.write(String(self.title))

        b.write(Int(self.icon_color))

        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))

        return b.getvalue()
