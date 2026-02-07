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


class GetFutureSalts(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B921BD04``

    Parameters:
        num (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`FutureSalts <pyrogram.raw.base.FutureSalts>`
    """

    __slots__: List[str] = ["num"]

    ID = 0xb921bd04
    QUALNAME = "functions.GetFutureSalts"

    def __init__(self, *, num: int) -> None:
        self.num = num  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFutureSalts":
        # No flags

        num = Int.read(b)

        return GetFutureSalts(num=num)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.num))

        return b.getvalue()
