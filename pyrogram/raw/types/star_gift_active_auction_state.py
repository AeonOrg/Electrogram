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


class StarGiftActiveAuctionState(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarGiftActiveAuctionState`.

    Details:
        - Layer: ``224``
        - ID: ``D31BC45D``

    Parameters:
        gift (:obj:`StarGift <pyrogram.raw.base.StarGift>`):
            N/A

        state (:obj:`StarGiftAuctionState <pyrogram.raw.base.StarGiftAuctionState>`):
            N/A

        user_state (:obj:`StarGiftAuctionUserState <pyrogram.raw.base.StarGiftAuctionUserState>`):
            N/A

    """

    __slots__: List[str] = ["gift", "state", "user_state"]

    ID = 0xd31bc45d
    QUALNAME = "types.StarGiftActiveAuctionState"

    def __init__(self, *, gift: "raw.base.StarGift", state: "raw.base.StarGiftAuctionState", user_state: "raw.base.StarGiftAuctionUserState") -> None:
        self.gift = gift  # StarGift
        self.state = state  # StarGiftAuctionState
        self.user_state = user_state  # StarGiftAuctionUserState

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftActiveAuctionState":
        # No flags

        gift = TLObject.read(b)

        state = TLObject.read(b)

        user_state = TLObject.read(b)

        return StarGiftActiveAuctionState(gift=gift, state=state, user_state=user_state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.gift.write())

        b.write(self.state.write())

        b.write(self.user_state.write())

        return b.getvalue()
