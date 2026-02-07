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


class TodoItem(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.TodoItem`.

    Details:
        - Layer: ``224``
        - ID: ``CBA9A52F``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        title (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

    """

    __slots__: List[str] = ["id", "title"]

    ID = 0xcba9a52f
    QUALNAME = "types.TodoItem"

    def __init__(self, *, id: int, title: "raw.base.TextWithEntities") -> None:
        self.id = id  # int
        self.title = title  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TodoItem":
        # No flags

        id = Int.read(b)

        title = TLObject.read(b)

        return TodoItem(id=id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.id))

        b.write(self.title.write())

        return b.getvalue()
