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


class GetCraftStarGifts(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FD05DD00``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`payments.SavedStarGifts <pyrogram.raw.base.payments.SavedStarGifts>`
    """

    __slots__: List[str] = ["gift_id", "offset", "limit"]

    ID = 0xfd05dd00
    QUALNAME = "functions.messages.GetCraftStarGifts"

    def __init__(self, *, gift_id: int, offset: str, limit: int) -> None:
        self.gift_id = gift_id  # long
        self.offset = offset  # string
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCraftStarGifts":
        # No flags

        gift_id = Long.read(b)

        offset = String.read(b)

        limit = Int.read(b)

        return GetCraftStarGifts(gift_id=gift_id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.gift_id))

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
