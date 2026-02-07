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


class UpdateReadStories(TLObject):  # type: ignore
    """Stories of a specific peer were marked as read.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F74E932B``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The peer

        max_id (``int`` ``32-bit``):
            ID of the last story that was marked as read

    """

    __slots__: List[str] = ["peer", "max_id"]

    ID = 0xf74e932b
    QUALNAME = "types.UpdateReadStories"

    def __init__(self, *, peer: "raw.base.Peer", max_id: int) -> None:
        self.peer = peer  # Peer
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadStories":
        # No flags

        peer = TLObject.read(b)

        max_id = Int.read(b)

        return UpdateReadStories(peer=peer, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.max_id))

        return b.getvalue()
