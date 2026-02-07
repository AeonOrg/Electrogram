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


class VideoSize(TLObject):  # type: ignore
    """An animated profile picture in MPEG4 format

    Constructor of :obj:`~pyrogram.raw.base.VideoSize`.

    Details:
        - Layer: ``224``
        - ID: ``DE33B094``

    Parameters:
        type (``str``):
            u for animated profile pictures, and v for trimmed and downscaled video previews

        w (``int`` ``32-bit``):
            Video width

        h (``int`` ``32-bit``):
            Video height

        size (``int`` ``32-bit``):
            File size

        video_start_ts (``float`` ``64-bit``, *optional*):
            Timestamp that should be shown as static preview to the user (seconds)

    """

    __slots__: List[str] = ["type", "w", "h", "size", "video_start_ts"]

    ID = 0xde33b094
    QUALNAME = "types.VideoSize"

    def __init__(self, *, type: str, w: int, h: int, size: int, video_start_ts: Optional[float] = None) -> None:
        self.type = type  # string
        self.w = w  # int
        self.h = h  # int
        self.size = size  # int
        self.video_start_ts = video_start_ts  # flags.0?double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VideoSize":

        flags = Int.read(b)

        type = String.read(b)

        w = Int.read(b)

        h = Int.read(b)

        size = Int.read(b)

        video_start_ts = Double.read(b) if flags & (1 << 0) else None
        return VideoSize(type=type, w=w, h=h, size=size, video_start_ts=video_start_ts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video_start_ts is not None else 0
        b.write(Int(flags))

        b.write(String(self.type))

        b.write(Int(self.w))

        b.write(Int(self.h))

        b.write(Int(self.size))

        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))

        return b.getvalue()
