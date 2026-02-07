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


class FinishTakeoutSession(TLObject):  # type: ignore
    """Terminate a takeout session, see here » for more info.


    Details:
        - Layer: ``224``
        - ID: ``1D2652EE``

    Parameters:
        success (``bool``, *optional*):
            Data exported successfully

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["success"]

    ID = 0x1d2652ee
    QUALNAME = "functions.account.FinishTakeoutSession"

    def __init__(self, *, success: Optional[bool] = None) -> None:
        self.success = success  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FinishTakeoutSession":

        flags = Int.read(b)

        success = True if flags & (1 << 0) else False
        return FinishTakeoutSession(success=success)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.success else 0
        b.write(Int(flags))

        return b.getvalue()
