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


class UpdateDialogFiltersOrder(TLObject):  # type: ignore
    """Reorder folders


    Details:
        - Layer: ``224``
        - ID: ``C563C1E4``

    Parameters:
        order (List of ``int`` ``32-bit``):
            New folder order

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order"]

    ID = 0xc563c1e4
    QUALNAME = "functions.messages.UpdateDialogFiltersOrder"

    def __init__(self, *, order: List[int]) -> None:
        self.order = order  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDialogFiltersOrder":
        # No flags

        order = TLObject.read(b, Int)

        return UpdateDialogFiltersOrder(order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.order, Int))

        return b.getvalue()
