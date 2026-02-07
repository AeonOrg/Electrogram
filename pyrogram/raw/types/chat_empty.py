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


class ChatEmpty(TLObject):  # type: ignore
    """Empty constructor, group doesn't exist

    Constructor of :obj:`~pyrogram.raw.base.Chat`.

    Details:
        - Layer: ``224``
        - ID: ``29562865``

    Parameters:
        id (``int`` ``64-bit``):
            Group identifier

    """

    __slots__: List[str] = ["id"]

    ID = 0x29562865
    QUALNAME = "types.ChatEmpty"

    def __init__(self, *, id: int) -> None:
        self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatEmpty":
        # No flags

        id = Long.read(b)

        return ChatEmpty(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        return b.getvalue()
