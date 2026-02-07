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


class StarsAmount(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsAmount`.

    Details:
        - Layer: ``224``
        - ID: ``BBB6B4A3``

    Parameters:
        amount (``int`` ``64-bit``):
            N/A

        nanos (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["amount", "nanos"]

    ID = 0xbbb6b4a3
    QUALNAME = "types.StarsAmount"

    def __init__(self, *, amount: int, nanos: int) -> None:
        self.amount = amount  # long
        self.nanos = nanos  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsAmount":
        # No flags

        amount = Long.read(b)

        nanos = Int.read(b)

        return StarsAmount(amount=amount, nanos=nanos)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.amount))

        b.write(Int(self.nanos))

        return b.getvalue()
