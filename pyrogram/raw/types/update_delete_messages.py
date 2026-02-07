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


class UpdateDeleteMessages(TLObject):  # type: ignore
    """Messages were deleted.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``A20DB0E5``

    Parameters:
        messages (List of ``int`` ``32-bit``):
            List of identifiers of deleted messages

        pts (``int`` ``32-bit``):
            New quality of actions in a message box

        pts_count (``int`` ``32-bit``):
            Number of generated events

    """

    __slots__: List[str] = ["messages", "pts", "pts_count"]

    ID = 0xa20db0e5
    QUALNAME = "types.UpdateDeleteMessages"

    def __init__(self, *, messages: List[int], pts: int, pts_count: int) -> None:
        self.messages = messages  # Vector<int>
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeleteMessages":
        # No flags

        messages = TLObject.read(b, Int)

        pts = Int.read(b)

        pts_count = Int.read(b)

        return UpdateDeleteMessages(messages=messages, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.messages, Int))

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        return b.getvalue()
