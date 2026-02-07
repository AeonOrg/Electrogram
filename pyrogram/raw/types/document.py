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


class Document(TLObject):  # type: ignore
    """Document

    Constructor of :obj:`~pyrogram.raw.base.Document`.

    Details:
        - Layer: ``224``
        - ID: ``8FD4C4D8``

    Parameters:
        id (``int`` ``64-bit``):
            Document ID

        access_hash (``int`` ``64-bit``):
            Check sum, dependent on document ID

        file_reference (``bytes``):
            File reference

        date (``int`` ``32-bit``):
            Creation date

        mime_type (``str``):
            MIME type

        size (``int`` ``64-bit``):
            Size

        dc_id (``int`` ``32-bit``):
            DC ID

        attributes (List of :obj:`DocumentAttribute <pyrogram.raw.base.DocumentAttribute>`):
            Attributes

        thumbs (List of :obj:`PhotoSize <pyrogram.raw.base.PhotoSize>`, *optional*):
            Thumbnails

        video_thumbs (List of :obj:`VideoSize <pyrogram.raw.base.VideoSize>`, *optional*):
            Video thumbnails

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.UploadTheme
            account.UploadRingtone
            messages.GetDocumentByHash
            messages.GetCustomEmojiDocuments
    """

    __slots__: List[str] = ["id", "access_hash", "file_reference", "date", "mime_type", "size", "dc_id", "attributes", "thumbs", "video_thumbs"]

    ID = 0x8fd4c4d8
    QUALNAME = "types.Document"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, date: int, mime_type: str, size: int, dc_id: int, attributes: List["raw.base.DocumentAttribute"], thumbs: Optional[List["raw.base.PhotoSize"]] = None, video_thumbs: Optional[List["raw.base.VideoSize"]] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.file_reference = file_reference  # bytes
        self.date = date  # int
        self.mime_type = mime_type  # string
        self.size = size  # long
        self.dc_id = dc_id  # int
        self.attributes = attributes  # Vector<DocumentAttribute>
        self.thumbs = thumbs  # flags.0?Vector<PhotoSize>
        self.video_thumbs = video_thumbs  # flags.1?Vector<VideoSize>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Document":

        flags = Int.read(b)

        id = Long.read(b)

        access_hash = Long.read(b)

        file_reference = Bytes.read(b)

        date = Int.read(b)

        mime_type = String.read(b)

        size = Long.read(b)

        thumbs = TLObject.read(b) if flags & (1 << 0) else []

        video_thumbs = TLObject.read(b) if flags & (1 << 1) else []

        dc_id = Int.read(b)

        attributes = TLObject.read(b)

        return Document(id=id, access_hash=access_hash, file_reference=file_reference, date=date, mime_type=mime_type, size=size, dc_id=dc_id, attributes=attributes, thumbs=thumbs, video_thumbs=video_thumbs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.thumbs else 0
        flags |= (1 << 1) if self.video_thumbs else 0
        b.write(Int(flags))

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        b.write(Bytes(self.file_reference))

        b.write(Int(self.date))

        b.write(String(self.mime_type))

        b.write(Long(self.size))

        if self.thumbs is not None:
            b.write(Vector(self.thumbs))

        if self.video_thumbs is not None:
            b.write(Vector(self.video_thumbs))

        b.write(Int(self.dc_id))

        b.write(Vector(self.attributes))

        return b.getvalue()
