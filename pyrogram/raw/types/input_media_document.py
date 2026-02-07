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


class InputMediaDocument(TLObject):  # type: ignore
    """Forwarded document

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``A8763AB5``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            The document to be forwarded.

        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        video_cover (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`, *optional*):
            N/A

        video_timestamp (``int`` ``32-bit``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Time to live of self-destructing document

        query (``str``, *optional*):
            Text query or emoji that was used by the user to find this sticker or GIF: used to improve search result relevance.

    """

    __slots__: List[str] = ["id", "spoiler", "video_cover", "video_timestamp", "ttl_seconds", "query"]

    ID = 0xa8763ab5
    QUALNAME = "types.InputMediaDocument"

    def __init__(self, *, id: "raw.base.InputDocument", spoiler: Optional[bool] = None, video_cover: "raw.base.InputPhoto" = None, video_timestamp: Optional[int] = None, ttl_seconds: Optional[int] = None, query: Optional[str] = None) -> None:
        self.id = id  # InputDocument
        self.spoiler = spoiler  # flags.2?true
        self.video_cover = video_cover  # flags.3?InputPhoto
        self.video_timestamp = video_timestamp  # flags.4?int
        self.ttl_seconds = ttl_seconds  # flags.0?int
        self.query = query  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaDocument":

        flags = Int.read(b)

        spoiler = True if flags & (1 << 2) else False
        id = TLObject.read(b)

        video_cover = TLObject.read(b) if flags & (1 << 3) else None

        video_timestamp = Int.read(b) if flags & (1 << 4) else None
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        query = String.read(b) if flags & (1 << 1) else None
        return InputMediaDocument(id=id, spoiler=spoiler, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.spoiler else 0
        flags |= (1 << 3) if self.video_cover is not None else 0
        flags |= (1 << 4) if self.video_timestamp is not None else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        flags |= (1 << 1) if self.query is not None else 0
        b.write(Int(flags))

        b.write(self.id.write())

        if self.video_cover is not None:
            b.write(self.video_cover.write())

        if self.video_timestamp is not None:
            b.write(Int(self.video_timestamp))

        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))

        if self.query is not None:
            b.write(String(self.query))

        return b.getvalue()
