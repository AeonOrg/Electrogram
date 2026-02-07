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


class UpdatePeerHistoryTTL(TLObject):  # type: ignore
    """The Time-To-Live for messages sent by the current user in a specific chat has changed

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``BB9BB9A5``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The chat

        ttl_period (``int`` ``32-bit``, *optional*):
            The new Time-To-Live

    """

    __slots__: List[str] = ["peer", "ttl_period"]

    ID = 0xbb9bb9a5
    QUALNAME = "types.UpdatePeerHistoryTTL"

    def __init__(self, *, peer: "raw.base.Peer", ttl_period: Optional[int] = None) -> None:
        self.peer = peer  # Peer
        self.ttl_period = ttl_period  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerHistoryTTL":

        flags = Int.read(b)

        peer = TLObject.read(b)

        ttl_period = Int.read(b) if flags & (1 << 0) else None
        return UpdatePeerHistoryTTL(peer=peer, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ttl_period is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))

        return b.getvalue()
