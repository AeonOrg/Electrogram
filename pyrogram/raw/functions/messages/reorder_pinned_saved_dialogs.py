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


class ReorderPinnedSavedDialogs(TLObject):  # type: ignore
    """Reorder pinned saved message dialogs ».


    Details:
        - Layer: ``224``
        - ID: ``8B716587``

    Parameters:
        order (List of :obj:`InputDialogPeer <pyrogram.raw.base.InputDialogPeer>`):
            New dialog order

        force (``bool``, *optional*):
            If set, dialogs pinned server-side but not present in the order field will be unpinned.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order", "force"]

    ID = 0x8b716587
    QUALNAME = "functions.messages.ReorderPinnedSavedDialogs"

    def __init__(self, *, order: List["raw.base.InputDialogPeer"], force: Optional[bool] = None) -> None:
        self.order = order  # Vector<InputDialogPeer>
        self.force = force  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderPinnedSavedDialogs":

        flags = Int.read(b)

        force = True if flags & (1 << 0) else False
        order = TLObject.read(b)

        return ReorderPinnedSavedDialogs(order=order, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force else 0
        b.write(Int(flags))

        b.write(Vector(self.order))

        return b.getvalue()
