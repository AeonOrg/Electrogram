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


class AutoSaveSettings(TLObject):  # type: ignore
    """Media autosave settings

    Constructor of :obj:`~pyrogram.raw.base.AutoSaveSettings`.

    Details:
        - Layer: ``224``
        - ID: ``C84834CE``

    Parameters:
        photos (``bool``, *optional*):
            Whether photos should be autosaved to the gallery.

        videos (``bool``, *optional*):
            Whether videos should be autosaved to the gallery.

        video_max_size (``int`` ``64-bit``, *optional*):
            If set, specifies a size limit for autosavable videos

    """

    __slots__: List[str] = ["photos", "videos", "video_max_size"]

    ID = 0xc84834ce
    QUALNAME = "types.AutoSaveSettings"

    def __init__(self, *, photos: Optional[bool] = None, videos: Optional[bool] = None, video_max_size: Optional[int] = None) -> None:
        self.photos = photos  # flags.0?true
        self.videos = videos  # flags.1?true
        self.video_max_size = video_max_size  # flags.2?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoSaveSettings":

        flags = Int.read(b)

        photos = True if flags & (1 << 0) else False
        videos = True if flags & (1 << 1) else False
        video_max_size = Long.read(b) if flags & (1 << 2) else None
        return AutoSaveSettings(photos=photos, videos=videos, video_max_size=video_max_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photos else 0
        flags |= (1 << 1) if self.videos else 0
        flags |= (1 << 2) if self.video_max_size is not None else 0
        b.write(Int(flags))

        if self.video_max_size is not None:
            b.write(Long(self.video_max_size))

        return b.getvalue()
