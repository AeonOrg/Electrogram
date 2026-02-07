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


class StoryItemDeleted(TLObject):  # type: ignore
    """Represents a previously active story, that was deleted

    Constructor of :obj:`~pyrogram.raw.base.StoryItem`.

    Details:
        - Layer: ``224``
        - ID: ``51E6EE4F``

    Parameters:
        id (``int`` ``32-bit``):
            Story ID

    """

    __slots__: List[str] = ["id"]

    ID = 0x51e6ee4f
    QUALNAME = "types.StoryItemDeleted"

    def __init__(self, *, id: int) -> None:
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryItemDeleted":
        # No flags

        id = Int.read(b)

        return StoryItemDeleted(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.id))

        return b.getvalue()
