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


class UpdatePinnedSavedDialogs(TLObject):  # type: ignore
    """Pinned saved dialogs » were updated

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``686C85A6``

    Parameters:
        order (List of :obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`, *optional*):
            New order of pinned saved dialogs

    """

    __slots__: List[str] = ["order"]

    ID = 0x686c85a6
    QUALNAME = "types.UpdatePinnedSavedDialogs"

    def __init__(self, *, order: Optional[List["raw.base.DialogPeer"]] = None) -> None:
        self.order = order  # flags.0?Vector<DialogPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedSavedDialogs":

        flags = Int.read(b)

        order = TLObject.read(b) if flags & (1 << 0) else []

        return UpdatePinnedSavedDialogs(order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.order else 0
        b.write(Int(flags))

        if self.order is not None:
            b.write(Vector(self.order))

        return b.getvalue()
