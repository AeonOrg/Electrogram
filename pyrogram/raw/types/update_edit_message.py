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


class UpdateEditMessage(TLObject):  # type: ignore
    """A message was edited

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``E40370A3``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            The new edited message

        pts (``int`` ``32-bit``):
            PTS

        pts_count (``int`` ``32-bit``):
            PTS count

    """

    __slots__: List[str] = ["message", "pts", "pts_count"]

    ID = 0xe40370a3
    QUALNAME = "types.UpdateEditMessage"

    def __init__(self, *, message: "raw.base.Message", pts: int, pts_count: int) -> None:
        self.message = message  # Message
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEditMessage":
        # No flags

        message = TLObject.read(b)

        pts = Int.read(b)

        pts_count = Int.read(b)

        return UpdateEditMessage(message=message, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.message.write())

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        return b.getvalue()
