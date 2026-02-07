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


class GetStarGiftUpgradePreview(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9C9ABCB1``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`payments.StarGiftUpgradePreview <pyrogram.raw.base.payments.StarGiftUpgradePreview>`
    """

    __slots__: List[str] = ["gift_id"]

    ID = 0x9c9abcb1
    QUALNAME = "functions.payments.GetStarGiftUpgradePreview"

    def __init__(self, *, gift_id: int) -> None:
        self.gift_id = gift_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarGiftUpgradePreview":
        # No flags

        gift_id = Long.read(b)

        return GetStarGiftUpgradePreview(gift_id=gift_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.gift_id))

        return b.getvalue()
