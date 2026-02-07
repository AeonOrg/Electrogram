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


class GetUnreadMentions(TLObject):  # type: ignore
    """Get unread messages where we were mentioned


    Details:
        - Layer: ``224``
        - ID: ``F107E790``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer where to look for mentions

        offset_id (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        add_offset (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        max_id (``int`` ``32-bit``):
            Maximum message ID to return, see pagination

        min_id (``int`` ``32-bit``):
            Minimum message ID to return, see pagination

        top_msg_id (``int`` ``32-bit``, *optional*):
            If set, considers only messages within the specified forum topic

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "offset_id", "add_offset", "limit", "max_id", "min_id", "top_msg_id"]

    ID = 0xf107e790
    QUALNAME = "functions.messages.GetUnreadMentions"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset_id = offset_id  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUnreadMentions":

        flags = Int.read(b)

        peer = TLObject.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        offset_id = Int.read(b)

        add_offset = Int.read(b)

        limit = Int.read(b)

        max_id = Int.read(b)

        min_id = Int.read(b)

        return GetUnreadMentions(peer=peer, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        b.write(Int(self.offset_id))

        b.write(Int(self.add_offset))

        b.write(Int(self.limit))

        b.write(Int(self.max_id))

        b.write(Int(self.min_id))

        return b.getvalue()
