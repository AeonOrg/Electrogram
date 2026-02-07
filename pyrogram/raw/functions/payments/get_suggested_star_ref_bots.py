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


class GetSuggestedStarRefBots(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D6B48F7``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        order_by_revenue (``bool``, *optional*):
            N/A

        order_by_date (``bool``, *optional*):
            N/A

    Returns:
        :obj:`payments.SuggestedStarRefBots <pyrogram.raw.base.payments.SuggestedStarRefBots>`
    """

    __slots__: List[str] = ["peer", "offset", "limit", "order_by_revenue", "order_by_date"]

    ID = 0xd6b48f7
    QUALNAME = "functions.payments.GetSuggestedStarRefBots"

    def __init__(self, *, peer: "raw.base.InputPeer", offset: str, limit: int, order_by_revenue: Optional[bool] = None, order_by_date: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset = offset  # string
        self.limit = limit  # int
        self.order_by_revenue = order_by_revenue  # flags.0?true
        self.order_by_date = order_by_date  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSuggestedStarRefBots":

        flags = Int.read(b)

        order_by_revenue = True if flags & (1 << 0) else False
        order_by_date = True if flags & (1 << 1) else False
        peer = TLObject.read(b)

        offset = String.read(b)

        limit = Int.read(b)

        return GetSuggestedStarRefBots(peer=peer, offset=offset, limit=limit, order_by_revenue=order_by_revenue, order_by_date=order_by_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.order_by_revenue else 0
        flags |= (1 << 1) if self.order_by_date else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
