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


class ReorderStarGiftCollections(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C32AF4CC``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        order (List of ``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "order"]

    ID = 0xc32af4cc
    QUALNAME = "functions.payments.ReorderStarGiftCollections"

    def __init__(self, *, peer: "raw.base.InputPeer", order: List[int]) -> None:
        self.peer = peer  # InputPeer
        self.order = order  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderStarGiftCollections":
        # No flags

        peer = TLObject.read(b)

        order = TLObject.read(b, Int)

        return ReorderStarGiftCollections(peer=peer, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Vector(self.order, Int))

        return b.getvalue()
