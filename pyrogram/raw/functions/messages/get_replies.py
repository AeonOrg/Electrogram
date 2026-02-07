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


class GetReplies(TLObject):  # type: ignore
    """Get messages in a reply thread


    Details:
        - Layer: ``224``
        - ID: ``22DDD30C``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer

        msg_id (``int`` ``32-bit``):
            Message ID

        offset_id (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        offset_date (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        add_offset (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        max_id (``int`` ``32-bit``):
            If a positive value was transferred, the method will return only messages with ID smaller than max_id

        min_id (``int`` ``32-bit``):
            If a positive value was transferred, the method will return only messages with ID bigger than min_id

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "msg_id", "offset_id", "offset_date", "add_offset", "limit", "max_id", "min_id", "hash"]

    ID = 0x22ddd30c
    QUALNAME = "functions.messages.GetReplies"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, offset_id: int, offset_date: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.offset_id = offset_id  # int
        self.offset_date = offset_date  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetReplies":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        offset_id = Int.read(b)

        offset_date = Int.read(b)

        add_offset = Int.read(b)

        limit = Int.read(b)

        max_id = Int.read(b)

        min_id = Int.read(b)

        hash = Long.read(b)

        return GetReplies(peer=peer, msg_id=msg_id, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Int(self.offset_id))

        b.write(Int(self.offset_date))

        b.write(Int(self.add_offset))

        b.write(Int(self.limit))

        b.write(Int(self.max_id))

        b.write(Int(self.min_id))

        b.write(Long(self.hash))

        return b.getvalue()
