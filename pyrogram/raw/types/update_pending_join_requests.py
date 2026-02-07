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


class UpdatePendingJoinRequests(TLObject):  # type: ignore
    """Someone has requested to join a chat or channel

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``7063C3DB``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Chat or channel

        requests_pending (``int`` ``32-bit``):
            Number of pending join requests » for the chat or channel

        recent_requesters (List of ``int`` ``64-bit``):
            IDs of users that have recently requested to join

    """

    __slots__: List[str] = ["peer", "requests_pending", "recent_requesters"]

    ID = 0x7063c3db
    QUALNAME = "types.UpdatePendingJoinRequests"

    def __init__(self, *, peer: "raw.base.Peer", requests_pending: int, recent_requesters: List[int]) -> None:
        self.peer = peer  # Peer
        self.requests_pending = requests_pending  # int
        self.recent_requesters = recent_requesters  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePendingJoinRequests":
        # No flags

        peer = TLObject.read(b)

        requests_pending = Int.read(b)

        recent_requesters = TLObject.read(b, Long)

        return UpdatePendingJoinRequests(peer=peer, requests_pending=requests_pending, recent_requesters=recent_requesters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.requests_pending))

        b.write(Vector(self.recent_requesters, Long))

        return b.getvalue()
