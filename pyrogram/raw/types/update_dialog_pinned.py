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


class UpdateDialogPinned(TLObject):  # type: ignore
    """A dialog was pinned/unpinned

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``6E6FE51C``

    Parameters:
        peer (:obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`):
            The dialog

        pinned (``bool``, *optional*):
            Whether the dialog was pinned

        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

    """

    __slots__: List[str] = ["peer", "pinned", "folder_id"]

    ID = 0x6e6fe51c
    QUALNAME = "types.UpdateDialogPinned"

    def __init__(self, *, peer: "raw.base.DialogPeer", pinned: Optional[bool] = None, folder_id: Optional[int] = None) -> None:
        self.peer = peer  # DialogPeer
        self.pinned = pinned  # flags.0?true
        self.folder_id = folder_id  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDialogPinned":

        flags = Int.read(b)

        pinned = True if flags & (1 << 0) else False
        folder_id = Int.read(b) if flags & (1 << 1) else None
        peer = TLObject.read(b)

        return UpdateDialogPinned(peer=peer, pinned=pinned, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned else 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        b.write(Int(flags))

        if self.folder_id is not None:
            b.write(Int(self.folder_id))

        b.write(self.peer.write())

        return b.getvalue()
