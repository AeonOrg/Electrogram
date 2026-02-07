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


class ApplyBoost(TLObject):  # type: ignore
    """Apply one or more boosts » to a peer.


    Details:
        - Layer: ``224``
        - ID: ``6B7DA746``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The peer to boost.

        slots (List of ``int`` ``32-bit``, *optional*):
            Which boost slots to assign to this peer.

    Returns:
        :obj:`premium.MyBoosts <pyrogram.raw.base.premium.MyBoosts>`
    """

    __slots__: List[str] = ["peer", "slots"]

    ID = 0x6b7da746
    QUALNAME = "functions.premium.ApplyBoost"

    def __init__(self, *, peer: "raw.base.InputPeer", slots: Optional[List[int]] = None) -> None:
        self.peer = peer  # InputPeer
        self.slots = slots  # flags.0?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ApplyBoost":

        flags = Int.read(b)

        slots = TLObject.read(b, Int) if flags & (1 << 0) else []

        peer = TLObject.read(b)

        return ApplyBoost(peer=peer, slots=slots)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.slots else 0
        b.write(Int(flags))

        if self.slots is not None:
            b.write(Vector(self.slots, Int))

        b.write(self.peer.write())

        return b.getvalue()
