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


class MessageMediaDocument(TLObject):  # type: ignore
    """Document (video, audio, voice, sticker, any media type except photo)

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``52D8CCD9``

    Parameters:
        nopremium (``bool``, *optional*):
            Whether this is a normal sticker, if not set this is a premium sticker and a premium sticker animation must be played.

        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        video (``bool``, *optional*):
            Whether this is a video.

        round (``bool``, *optional*):
            Whether this is a round video.

        voice (``bool``, *optional*):
            Whether this is a voice message.

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            Attached document

        alt_documents (List of :obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        video_cover (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        video_timestamp (``int`` ``32-bit``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Time to live of self-destructing document

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["nopremium", "spoiler", "video", "round", "voice", "document", "alt_documents", "video_cover", "video_timestamp", "ttl_seconds"]

    ID = 0x52d8ccd9
    QUALNAME = "types.MessageMediaDocument"

    def __init__(self, *, nopremium: Optional[bool] = None, spoiler: Optional[bool] = None, video: Optional[bool] = None, round: Optional[bool] = None, voice: Optional[bool] = None, document: "raw.base.Document" = None, alt_documents: Optional[List["raw.base.Document"]] = None, video_cover: "raw.base.Photo" = None, video_timestamp: Optional[int] = None, ttl_seconds: Optional[int] = None) -> None:
        self.nopremium = nopremium  # flags.3?true
        self.spoiler = spoiler  # flags.4?true
        self.video = video  # flags.6?true
        self.round = round  # flags.7?true
        self.voice = voice  # flags.8?true
        self.document = document  # flags.0?Document
        self.alt_documents = alt_documents  # flags.5?Vector<Document>
        self.video_cover = video_cover  # flags.9?Photo
        self.video_timestamp = video_timestamp  # flags.10?int
        self.ttl_seconds = ttl_seconds  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaDocument":

        flags = Int.read(b)

        nopremium = True if flags & (1 << 3) else False
        spoiler = True if flags & (1 << 4) else False
        video = True if flags & (1 << 6) else False
        round = True if flags & (1 << 7) else False
        voice = True if flags & (1 << 8) else False
        document = TLObject.read(b) if flags & (1 << 0) else None

        alt_documents = TLObject.read(b) if flags & (1 << 5) else []

        video_cover = TLObject.read(b) if flags & (1 << 9) else None

        video_timestamp = Int.read(b) if flags & (1 << 10) else None
        ttl_seconds = Int.read(b) if flags & (1 << 2) else None
        return MessageMediaDocument(nopremium=nopremium, spoiler=spoiler, video=video, round=round, voice=voice, document=document, alt_documents=alt_documents, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.nopremium else 0
        flags |= (1 << 4) if self.spoiler else 0
        flags |= (1 << 6) if self.video else 0
        flags |= (1 << 7) if self.round else 0
        flags |= (1 << 8) if self.voice else 0
        flags |= (1 << 0) if self.document is not None else 0
        flags |= (1 << 5) if self.alt_documents else 0
        flags |= (1 << 9) if self.video_cover is not None else 0
        flags |= (1 << 10) if self.video_timestamp is not None else 0
        flags |= (1 << 2) if self.ttl_seconds is not None else 0
        b.write(Int(flags))

        if self.document is not None:
            b.write(self.document.write())

        if self.alt_documents is not None:
            b.write(Vector(self.alt_documents))

        if self.video_cover is not None:
            b.write(self.video_cover.write())

        if self.video_timestamp is not None:
            b.write(Int(self.video_timestamp))

        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))

        return b.getvalue()
