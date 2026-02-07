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


class WebPage(TLObject):  # type: ignore
    """Webpage preview

    Constructor of :obj:`~pyrogram.raw.base.WebPage`.

    Details:
        - Layer: ``224``
        - ID: ``E89C45B2``

    Parameters:
        id (``int`` ``64-bit``):
            Preview ID

        url (``str``):
            URL of previewed webpage

        display_url (``str``):
            Webpage URL to be displayed to the user

        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

        has_large_media (``bool``, *optional*):
            Whether the size of the media in the preview can be changed.

        video_cover_photo (``bool``, *optional*):
            N/A

        type (``str``, *optional*):
            Type of the web page. Can be: article, photo, audio, video, document, profile, app, or something else

        site_name (``str``, *optional*):
            Short name of the site (e.g., Google Docs, App Store)

        title (``str``, *optional*):
            Title of the content

        description (``str``, *optional*):
            Content description

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            Image representing the content

        embed_url (``str``, *optional*):
            URL to show in the embedded preview

        embed_type (``str``, *optional*):
            MIME type of the embedded preview, (e.g., text/html or video/mp4)

        embed_width (``int`` ``32-bit``, *optional*):
            Width of the embedded preview

        embed_height (``int`` ``32-bit``, *optional*):
            Height of the embedded preview

        duration (``int`` ``32-bit``, *optional*):
            Duration of the content, in seconds

        author (``str``, *optional*):
            Author of the content

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            Preview of the content as a media file

        cached_page (:obj:`Page <pyrogram.raw.base.Page>`, *optional*):
            Page contents in instant view format

        attributes (List of :obj:`WebPageAttribute <pyrogram.raw.base.WebPageAttribute>`, *optional*):
            Webpage attributes

    """

    __slots__: List[str] = ["id", "url", "display_url", "hash", "has_large_media", "video_cover_photo", "type", "site_name", "title", "description", "photo", "embed_url", "embed_type", "embed_width", "embed_height", "duration", "author", "document", "cached_page", "attributes"]

    ID = 0xe89c45b2
    QUALNAME = "types.WebPage"

    def __init__(self, *, id: int, url: str, display_url: str, hash: int, has_large_media: Optional[bool] = None, video_cover_photo: Optional[bool] = None, type: Optional[str] = None, site_name: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None, photo: "raw.base.Photo" = None, embed_url: Optional[str] = None, embed_type: Optional[str] = None, embed_width: Optional[int] = None, embed_height: Optional[int] = None, duration: Optional[int] = None, author: Optional[str] = None, document: "raw.base.Document" = None, cached_page: "raw.base.Page" = None, attributes: Optional[List["raw.base.WebPageAttribute"]] = None) -> None:
        self.id = id  # long
        self.url = url  # string
        self.display_url = display_url  # string
        self.hash = hash  # int
        self.has_large_media = has_large_media  # flags.13?true
        self.video_cover_photo = video_cover_photo  # flags.14?true
        self.type = type  # flags.0?string
        self.site_name = site_name  # flags.1?string
        self.title = title  # flags.2?string
        self.description = description  # flags.3?string
        self.photo = photo  # flags.4?Photo
        self.embed_url = embed_url  # flags.5?string
        self.embed_type = embed_type  # flags.5?string
        self.embed_width = embed_width  # flags.6?int
        self.embed_height = embed_height  # flags.6?int
        self.duration = duration  # flags.7?int
        self.author = author  # flags.8?string
        self.document = document  # flags.9?Document
        self.cached_page = cached_page  # flags.10?Page
        self.attributes = attributes  # flags.12?Vector<WebPageAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPage":

        flags = Int.read(b)

        has_large_media = True if flags & (1 << 13) else False
        video_cover_photo = True if flags & (1 << 14) else False
        id = Long.read(b)

        url = String.read(b)

        display_url = String.read(b)

        hash = Int.read(b)

        type = String.read(b) if flags & (1 << 0) else None
        site_name = String.read(b) if flags & (1 << 1) else None
        title = String.read(b) if flags & (1 << 2) else None
        description = String.read(b) if flags & (1 << 3) else None
        photo = TLObject.read(b) if flags & (1 << 4) else None

        embed_url = String.read(b) if flags & (1 << 5) else None
        embed_type = String.read(b) if flags & (1 << 5) else None
        embed_width = Int.read(b) if flags & (1 << 6) else None
        embed_height = Int.read(b) if flags & (1 << 6) else None
        duration = Int.read(b) if flags & (1 << 7) else None
        author = String.read(b) if flags & (1 << 8) else None
        document = TLObject.read(b) if flags & (1 << 9) else None

        cached_page = TLObject.read(b) if flags & (1 << 10) else None

        attributes = TLObject.read(b) if flags & (1 << 12) else []

        return WebPage(id=id, url=url, display_url=display_url, hash=hash, has_large_media=has_large_media, video_cover_photo=video_cover_photo, type=type, site_name=site_name, title=title, description=description, photo=photo, embed_url=embed_url, embed_type=embed_type, embed_width=embed_width, embed_height=embed_height, duration=duration, author=author, document=document, cached_page=cached_page, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 13) if self.has_large_media else 0
        flags |= (1 << 14) if self.video_cover_photo else 0
        flags |= (1 << 0) if self.type is not None else 0
        flags |= (1 << 1) if self.site_name is not None else 0
        flags |= (1 << 2) if self.title is not None else 0
        flags |= (1 << 3) if self.description is not None else 0
        flags |= (1 << 4) if self.photo is not None else 0
        flags |= (1 << 5) if self.embed_url is not None else 0
        flags |= (1 << 5) if self.embed_type is not None else 0
        flags |= (1 << 6) if self.embed_width is not None else 0
        flags |= (1 << 6) if self.embed_height is not None else 0
        flags |= (1 << 7) if self.duration is not None else 0
        flags |= (1 << 8) if self.author is not None else 0
        flags |= (1 << 9) if self.document is not None else 0
        flags |= (1 << 10) if self.cached_page is not None else 0
        flags |= (1 << 12) if self.attributes else 0
        b.write(Int(flags))

        b.write(Long(self.id))

        b.write(String(self.url))

        b.write(String(self.display_url))

        b.write(Int(self.hash))

        if self.type is not None:
            b.write(String(self.type))

        if self.site_name is not None:
            b.write(String(self.site_name))

        if self.title is not None:
            b.write(String(self.title))

        if self.description is not None:
            b.write(String(self.description))

        if self.photo is not None:
            b.write(self.photo.write())

        if self.embed_url is not None:
            b.write(String(self.embed_url))

        if self.embed_type is not None:
            b.write(String(self.embed_type))

        if self.embed_width is not None:
            b.write(Int(self.embed_width))

        if self.embed_height is not None:
            b.write(Int(self.embed_height))

        if self.duration is not None:
            b.write(Int(self.duration))

        if self.author is not None:
            b.write(String(self.author))

        if self.document is not None:
            b.write(self.document.write())

        if self.cached_page is not None:
            b.write(self.cached_page.write())

        if self.attributes is not None:
            b.write(Vector(self.attributes))

        return b.getvalue()
