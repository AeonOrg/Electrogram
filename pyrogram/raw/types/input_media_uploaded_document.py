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


class InputMediaUploadedDocument(TLObject):  # type: ignore
    """New document

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``37C9330``

    Parameters:
        file (:obj:`InputFile <pyrogram.raw.base.InputFile>`):
            The uploaded file

        mime_type (``str``):
            MIME type of document

        attributes (List of :obj:`DocumentAttribute <pyrogram.raw.base.DocumentAttribute>`):
            Attributes that specify the type of the document (video, audio, voice, sticker, etc.)

        nosound_video (``bool``, *optional*):
            Whether the specified document is a video file with no audio tracks (a GIF animation (even as MPEG4), for example)

        force_file (``bool``, *optional*):
            Force the media file to be uploaded as document

        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        thumb (:obj:`InputFile <pyrogram.raw.base.InputFile>`, *optional*):
            Thumbnail of the document, uploaded as for the file

        stickers (List of :obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            Attached stickers

        video_cover (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`, *optional*):
            N/A

        video_timestamp (``int`` ``32-bit``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Time to live in seconds of self-destructing document

    """

    __slots__: List[str] = ["file", "mime_type", "attributes", "nosound_video", "force_file", "spoiler", "thumb", "stickers", "video_cover", "video_timestamp", "ttl_seconds"]

    ID = 0x37c9330
    QUALNAME = "types.InputMediaUploadedDocument"

    def __init__(self, *, file: "raw.base.InputFile", mime_type: str, attributes: List["raw.base.DocumentAttribute"], nosound_video: Optional[bool] = None, force_file: Optional[bool] = None, spoiler: Optional[bool] = None, thumb: "raw.base.InputFile" = None, stickers: Optional[List["raw.base.InputDocument"]] = None, video_cover: "raw.base.InputPhoto" = None, video_timestamp: Optional[int] = None, ttl_seconds: Optional[int] = None) -> None:
        self.file = file  # InputFile
        self.mime_type = mime_type  # string
        self.attributes = attributes  # Vector<DocumentAttribute>
        self.nosound_video = nosound_video  # flags.3?true
        self.force_file = force_file  # flags.4?true
        self.spoiler = spoiler  # flags.5?true
        self.thumb = thumb  # flags.2?InputFile
        self.stickers = stickers  # flags.0?Vector<InputDocument>
        self.video_cover = video_cover  # flags.6?InputPhoto
        self.video_timestamp = video_timestamp  # flags.7?int
        self.ttl_seconds = ttl_seconds  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaUploadedDocument":

        flags = Int.read(b)

        nosound_video = True if flags & (1 << 3) else False
        force_file = True if flags & (1 << 4) else False
        spoiler = True if flags & (1 << 5) else False
        file = TLObject.read(b)

        thumb = TLObject.read(b) if flags & (1 << 2) else None

        mime_type = String.read(b)

        attributes = TLObject.read(b)

        stickers = TLObject.read(b) if flags & (1 << 0) else []

        video_cover = TLObject.read(b) if flags & (1 << 6) else None

        video_timestamp = Int.read(b) if flags & (1 << 7) else None
        ttl_seconds = Int.read(b) if flags & (1 << 1) else None
        return InputMediaUploadedDocument(file=file, mime_type=mime_type, attributes=attributes, nosound_video=nosound_video, force_file=force_file, spoiler=spoiler, thumb=thumb, stickers=stickers, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.nosound_video else 0
        flags |= (1 << 4) if self.force_file else 0
        flags |= (1 << 5) if self.spoiler else 0
        flags |= (1 << 2) if self.thumb is not None else 0
        flags |= (1 << 0) if self.stickers else 0
        flags |= (1 << 6) if self.video_cover is not None else 0
        flags |= (1 << 7) if self.video_timestamp is not None else 0
        flags |= (1 << 1) if self.ttl_seconds is not None else 0
        b.write(Int(flags))

        b.write(self.file.write())

        if self.thumb is not None:
            b.write(self.thumb.write())

        b.write(String(self.mime_type))

        b.write(Vector(self.attributes))

        if self.stickers is not None:
            b.write(Vector(self.stickers))

        if self.video_cover is not None:
            b.write(self.video_cover.write())

        if self.video_timestamp is not None:
            b.write(Int(self.video_timestamp))

        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))

        return b.getvalue()
