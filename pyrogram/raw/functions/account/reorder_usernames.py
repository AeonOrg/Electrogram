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


class ReorderUsernames(TLObject):  # type: ignore
    """Reorder usernames associated with the currently logged-in user.


    Details:
        - Layer: ``224``
        - ID: ``EF500EAB``

    Parameters:
        order (List of ``str``):
            The new order for active usernames. All active usernames must be specified.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["order"]

    ID = 0xef500eab
    QUALNAME = "functions.account.ReorderUsernames"

    def __init__(self, *, order: List[str]) -> None:
        self.order = order  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderUsernames":
        # No flags

        order = TLObject.read(b, String)

        return ReorderUsernames(order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.order, String))

        return b.getvalue()
