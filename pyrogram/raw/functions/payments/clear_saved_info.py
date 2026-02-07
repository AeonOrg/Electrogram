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


class ClearSavedInfo(TLObject):  # type: ignore
    """Clear saved payment information


    Details:
        - Layer: ``224``
        - ID: ``D83D70C1``

    Parameters:
        credentials (``bool``, *optional*):
            Remove saved payment credentials

        info (``bool``, *optional*):
            Clear the last order settings saved by the user

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["credentials", "info"]

    ID = 0xd83d70c1
    QUALNAME = "functions.payments.ClearSavedInfo"

    def __init__(self, *, credentials: Optional[bool] = None, info: Optional[bool] = None) -> None:
        self.credentials = credentials  # flags.0?true
        self.info = info  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ClearSavedInfo":

        flags = Int.read(b)

        credentials = True if flags & (1 << 0) else False
        info = True if flags & (1 << 1) else False
        return ClearSavedInfo(credentials=credentials, info=info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.credentials else 0
        flags |= (1 << 1) if self.info else 0
        b.write(Int(flags))

        return b.getvalue()
