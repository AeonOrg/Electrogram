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


class UpdateChannelTooLong(TLObject):  # type: ignore
    """There are new updates in the specified channel, the client must fetch them.
If the difference is too long or if the channel isn't currently in the states, start fetching from the specified pts.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``108D941F``

    Parameters:
        channel_id (``int`` ``64-bit``):
            The channel

        pts (``int`` ``32-bit``, *optional*):
            The PTS.

    """

    __slots__: List[str] = ["channel_id", "pts"]

    ID = 0x108d941f
    QUALNAME = "types.UpdateChannelTooLong"

    def __init__(self, *, channel_id: int, pts: Optional[int] = None) -> None:
        self.channel_id = channel_id  # long
        self.pts = pts  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelTooLong":

        flags = Int.read(b)

        channel_id = Long.read(b)

        pts = Int.read(b) if flags & (1 << 0) else None
        return UpdateChannelTooLong(channel_id=channel_id, pts=pts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pts is not None else 0
        b.write(Int(flags))

        b.write(Long(self.channel_id))

        if self.pts is not None:
            b.write(Int(self.pts))

        return b.getvalue()
