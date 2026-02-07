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


class UpdateNewChannelMessage(TLObject):  # type: ignore
    """A new message was sent in a channel/supergroup

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``62BA04D9``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            New message

        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

    """

    __slots__: List[str] = ["message", "pts", "pts_count"]

    ID = 0x62ba04d9
    QUALNAME = "types.UpdateNewChannelMessage"

    def __init__(self, *, message: "raw.base.Message", pts: int, pts_count: int) -> None:
        self.message = message  # Message
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewChannelMessage":
        # No flags

        message = TLObject.read(b)

        pts = Int.read(b)

        pts_count = Int.read(b)

        return UpdateNewChannelMessage(message=message, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.message.write())

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        return b.getvalue()
