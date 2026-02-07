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


class UpdateStarGiftAuctionUserState(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``DC58F31E``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

        user_state (:obj:`StarGiftAuctionUserState <pyrogram.raw.base.StarGiftAuctionUserState>`):
            N/A

    """

    __slots__: List[str] = ["gift_id", "user_state"]

    ID = 0xdc58f31e
    QUALNAME = "types.UpdateStarGiftAuctionUserState"

    def __init__(self, *, gift_id: int, user_state: "raw.base.StarGiftAuctionUserState") -> None:
        self.gift_id = gift_id  # long
        self.user_state = user_state  # StarGiftAuctionUserState

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarGiftAuctionUserState":
        # No flags

        gift_id = Long.read(b)

        user_state = TLObject.read(b)

        return UpdateStarGiftAuctionUserState(gift_id=gift_id, user_state=user_state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.gift_id))

        b.write(self.user_state.write())

        return b.getvalue()
