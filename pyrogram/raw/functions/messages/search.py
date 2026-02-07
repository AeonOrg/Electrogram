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


class Search(TLObject):  # type: ignore
    """Search for messages.


    Details:
        - Layer: ``224``
        - ID: ``29EE847A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            User or chat, histories with which are searched, or (inputPeerEmpty) constructor to search in all private chats and normal groups (not channels) ». Use messages.searchGlobal to search globally in all chats, groups, supergroups and channels.

        q (``str``):
            Text search request

        filter (:obj:`MessagesFilter <pyrogram.raw.base.MessagesFilter>`):
            Filter to return only specified message types

        min_date (``int`` ``32-bit``):
            If a positive value was transferred, only messages with a sending date bigger than the transferred one will be returned

        max_date (``int`` ``32-bit``):
            If a positive value was transferred, only messages with a sending date smaller than the transferred one will be returned

        offset_id (``int`` ``32-bit``):
            Only return messages starting from the specified message ID

        add_offset (``int`` ``32-bit``):
            Additional offset

        limit (``int`` ``32-bit``):
            Number of results to return

        max_id (``int`` ``32-bit``):
            Maximum message ID to return

        min_id (``int`` ``32-bit``):
            Minimum message ID to return

        hash (``int`` ``64-bit``):
            Hash

        from_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Only return messages sent by the specified user ID

        saved_peer_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Search within the saved message dialog » with this ID.

        saved_reaction (List of :obj:`Reaction <pyrogram.raw.base.Reaction>`, *optional*):


        top_msg_id (``int`` ``32-bit``, *optional*):
            Thread ID

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "q", "filter", "min_date", "max_date", "offset_id", "add_offset", "limit", "max_id", "min_id", "hash", "from_id", "saved_peer_id", "saved_reaction", "top_msg_id"]

    ID = 0x29ee847a
    QUALNAME = "functions.messages.Search"

    def __init__(self, *, peer: "raw.base.InputPeer", q: str, filter: "raw.base.MessagesFilter", min_date: int, max_date: int, offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, from_id: "raw.base.InputPeer" = None, saved_peer_id: "raw.base.InputPeer" = None, saved_reaction: Optional[List["raw.base.Reaction"]] = None, top_msg_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.q = q  # string
        self.filter = filter  # MessagesFilter
        self.min_date = min_date  # int
        self.max_date = max_date  # int
        self.offset_id = offset_id  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.hash = hash  # long
        self.from_id = from_id  # flags.0?InputPeer
        self.saved_peer_id = saved_peer_id  # flags.2?InputPeer
        self.saved_reaction = saved_reaction  # flags.3?Vector<Reaction>
        self.top_msg_id = top_msg_id  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Search":

        flags = Int.read(b)

        peer = TLObject.read(b)

        q = String.read(b)

        from_id = TLObject.read(b) if flags & (1 << 0) else None

        saved_peer_id = TLObject.read(b) if flags & (1 << 2) else None

        saved_reaction = TLObject.read(b) if flags & (1 << 3) else []

        top_msg_id = Int.read(b) if flags & (1 << 1) else None
        filter = TLObject.read(b)

        min_date = Int.read(b)

        max_date = Int.read(b)

        offset_id = Int.read(b)

        add_offset = Int.read(b)

        limit = Int.read(b)

        max_id = Int.read(b)

        min_id = Int.read(b)

        hash = Long.read(b)

        return Search(peer=peer, q=q, filter=filter, min_date=min_date, max_date=max_date, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash, from_id=from_id, saved_peer_id=saved_peer_id, saved_reaction=saved_reaction, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.from_id is not None else 0
        flags |= (1 << 2) if self.saved_peer_id is not None else 0
        flags |= (1 << 3) if self.saved_reaction else 0
        flags |= (1 << 1) if self.top_msg_id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(String(self.q))

        if self.from_id is not None:
            b.write(self.from_id.write())

        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())

        if self.saved_reaction is not None:
            b.write(Vector(self.saved_reaction))

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        b.write(self.filter.write())

        b.write(Int(self.min_date))

        b.write(Int(self.max_date))

        b.write(Int(self.offset_id))

        b.write(Int(self.add_offset))

        b.write(Int(self.limit))

        b.write(Int(self.max_id))

        b.write(Int(self.min_id))

        b.write(Long(self.hash))

        return b.getvalue()
