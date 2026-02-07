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


class AutoDownloadSettings(TLObject):  # type: ignore
    """Autodownload settings

    Constructor of :obj:`~pyrogram.raw.base.AutoDownloadSettings`.

    Details:
        - Layer: ``224``
        - ID: ``BAA57628``

    Parameters:
        photo_size_max (``int`` ``32-bit``):
            Maximum size of photos to preload

        video_size_max (``int`` ``64-bit``):
            Maximum size of videos to preload

        file_size_max (``int`` ``64-bit``):
            Maximum size of other files to preload

        video_upload_maxbitrate (``int`` ``32-bit``):
            Maximum suggested bitrate for uploading videos

        small_queue_active_operations_max (``int`` ``32-bit``):
            A limit, specifying the maximum number of files that should be downloaded in parallel from the same DC, for files smaller than 20MB.

        large_queue_active_operations_max (``int`` ``32-bit``):
            A limit, specifying the maximum number of files that should be downloaded in parallel from the same DC, for files bigger than 20MB.

        disabled (``bool``, *optional*):
            Disable automatic media downloads?

        video_preload_large (``bool``, *optional*):
            Whether to preload the first seconds of videos larger than the specified limit

        audio_preload_next (``bool``, *optional*):
            Whether to preload the next audio track when you're listening to music

        phonecalls_less_data (``bool``, *optional*):
            Whether to enable data saving mode in phone calls

        stories_preload (``bool``, *optional*):
            Whether to preload stories; in particular, the first documentAttributeVideo.preload_prefix_size bytes of story videos should be preloaded.

    """

    __slots__: List[str] = ["photo_size_max", "video_size_max", "file_size_max", "video_upload_maxbitrate", "small_queue_active_operations_max", "large_queue_active_operations_max", "disabled", "video_preload_large", "audio_preload_next", "phonecalls_less_data", "stories_preload"]

    ID = 0xbaa57628
    QUALNAME = "types.AutoDownloadSettings"

    def __init__(self, *, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int, small_queue_active_operations_max: int, large_queue_active_operations_max: int, disabled: Optional[bool] = None, video_preload_large: Optional[bool] = None, audio_preload_next: Optional[bool] = None, phonecalls_less_data: Optional[bool] = None, stories_preload: Optional[bool] = None) -> None:
        self.photo_size_max = photo_size_max  # int
        self.video_size_max = video_size_max  # long
        self.file_size_max = file_size_max  # long
        self.video_upload_maxbitrate = video_upload_maxbitrate  # int
        self.small_queue_active_operations_max = small_queue_active_operations_max  # int
        self.large_queue_active_operations_max = large_queue_active_operations_max  # int
        self.disabled = disabled  # flags.0?true
        self.video_preload_large = video_preload_large  # flags.1?true
        self.audio_preload_next = audio_preload_next  # flags.2?true
        self.phonecalls_less_data = phonecalls_less_data  # flags.3?true
        self.stories_preload = stories_preload  # flags.4?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoDownloadSettings":

        flags = Int.read(b)

        disabled = True if flags & (1 << 0) else False
        video_preload_large = True if flags & (1 << 1) else False
        audio_preload_next = True if flags & (1 << 2) else False
        phonecalls_less_data = True if flags & (1 << 3) else False
        stories_preload = True if flags & (1 << 4) else False
        photo_size_max = Int.read(b)

        video_size_max = Long.read(b)

        file_size_max = Long.read(b)

        video_upload_maxbitrate = Int.read(b)

        small_queue_active_operations_max = Int.read(b)

        large_queue_active_operations_max = Int.read(b)

        return AutoDownloadSettings(photo_size_max=photo_size_max, video_size_max=video_size_max, file_size_max=file_size_max, video_upload_maxbitrate=video_upload_maxbitrate, small_queue_active_operations_max=small_queue_active_operations_max, large_queue_active_operations_max=large_queue_active_operations_max, disabled=disabled, video_preload_large=video_preload_large, audio_preload_next=audio_preload_next, phonecalls_less_data=phonecalls_less_data, stories_preload=stories_preload)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.disabled else 0
        flags |= (1 << 1) if self.video_preload_large else 0
        flags |= (1 << 2) if self.audio_preload_next else 0
        flags |= (1 << 3) if self.phonecalls_less_data else 0
        flags |= (1 << 4) if self.stories_preload else 0
        b.write(Int(flags))

        b.write(Int(self.photo_size_max))

        b.write(Long(self.video_size_max))

        b.write(Long(self.file_size_max))

        b.write(Int(self.video_upload_maxbitrate))

        b.write(Int(self.small_queue_active_operations_max))

        b.write(Int(self.large_queue_active_operations_max))

        return b.getvalue()
