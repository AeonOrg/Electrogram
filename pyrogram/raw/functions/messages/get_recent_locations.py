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


class GetRecentLocations(TLObject):  # type: ignore
    """Get live location history of a certain user


    Details:
        - Layer: ``224``
        - ID: ``702A40E0``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            User

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "limit", "hash"]

    ID = 0x702a40e0
    QUALNAME = "functions.messages.GetRecentLocations"

    def __init__(self, *, peer: "raw.base.InputPeer", limit: int, hash: int) -> None:
        self.peer = peer  # InputPeer
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentLocations":
        # No flags

        peer = TLObject.read(b)

        limit = Int.read(b)

        hash = Long.read(b)

        return GetRecentLocations(peer=peer, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.limit))

        b.write(Long(self.hash))

        return b.getvalue()
