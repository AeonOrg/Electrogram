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


class MessageExtendedMediaPreview(TLObject):  # type: ignore
    """Extended media preview

    Constructor of :obj:`~pyrogram.raw.base.MessageExtendedMedia`.

    Details:
        - Layer: ``224``
        - ID: ``AD628CC8``

    Parameters:
        w (``int`` ``32-bit``, *optional*):
            Width

        h (``int`` ``32-bit``, *optional*):
            Height

        thumb (:obj:`PhotoSize <pyrogram.raw.base.PhotoSize>`, *optional*):
            Thumbnail

        video_duration (``int`` ``32-bit``, *optional*):
            Video duration

    """

    __slots__: List[str] = ["w", "h", "thumb", "video_duration"]

    ID = 0xad628cc8
    QUALNAME = "types.MessageExtendedMediaPreview"

    def __init__(self, *, w: Optional[int] = None, h: Optional[int] = None, thumb: "raw.base.PhotoSize" = None, video_duration: Optional[int] = None) -> None:
        self.w = w  # flags.0?int
        self.h = h  # flags.0?int
        self.thumb = thumb  # flags.1?PhotoSize
        self.video_duration = video_duration  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageExtendedMediaPreview":

        flags = Int.read(b)

        w = Int.read(b) if flags & (1 << 0) else None
        h = Int.read(b) if flags & (1 << 0) else None
        thumb = TLObject.read(b) if flags & (1 << 1) else None

        video_duration = Int.read(b) if flags & (1 << 2) else None
        return MessageExtendedMediaPreview(w=w, h=h, thumb=thumb, video_duration=video_duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.w is not None else 0
        flags |= (1 << 0) if self.h is not None else 0
        flags |= (1 << 1) if self.thumb is not None else 0
        flags |= (1 << 2) if self.video_duration is not None else 0
        b.write(Int(flags))

        if self.w is not None:
            b.write(Int(self.w))

        if self.h is not None:
            b.write(Int(self.h))

        if self.thumb is not None:
            b.write(self.thumb.write())

        if self.video_duration is not None:
            b.write(Int(self.video_duration))

        return b.getvalue()
