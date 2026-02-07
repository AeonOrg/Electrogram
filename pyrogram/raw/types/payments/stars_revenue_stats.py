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


class StarsRevenueStats(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarsRevenueStats`.

    Details:
        - Layer: ``224``
        - ID: ``6C207376``

    Parameters:
        revenue_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        status (:obj:`StarsRevenueStatus <pyrogram.raw.base.StarsRevenueStatus>`):
            N/A

        usd_rate (``float`` ``64-bit``):
            N/A

        top_hours_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarsRevenueStats
    """

    __slots__: List[str] = ["revenue_graph", "status", "usd_rate", "top_hours_graph"]

    ID = 0x6c207376
    QUALNAME = "types.payments.StarsRevenueStats"

    def __init__(self, *, revenue_graph: "raw.base.StatsGraph", status: "raw.base.StarsRevenueStatus", usd_rate: float, top_hours_graph: "raw.base.StatsGraph" = None) -> None:
        self.revenue_graph = revenue_graph  # StatsGraph
        self.status = status  # StarsRevenueStatus
        self.usd_rate = usd_rate  # double
        self.top_hours_graph = top_hours_graph  # flags.0?StatsGraph

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsRevenueStats":

        flags = Int.read(b)

        top_hours_graph = TLObject.read(b) if flags & (1 << 0) else None

        revenue_graph = TLObject.read(b)

        status = TLObject.read(b)

        usd_rate = Double.read(b)

        return StarsRevenueStats(revenue_graph=revenue_graph, status=status, usd_rate=usd_rate, top_hours_graph=top_hours_graph)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_hours_graph is not None else 0
        b.write(Int(flags))

        if self.top_hours_graph is not None:
            b.write(self.top_hours_graph.write())

        b.write(self.revenue_graph.write())

        b.write(self.status.write())

        b.write(Double(self.usd_rate))

        return b.getvalue()
