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


class SearchPosts(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D1810907``

    Parameters:
        offset (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hashtag (``str``, *optional*):
            N/A

        area (:obj:`MediaArea <pyrogram.raw.base.MediaArea>`, *optional*):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`stories.FoundStories <pyrogram.raw.base.stories.FoundStories>`
    """

    __slots__: List[str] = ["offset", "limit", "hashtag", "area", "peer"]

    ID = 0xd1810907
    QUALNAME = "functions.stories.SearchPosts"

    def __init__(self, *, offset: str, limit: int, hashtag: Optional[str] = None, area: "raw.base.MediaArea" = None, peer: "raw.base.InputPeer" = None) -> None:
        self.offset = offset  # string
        self.limit = limit  # int
        self.hashtag = hashtag  # flags.0?string
        self.area = area  # flags.1?MediaArea
        self.peer = peer  # flags.2?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchPosts":

        flags = Int.read(b)

        hashtag = String.read(b) if flags & (1 << 0) else None
        area = TLObject.read(b) if flags & (1 << 1) else None

        peer = TLObject.read(b) if flags & (1 << 2) else None

        offset = String.read(b)

        limit = Int.read(b)

        return SearchPosts(offset=offset, limit=limit, hashtag=hashtag, area=area, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.hashtag is not None else 0
        flags |= (1 << 1) if self.area is not None else 0
        flags |= (1 << 2) if self.peer is not None else 0
        b.write(Int(flags))

        if self.hashtag is not None:
            b.write(String(self.hashtag))

        if self.area is not None:
            b.write(self.area.write())

        if self.peer is not None:
            b.write(self.peer.write())

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
