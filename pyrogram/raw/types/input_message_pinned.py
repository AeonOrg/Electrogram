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


class InputMessagePinned(TLObject):  # type: ignore
    """Pinned message

    Constructor of :obj:`~pyrogram.raw.base.InputMessage`.

    Details:
        - Layer: ``224``
        - ID: ``86872538``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x86872538
    QUALNAME = "types.InputMessagePinned"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessagePinned":
        # No flags

        return InputMessagePinned()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
