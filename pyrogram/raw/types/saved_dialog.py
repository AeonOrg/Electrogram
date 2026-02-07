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


class SavedDialog(TLObject):  # type: ignore
    """Represents a saved dialog ».

    Constructor of :obj:`~pyrogram.raw.base.SavedDialog`.

    Details:
        - Layer: ``224``
        - ID: ``BD87CB6C``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            The dialog

        top_message (``int`` ``32-bit``):
            The latest message ID

        pinned (``bool``, *optional*):
            Is the dialog pinned

    """

    __slots__: List[str] = ["peer", "top_message", "pinned"]

    ID = 0xbd87cb6c
    QUALNAME = "types.SavedDialog"

    def __init__(self, *, peer: "raw.base.Peer", top_message: int, pinned: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.top_message = top_message  # int
        self.pinned = pinned  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedDialog":

        flags = Int.read(b)

        pinned = True if flags & (1 << 2) else False
        peer = TLObject.read(b)

        top_message = Int.read(b)

        return SavedDialog(peer=peer, top_message=top_message, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.top_message))

        return b.getvalue()
