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


class UpdatePinnedDialogs(TLObject):  # type: ignore
    """Pinned dialogs were updated

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``FA0F3CA2``

    Parameters:
        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

        order (List of :obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`, *optional*):
            New order of pinned dialogs

    """

    __slots__: List[str] = ["folder_id", "order"]

    ID = 0xfa0f3ca2
    QUALNAME = "types.UpdatePinnedDialogs"

    def __init__(self, *, folder_id: Optional[int] = None, order: Optional[List["raw.base.DialogPeer"]] = None) -> None:
        self.folder_id = folder_id  # flags.1?int
        self.order = order  # flags.0?Vector<DialogPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedDialogs":

        flags = Int.read(b)

        folder_id = Int.read(b) if flags & (1 << 1) else None
        order = TLObject.read(b) if flags & (1 << 0) else []

        return UpdatePinnedDialogs(folder_id=folder_id, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        flags |= (1 << 0) if self.order else 0
        b.write(Int(flags))

        if self.folder_id is not None:
            b.write(Int(self.folder_id))

        if self.order is not None:
            b.write(Vector(self.order))

        return b.getvalue()
