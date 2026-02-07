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


class UpdateChannelWebPage(TLObject):  # type: ignore
    """A webpage preview of a link in a channel/supergroup message was generated

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``2F2BA99F``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel/supergroup ID

        webpage (:obj:`WebPage <pyrogram.raw.base.WebPage>`):
            Generated webpage preview

        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

    """

    __slots__: List[str] = ["channel_id", "webpage", "pts", "pts_count"]

    ID = 0x2f2ba99f
    QUALNAME = "types.UpdateChannelWebPage"

    def __init__(self, *, channel_id: int, webpage: "raw.base.WebPage", pts: int, pts_count: int) -> None:
        self.channel_id = channel_id  # long
        self.webpage = webpage  # WebPage
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelWebPage":
        # No flags

        channel_id = Long.read(b)

        webpage = TLObject.read(b)

        pts = Int.read(b)

        pts_count = Int.read(b)

        return UpdateChannelWebPage(channel_id=channel_id, webpage=webpage, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(self.webpage.write())

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        return b.getvalue()
