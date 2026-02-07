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


class UpdatePinnedForumTopics(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``DEF143D0``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        order (List of ``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "order"]

    ID = 0xdef143d0
    QUALNAME = "types.UpdatePinnedForumTopics"

    def __init__(self, *, peer: "raw.base.Peer", order: Optional[List[int]] = None) -> None:
        self.peer = peer  # Peer
        self.order = order  # flags.0?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedForumTopics":

        flags = Int.read(b)

        peer = TLObject.read(b)

        order = TLObject.read(b, Int) if flags & (1 << 0) else []

        return UpdatePinnedForumTopics(peer=peer, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.order else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.order is not None:
            b.write(Vector(self.order, Int))

        return b.getvalue()
