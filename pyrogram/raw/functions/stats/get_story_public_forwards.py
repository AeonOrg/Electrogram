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


class GetStoryPublicForwards(TLObject):  # type: ignore
    """Obtain forwards of a story as a message to public chats and reposts by public channels.


    Details:
        - Layer: ``224``
        - ID: ``A6437EF6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer where the story was originally posted

        id (``int`` ``32-bit``):
            Story ID

        offset (``str``):
            Offset for pagination, from stats.PublicForwards.next_offset.

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

    Returns:
        :obj:`stats.PublicForwards <pyrogram.raw.base.stats.PublicForwards>`
    """

    __slots__: List[str] = ["peer", "id", "offset", "limit"]

    ID = 0xa6437ef6
    QUALNAME = "functions.stats.GetStoryPublicForwards"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, offset: str, limit: int) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.offset = offset  # string
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryPublicForwards":
        # No flags

        peer = TLObject.read(b)

        id = Int.read(b)

        offset = String.read(b)

        limit = Int.read(b)

        return GetStoryPublicForwards(peer=peer, id=id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.id))

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
