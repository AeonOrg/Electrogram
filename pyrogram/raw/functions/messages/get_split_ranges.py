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


class GetSplitRanges(TLObject):  # type: ignore
    """Get message ranges for saving the user's chat history


    Details:
        - Layer: ``224``
        - ID: ``1CFF7E08``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`MessageRange <pyrogram.raw.base.MessageRange>`
    """

    __slots__: List[str] = []

    ID = 0x1cff7e08
    QUALNAME = "functions.messages.GetSplitRanges"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSplitRanges":
        # No flags

        return GetSplitRanges()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
