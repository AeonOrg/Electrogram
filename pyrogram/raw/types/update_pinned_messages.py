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


class UpdatePinnedMessages(TLObject):  # type: ignore
    """Some messages were pinned in a chat

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``ED85EAB5``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer

        messages (List of ``int`` ``32-bit``):
            Message IDs

        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

        pinned (``bool``, *optional*):
            Whether the messages were pinned or unpinned

    """

    __slots__: List[str] = ["peer", "messages", "pts", "pts_count", "pinned"]

    ID = 0xed85eab5
    QUALNAME = "types.UpdatePinnedMessages"

    def __init__(self, *, peer: "raw.base.Peer", messages: List[int], pts: int, pts_count: int, pinned: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.messages = messages  # Vector<int>
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.pinned = pinned  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedMessages":

        flags = Int.read(b)

        pinned = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        messages = TLObject.read(b, Int)

        pts = Int.read(b)

        pts_count = Int.read(b)

        return UpdatePinnedMessages(peer=peer, messages=messages, pts=pts, pts_count=pts_count, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Vector(self.messages, Int))

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        return b.getvalue()
