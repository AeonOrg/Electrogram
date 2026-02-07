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


class InputUserSelf(TLObject):  # type: ignore
    """Defines the current user.

    Constructor of :obj:`~pyrogram.raw.base.InputUser`.

    Details:
        - Layer: ``224``
        - ID: ``F7C1B13F``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xf7c1b13f
    QUALNAME = "types.InputUserSelf"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputUserSelf":
        # No flags

        return InputUserSelf()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
