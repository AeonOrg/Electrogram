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


class StarsTonAmount(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsAmount`.

    Details:
        - Layer: ``224``
        - ID: ``74AEE3E0``

    Parameters:
        amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["amount"]

    ID = 0x74aee3e0
    QUALNAME = "types.StarsTonAmount"

    def __init__(self, *, amount: int) -> None:
        self.amount = amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTonAmount":
        # No flags

        amount = Long.read(b)

        return StarsTonAmount(amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.amount))

        return b.getvalue()
