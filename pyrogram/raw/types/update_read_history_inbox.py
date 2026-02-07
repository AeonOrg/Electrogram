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


class UpdateReadHistoryInbox(TLObject):  # type: ignore
    """Incoming messages were read

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``9E84BC99``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer

        max_id (``int`` ``32-bit``):
            Maximum ID of messages read

        still_unread_count (``int`` ``32-bit``):
            Number of messages that are still unread

        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "max_id", "still_unread_count", "pts", "pts_count", "folder_id", "top_msg_id"]

    ID = 0x9e84bc99
    QUALNAME = "types.UpdateReadHistoryInbox"

    def __init__(self, *, peer: "raw.base.Peer", max_id: int, still_unread_count: int, pts: int, pts_count: int, folder_id: Optional[int] = None, top_msg_id: Optional[int] = None) -> None:
        self.peer = peer  # Peer
        self.max_id = max_id  # int
        self.still_unread_count = still_unread_count  # int
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.folder_id = folder_id  # flags.0?int
        self.top_msg_id = top_msg_id  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadHistoryInbox":

        flags = Int.read(b)

        folder_id = Int.read(b) if flags & (1 << 0) else None
        peer = TLObject.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 1) else None
        max_id = Int.read(b)

        still_unread_count = Int.read(b)

        pts = Int.read(b)

        pts_count = Int.read(b)

        return UpdateReadHistoryInbox(peer=peer, max_id=max_id, still_unread_count=still_unread_count, pts=pts, pts_count=pts_count, folder_id=folder_id, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        flags |= (1 << 1) if self.top_msg_id is not None else 0
        b.write(Int(flags))

        if self.folder_id is not None:
            b.write(Int(self.folder_id))

        b.write(self.peer.write())

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        b.write(Int(self.max_id))

        b.write(Int(self.still_unread_count))

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        return b.getvalue()
