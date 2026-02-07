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


class ReqPqMulti(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BE7E8EF1``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

    Returns:
        :obj:`ResPQ <pyrogram.raw.base.ResPQ>`
    """

    __slots__: List[str] = ["nonce"]

    ID = 0xbe7e8ef1
    QUALNAME = "functions.ReqPqMulti"

    def __init__(self, *, nonce: int) -> None:
        self.nonce = nonce  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReqPqMulti":
        # No flags

        nonce = Int128.read(b)

        return ReqPqMulti(nonce=nonce)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int128(self.nonce))

        return b.getvalue()
