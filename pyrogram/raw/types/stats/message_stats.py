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


class MessageStats(TLObject):  # type: ignore
    """Message statistics

    Constructor of :obj:`~pyrogram.raw.base.stats.MessageStats`.

    Details:
        - Layer: ``224``
        - ID: ``7FE91C14``

    Parameters:
        views_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            Message view graph

        reactions_by_emotion_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            A graph containing the number of reactions on stories categorized by emotion

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetMessageStats
    """

    __slots__: List[str] = ["views_graph", "reactions_by_emotion_graph"]

    ID = 0x7fe91c14
    QUALNAME = "types.stats.MessageStats"

    def __init__(self, *, views_graph: "raw.base.StatsGraph", reactions_by_emotion_graph: "raw.base.StatsGraph") -> None:
        self.views_graph = views_graph  # StatsGraph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph  # StatsGraph

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageStats":
        # No flags

        views_graph = TLObject.read(b)

        reactions_by_emotion_graph = TLObject.read(b)

        return MessageStats(views_graph=views_graph, reactions_by_emotion_graph=reactions_by_emotion_graph)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.views_graph.write())

        b.write(self.reactions_by_emotion_graph.write())

        return b.getvalue()
