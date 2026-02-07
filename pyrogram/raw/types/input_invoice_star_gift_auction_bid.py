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


class InputInvoiceStarGiftAuctionBid(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``1ECAFA10``

    Parameters:
        gift_id (``int`` ``64-bit``):
            N/A

        bid_amount (``int`` ``64-bit``):
            N/A

        hide_name (``bool``, *optional*):
            N/A

        update_bid (``bool``, *optional*):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["gift_id", "bid_amount", "hide_name", "update_bid", "peer", "message"]

    ID = 0x1ecafa10
    QUALNAME = "types.InputInvoiceStarGiftAuctionBid"

    def __init__(self, *, gift_id: int, bid_amount: int, hide_name: Optional[bool] = None, update_bid: Optional[bool] = None, peer: "raw.base.InputPeer" = None, message: "raw.base.TextWithEntities" = None) -> None:
        self.gift_id = gift_id  # long
        self.bid_amount = bid_amount  # long
        self.hide_name = hide_name  # flags.0?true
        self.update_bid = update_bid  # flags.2?true
        self.peer = peer  # flags.3?InputPeer
        self.message = message  # flags.1?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftAuctionBid":

        flags = Int.read(b)

        hide_name = True if flags & (1 << 0) else False
        update_bid = True if flags & (1 << 2) else False
        peer = TLObject.read(b) if flags & (1 << 3) else None

        gift_id = Long.read(b)

        bid_amount = Long.read(b)

        message = TLObject.read(b) if flags & (1 << 1) else None

        return InputInvoiceStarGiftAuctionBid(gift_id=gift_id, bid_amount=bid_amount, hide_name=hide_name, update_bid=update_bid, peer=peer, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.hide_name else 0
        flags |= (1 << 2) if self.update_bid else 0
        flags |= (1 << 3) if self.peer is not None else 0
        flags |= (1 << 1) if self.message is not None else 0
        b.write(Int(flags))

        if self.peer is not None:
            b.write(self.peer.write())

        b.write(Long(self.gift_id))

        b.write(Long(self.bid_amount))

        if self.message is not None:
            b.write(self.message.write())

        return b.getvalue()
