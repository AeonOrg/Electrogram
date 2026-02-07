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


class StoryStats(TLObject):  # type: ignore
    """Contains statistics about a story.

    Constructor of :obj:`~pyrogram.raw.base.stats.StoryStats`.

    Details:
        - Layer: ``224``
        - ID: ``50CD067C``

    Parameters:
        views_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            A graph containing the number of story views and shares

        reactions_by_emotion_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            A bar graph containing the number of story reactions categorized by "emotion" (i.e. Positive, Negative, Other, etc...)

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetStoryStats
    """

    __slots__: List[str] = ["views_graph", "reactions_by_emotion_graph"]

    ID = 0x50cd067c
    QUALNAME = "types.stats.StoryStats"

    def __init__(self, *, views_graph: "raw.base.StatsGraph", reactions_by_emotion_graph: "raw.base.StatsGraph") -> None:
        self.views_graph = views_graph  # StatsGraph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph  # StatsGraph

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryStats":
        # No flags

        views_graph = TLObject.read(b)

        reactions_by_emotion_graph = TLObject.read(b)

        return StoryStats(views_graph=views_graph, reactions_by_emotion_graph=reactions_by_emotion_graph)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.views_graph.write())

        b.write(self.reactions_by_emotion_graph.write())

        return b.getvalue()
