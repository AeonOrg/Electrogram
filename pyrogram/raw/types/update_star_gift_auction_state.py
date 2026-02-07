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


class UpdateStarGiftAuctionState(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``48E246C2``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

        state (:obj:`StarGiftAuctionState <pyrogram.raw.base.StarGiftAuctionState>`):
            N/A

    """

    __slots__: List[str] = ["gift_id", "state"]

    ID = 0x48e246c2
    QUALNAME = "types.UpdateStarGiftAuctionState"

    def __init__(self, *, gift_id: int, state: "raw.base.StarGiftAuctionState") -> None:
        self.gift_id = gift_id  # long
        self.state = state  # StarGiftAuctionState

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarGiftAuctionState":
        # No flags

        gift_id = Long.read(b)

        state = TLObject.read(b)

        return UpdateStarGiftAuctionState(gift_id=gift_id, state=state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.gift_id))

        b.write(self.state.write())

        return b.getvalue()
