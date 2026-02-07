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


class UpdatePeerBlocked(TLObject):  # type: ignore
    """We blocked a peer, see here » for more info on blocklists.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``EBE07752``

    Parameters:
        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The (un)blocked peer

        blocked (``bool``, *optional*):
            Whether the peer was blocked or unblocked

        blocked_my_stories_from (``bool``, *optional*):
            Whether the peer was added/removed to/from the story blocklist; if not set, this update affects the main blocklist, see here » for more info.

    """

    __slots__: List[str] = ["peer_id", "blocked", "blocked_my_stories_from"]

    ID = 0xebe07752
    QUALNAME = "types.UpdatePeerBlocked"

    def __init__(self, *, peer_id: "raw.base.Peer", blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None) -> None:
        self.peer_id = peer_id  # Peer
        self.blocked = blocked  # flags.0?true
        self.blocked_my_stories_from = blocked_my_stories_from  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerBlocked":

        flags = Int.read(b)

        blocked = True if flags & (1 << 0) else False
        blocked_my_stories_from = True if flags & (1 << 1) else False
        peer_id = TLObject.read(b)

        return UpdatePeerBlocked(peer_id=peer_id, blocked=blocked, blocked_my_stories_from=blocked_my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 1) if self.blocked_my_stories_from else 0
        b.write(Int(flags))

        b.write(self.peer_id.write())

        return b.getvalue()
