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


class PeerLocated(TLObject):  # type: ignore
    """Peer geolocated nearby

    Constructor of :obj:`~pyrogram.raw.base.PeerLocated`.

    Details:
        - Layer: ``224``
        - ID: ``CA461B5D``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer

        expires (``int`` ``32-bit``):
            Validity period of current data

        distance (``int`` ``32-bit``):
            Distance from the peer in meters

    """

    __slots__: List[str] = ["peer", "expires", "distance"]

    ID = 0xca461b5d
    QUALNAME = "types.PeerLocated"

    def __init__(self, *, peer: "raw.base.Peer", expires: int, distance: int) -> None:
        self.peer = peer  # Peer
        self.expires = expires  # int
        self.distance = distance  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerLocated":
        # No flags

        peer = TLObject.read(b)

        expires = Int.read(b)

        distance = Int.read(b)

        return PeerLocated(peer=peer, expires=expires, distance=distance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.expires))

        b.write(Int(self.distance))

        return b.getvalue()
