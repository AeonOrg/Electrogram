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


class UpdateReadChannelInbox(TLObject):  # type: ignore
    """Incoming messages in a channel/supergroup were read

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``922E6E10``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel/supergroup ID

        max_id (``int`` ``32-bit``):
            Position up to which all incoming messages are read.

        still_unread_count (``int`` ``32-bit``):
            Count of messages weren't read yet

        pts (``int`` ``32-bit``):
            Event count after generation

        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

    """

    __slots__: List[str] = ["channel_id", "max_id", "still_unread_count", "pts", "folder_id"]

    ID = 0x922e6e10
    QUALNAME = "types.UpdateReadChannelInbox"

    def __init__(self, *, channel_id: int, max_id: int, still_unread_count: int, pts: int, folder_id: Optional[int] = None) -> None:
        self.channel_id = channel_id  # long
        self.max_id = max_id  # int
        self.still_unread_count = still_unread_count  # int
        self.pts = pts  # int
        self.folder_id = folder_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadChannelInbox":

        flags = Int.read(b)

        folder_id = Int.read(b) if flags & (1 << 0) else None
        channel_id = Long.read(b)

        max_id = Int.read(b)

        still_unread_count = Int.read(b)

        pts = Int.read(b)

        return UpdateReadChannelInbox(channel_id=channel_id, max_id=max_id, still_unread_count=still_unread_count, pts=pts, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        b.write(Int(flags))

        if self.folder_id is not None:
            b.write(Int(self.folder_id))

        b.write(Long(self.channel_id))

        b.write(Int(self.max_id))

        b.write(Int(self.still_unread_count))

        b.write(Int(self.pts))

        return b.getvalue()
