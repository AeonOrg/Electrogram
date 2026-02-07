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


class UpdateReadMessagesContents(TLObject):  # type: ignore
    """Contents of messages in the common message box were read

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F8227181``

    Parameters:
        messages (List of ``int`` ``32-bit``):
            IDs of read messages

        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

        date (``int`` ``32-bit``, *optional*):
            When was the last message in messages marked as read.

    """

    __slots__: List[str] = ["messages", "pts", "pts_count", "date"]

    ID = 0xf8227181
    QUALNAME = "types.UpdateReadMessagesContents"

    def __init__(self, *, messages: List[int], pts: int, pts_count: int, date: Optional[int] = None) -> None:
        self.messages = messages  # Vector<int>
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.date = date  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadMessagesContents":

        flags = Int.read(b)

        messages = TLObject.read(b, Int)

        pts = Int.read(b)

        pts_count = Int.read(b)

        date = Int.read(b) if flags & (1 << 0) else None
        return UpdateReadMessagesContents(messages=messages, pts=pts, pts_count=pts_count, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.date is not None else 0
        b.write(Int(flags))

        b.write(Vector(self.messages, Int))

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        if self.date is not None:
            b.write(Int(self.date))

        return b.getvalue()
