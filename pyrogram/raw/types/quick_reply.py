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


class QuickReply(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.QuickReply`.

    Details:
        - Layer: ``224``
        - ID: ``697102B``

    Parameters:
        shortcut_id (``int`` ``32-bit``):


        shortcut (``str``):


        top_message (``int`` ``32-bit``):


        count (``int`` ``32-bit``):


    """

    __slots__: List[str] = ["shortcut_id", "shortcut", "top_message", "count"]

    ID = 0x697102b
    QUALNAME = "types.QuickReply"

    def __init__(self, *, shortcut_id: int, shortcut: str, top_message: int, count: int) -> None:
        self.shortcut_id = shortcut_id  # int
        self.shortcut = shortcut  # string
        self.top_message = top_message  # int
        self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "QuickReply":
        # No flags

        shortcut_id = Int.read(b)

        shortcut = String.read(b)

        top_message = Int.read(b)

        count = Int.read(b)

        return QuickReply(shortcut_id=shortcut_id, shortcut=shortcut, top_message=top_message, count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.shortcut_id))

        b.write(String(self.shortcut))

        b.write(Int(self.top_message))

        b.write(Int(self.count))

        return b.getvalue()
