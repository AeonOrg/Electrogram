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


class TopPeerCategoryPeers(TLObject):  # type: ignore
    """Top peer category

    Constructor of :obj:`~pyrogram.raw.base.TopPeerCategoryPeers`.

    Details:
        - Layer: ``224``
        - ID: ``FB834291``

    Parameters:
        category (:obj:`TopPeerCategory <pyrogram.raw.base.TopPeerCategory>`):
            Top peer category of peers

        count (``int`` ``32-bit``):
            Count of peers

        peers (List of :obj:`TopPeer <pyrogram.raw.base.TopPeer>`):
            Peers

    """

    __slots__: List[str] = ["category", "count", "peers"]

    ID = 0xfb834291
    QUALNAME = "types.TopPeerCategoryPeers"

    def __init__(self, *, category: "raw.base.TopPeerCategory", count: int, peers: List["raw.base.TopPeer"]) -> None:
        self.category = category  # TopPeerCategory
        self.count = count  # int
        self.peers = peers  # Vector<TopPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeerCategoryPeers":
        # No flags

        category = TLObject.read(b)

        count = Int.read(b)

        peers = TLObject.read(b)

        return TopPeerCategoryPeers(category=category, count=count, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.category.write())

        b.write(Int(self.count))

        b.write(Vector(self.peers))

        return b.getvalue()
