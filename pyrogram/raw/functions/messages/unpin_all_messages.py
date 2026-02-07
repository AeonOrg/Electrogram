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


class UnpinAllMessages(TLObject):  # type: ignore
    """Unpin all pinned messages


    Details:
        - Layer: ``224``
        - ID: ``62DD747``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Chat where to unpin

        top_msg_id (``int`` ``32-bit``, *optional*):
            Forum topic where to unpin

        saved_peer_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`messages.AffectedHistory <pyrogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["peer", "top_msg_id", "saved_peer_id"]

    ID = 0x62dd747
    QUALNAME = "functions.messages.UnpinAllMessages"

    def __init__(self, *, peer: "raw.base.InputPeer", top_msg_id: Optional[int] = None, saved_peer_id: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.top_msg_id = top_msg_id  # flags.0?int
        self.saved_peer_id = saved_peer_id  # flags.1?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UnpinAllMessages":

        flags = Int.read(b)

        peer = TLObject.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        saved_peer_id = TLObject.read(b) if flags & (1 << 1) else None

        return UnpinAllMessages(peer=peer, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        flags |= (1 << 1) if self.saved_peer_id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())

        return b.getvalue()
