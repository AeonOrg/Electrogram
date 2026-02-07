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


class StoryItemSkipped(TLObject):  # type: ignore
    """Represents an active story, whose full information was omitted for space and performance reasons; use stories.getStoriesByID to fetch full info about the skipped story when and if needed.

    Constructor of :obj:`~pyrogram.raw.base.StoryItem`.

    Details:
        - Layer: ``224``
        - ID: ``FFADC913``

    Parameters:
        id (``int`` ``32-bit``):
            Story ID

        date (``int`` ``32-bit``):
            When was the story posted.

        expire_date (``int`` ``32-bit``):
            When does the story expire.

        close_friends (``bool``, *optional*):
            Whether this story can only be viewed by our close friends, see here » for more info

        live (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "date", "expire_date", "close_friends", "live"]

    ID = 0xffadc913
    QUALNAME = "types.StoryItemSkipped"

    def __init__(self, *, id: int, date: int, expire_date: int, close_friends: Optional[bool] = None, live: Optional[bool] = None) -> None:
        self.id = id  # int
        self.date = date  # int
        self.expire_date = expire_date  # int
        self.close_friends = close_friends  # flags.8?true
        self.live = live  # flags.9?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryItemSkipped":

        flags = Int.read(b)

        close_friends = True if flags & (1 << 8) else False
        live = True if flags & (1 << 9) else False
        id = Int.read(b)

        date = Int.read(b)

        expire_date = Int.read(b)

        return StoryItemSkipped(id=id, date=date, expire_date=expire_date, close_friends=close_friends, live=live)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 8) if self.close_friends else 0
        flags |= (1 << 9) if self.live else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        b.write(Int(self.date))

        b.write(Int(self.expire_date))

        return b.getvalue()
