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


class ReorderQuickReplies(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``60331907``

    Parameters:
        order (List of ``int`` ``32-bit``):


    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order"]

    ID = 0x60331907
    QUALNAME = "functions.messages.ReorderQuickReplies"

    def __init__(self, *, order: List[int]) -> None:
        self.order = order  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderQuickReplies":
        # No flags

        order = TLObject.read(b, Int)

        return ReorderQuickReplies(order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.order, Int))

        return b.getvalue()
