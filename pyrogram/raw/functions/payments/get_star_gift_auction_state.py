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


class GetStarGiftAuctionState(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5C9FF4D6``

    Parameters:
        auction (:obj:`InputStarGiftAuction <pyrogram.raw.base.InputStarGiftAuction>`):
            N/A

        version (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`payments.StarGiftAuctionState <pyrogram.raw.base.payments.StarGiftAuctionState>`
    """

    __slots__: List[str] = ["auction", "version"]

    ID = 0x5c9ff4d6
    QUALNAME = "functions.payments.GetStarGiftAuctionState"

    def __init__(self, *, auction: "raw.base.InputStarGiftAuction", version: int) -> None:
        self.auction = auction  # InputStarGiftAuction
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarGiftAuctionState":
        # No flags

        auction = TLObject.read(b)

        version = Int.read(b)

        return GetStarGiftAuctionState(auction=auction, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.auction.write())

        b.write(Int(self.version))

        return b.getvalue()
