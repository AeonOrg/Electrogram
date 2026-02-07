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


class GetSavedHistory(TLObject):  # type: ignore
    """Returns saved messages » forwarded from a specific peer


    Details:
        - Layer: ``224``
        - ID: ``998AB009``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Target peer

        offset_id (``int`` ``32-bit``):
            Only return messages starting from the specified message ID

        offset_date (``int`` ``32-bit``):
            Only return messages sent before the specified date

        add_offset (``int`` ``32-bit``):
            Number of list elements to be skipped, negative values are also accepted.

        limit (``int`` ``32-bit``):
            Number of results to return

        max_id (``int`` ``32-bit``):
            If a positive value was transferred, the method will return only messages with IDs less than max_id

        min_id (``int`` ``32-bit``):
            If a positive value was transferred, the method will return only messages with IDs more than min_id

        hash (``int`` ``64-bit``):
            Result hash

        parent_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "offset_id", "offset_date", "add_offset", "limit", "max_id", "min_id", "hash", "parent_peer"]

    ID = 0x998ab009
    QUALNAME = "functions.messages.GetSavedHistory"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_id: int, offset_date: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, parent_peer: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.offset_id = offset_id  # int
        self.offset_date = offset_date  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.hash = hash  # long
        self.parent_peer = parent_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedHistory":

        flags = Int.read(b)

        parent_peer = TLObject.read(b) if flags & (1 << 0) else None

        peer = TLObject.read(b)

        offset_id = Int.read(b)

        offset_date = Int.read(b)

        add_offset = Int.read(b)

        limit = Int.read(b)

        max_id = Int.read(b)

        min_id = Int.read(b)

        hash = Long.read(b)

        return GetSavedHistory(peer=peer, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash, parent_peer=parent_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.parent_peer is not None else 0
        b.write(Int(flags))

        if self.parent_peer is not None:
            b.write(self.parent_peer.write())

        b.write(self.peer.write())

        b.write(Int(self.offset_id))

        b.write(Int(self.offset_date))

        b.write(Int(self.add_offset))

        b.write(Int(self.limit))

        b.write(Int(self.max_id))

        b.write(Int(self.min_id))

        b.write(Long(self.hash))

        return b.getvalue()
