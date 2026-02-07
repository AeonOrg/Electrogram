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


class GetStarGiftActiveAuctions(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A5D0514D``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`payments.StarGiftActiveAuctions <pyrogram.raw.base.payments.StarGiftActiveAuctions>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xa5d0514d
    QUALNAME = "functions.payments.GetStarGiftActiveAuctions"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarGiftActiveAuctions":
        # No flags

        hash = Long.read(b)

        return GetStarGiftActiveAuctions(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        return b.getvalue()
