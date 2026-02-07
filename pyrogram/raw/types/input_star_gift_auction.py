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


class InputStarGiftAuction(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStarGiftAuction`.

    Details:
        - Layer: ``224``
        - ID: ``2E16C98``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["gift_id"]

    ID = 0x2e16c98
    QUALNAME = "types.InputStarGiftAuction"

    def __init__(self, *, gift_id: int) -> None:
        self.gift_id = gift_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStarGiftAuction":
        # No flags

        gift_id = Long.read(b)

        return InputStarGiftAuction(gift_id=gift_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.gift_id))

        return b.getvalue()
