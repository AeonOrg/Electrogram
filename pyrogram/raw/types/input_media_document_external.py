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


class InputMediaDocumentExternal(TLObject):  # type: ignore
    """Document that will be downloaded by the telegram servers

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``779600F9``

    Parameters:
        url (``str``):
            URL of the document

        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Self-destruct time to live of document

        video_cover (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`, *optional*):
            N/A

        video_timestamp (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["url", "spoiler", "ttl_seconds", "video_cover", "video_timestamp"]

    ID = 0x779600f9
    QUALNAME = "types.InputMediaDocumentExternal"

    def __init__(self, *, url: str, spoiler: Optional[bool] = None, ttl_seconds: Optional[int] = None, video_cover: "raw.base.InputPhoto" = None, video_timestamp: Optional[int] = None) -> None:
        self.url = url  # string
        self.spoiler = spoiler  # flags.1?true
        self.ttl_seconds = ttl_seconds  # flags.0?int
        self.video_cover = video_cover  # flags.2?InputPhoto
        self.video_timestamp = video_timestamp  # flags.3?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaDocumentExternal":

        flags = Int.read(b)

        spoiler = True if flags & (1 << 1) else False
        url = String.read(b)

        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        video_cover = TLObject.read(b) if flags & (1 << 2) else None

        video_timestamp = Int.read(b) if flags & (1 << 3) else None
        return InputMediaDocumentExternal(url=url, spoiler=spoiler, ttl_seconds=ttl_seconds, video_cover=video_cover, video_timestamp=video_timestamp)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.spoiler else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        flags |= (1 << 2) if self.video_cover is not None else 0
        flags |= (1 << 3) if self.video_timestamp is not None else 0
        b.write(Int(flags))

        b.write(String(self.url))

        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))

        if self.video_cover is not None:
            b.write(self.video_cover.write())

        if self.video_timestamp is not None:
            b.write(Int(self.video_timestamp))

        return b.getvalue()
