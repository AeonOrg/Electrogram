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


class InputChatUploadedPhoto(TLObject):  # type: ignore
    """New photo to be set as group profile photo.

    Constructor of :obj:`~pyrogram.raw.base.InputChatPhoto`.

    Details:
        - Layer: ``224``
        - ID: ``BDCDAEC0``

    Parameters:
        file (:obj:`InputFile <pyrogram.raw.base.InputFile>`, *optional*):
            File saved in parts using the method upload.saveFilePart

        video (:obj:`InputFile <pyrogram.raw.base.InputFile>`, *optional*):
            Square video for animated profile picture

        video_start_ts (``float`` ``64-bit``, *optional*):
            Floating point UNIX timestamp in seconds, indicating the frame of the video/sticker that should be used as static preview; can only be used if video or video_emoji_markup is set.

        video_emoji_markup (:obj:`VideoSize <pyrogram.raw.base.VideoSize>`, *optional*):
            Animated sticker profile picture, must contain either a videoSizeEmojiMarkup or a videoSizeStickerMarkup constructor.

    """

    __slots__: List[str] = ["file", "video", "video_start_ts", "video_emoji_markup"]

    ID = 0xbdcdaec0
    QUALNAME = "types.InputChatUploadedPhoto"

    def __init__(self, *, file: "raw.base.InputFile" = None, video: "raw.base.InputFile" = None, video_start_ts: Optional[float] = None, video_emoji_markup: "raw.base.VideoSize" = None) -> None:
        self.file = file  # flags.0?InputFile
        self.video = video  # flags.1?InputFile
        self.video_start_ts = video_start_ts  # flags.2?double
        self.video_emoji_markup = video_emoji_markup  # flags.3?VideoSize

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatUploadedPhoto":

        flags = Int.read(b)

        file = TLObject.read(b) if flags & (1 << 0) else None

        video = TLObject.read(b) if flags & (1 << 1) else None

        video_start_ts = Double.read(b) if flags & (1 << 2) else None
        video_emoji_markup = TLObject.read(b) if flags & (1 << 3) else None

        return InputChatUploadedPhoto(file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.file is not None else 0
        flags |= (1 << 1) if self.video is not None else 0
        flags |= (1 << 2) if self.video_start_ts is not None else 0
        flags |= (1 << 3) if self.video_emoji_markup is not None else 0
        b.write(Int(flags))

        if self.file is not None:
            b.write(self.file.write())

        if self.video is not None:
            b.write(self.video.write())

        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))

        if self.video_emoji_markup is not None:
            b.write(self.video_emoji_markup.write())

        return b.getvalue()
