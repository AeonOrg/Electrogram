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


class RpcError(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RpcError`.

    Details:
        - Layer: ``224``
        - ID: ``2144CA19``

    Parameters:
        error_code (``int`` ``32-bit``):
            N/A

        error_message (``str``):
            N/A

    """

    __slots__: List[str] = ["error_code", "error_message"]

    ID = 0x2144ca19
    QUALNAME = "types.RpcError"

    def __init__(self, *, error_code: int, error_message: str) -> None:
        self.error_code = error_code  # int
        self.error_message = error_message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcError":
        # No flags

        error_code = Int.read(b)

        error_message = String.read(b)

        return RpcError(error_code=error_code, error_message=error_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.error_code))

        b.write(String(self.error_message))

        return b.getvalue()
