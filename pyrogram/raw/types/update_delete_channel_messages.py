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


class UpdateDeleteChannelMessages(TLObject):  # type: ignore
    """Some messages in a supergroup/channel were deleted

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``C32D5B12``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

        messages (List of ``int`` ``32-bit``):
            IDs of messages that were deleted

        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

    """

    __slots__: List[str] = ["channel_id", "messages", "pts", "pts_count"]

    ID = 0xc32d5b12
    QUALNAME = "types.UpdateDeleteChannelMessages"

    def __init__(self, *, channel_id: int, messages: List[int], pts: int, pts_count: int) -> None:
        self.channel_id = channel_id  # long
        self.messages = messages  # Vector<int>
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeleteChannelMessages":
        # No flags

        channel_id = Long.read(b)

        messages = TLObject.read(b, Int)

        pts = Int.read(b)

        pts_count = Int.read(b)

        return UpdateDeleteChannelMessages(channel_id=channel_id, messages=messages, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(Vector(self.messages, Int))

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        return b.getvalue()
