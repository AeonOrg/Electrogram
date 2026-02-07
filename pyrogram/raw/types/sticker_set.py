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


class StickerSet(TLObject):  # type: ignore
    """Represents a stickerset (stickerpack)

    Constructor of :obj:`~pyrogram.raw.base.StickerSet`.

    Details:
        - Layer: ``224``
        - ID: ``2DD14EDC``

    Parameters:
        id (``int`` ``64-bit``):
            ID of the stickerset

        access_hash (``int`` ``64-bit``):
            Access hash of stickerset

        title (``str``):
            Title of stickerset

        short_name (``str``):
            Short name of stickerset, used when sharing stickerset using stickerset deep links.

        count (``int`` ``32-bit``):
            Number of stickers in pack

        hash (``int`` ``32-bit``):
            Hash

        archived (``bool``, *optional*):
            Whether this stickerset was archived (due to too many saved stickers in the current account)

        official (``bool``, *optional*):
            Is this stickerset official

        masks (``bool``, *optional*):
            Is this a mask stickerset

        emojis (``bool``, *optional*):
            This is a custom emoji stickerset

        text_color (``bool``, *optional*):
            Whether the color of this TGS custom emoji stickerset should be changed to the text color when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context.

        channel_emoji_status (``bool``, *optional*):
            If set, this custom emoji stickerset can be used in channel emoji statuses.

        creator (``bool``, *optional*):


        installed_date (``int`` ``32-bit``, *optional*):
            When was this stickerset installed

        thumbs (List of :obj:`PhotoSize <pyrogram.raw.base.PhotoSize>`, *optional*):
            Stickerset thumbnail

        thumb_dc_id (``int`` ``32-bit``, *optional*):
            DC ID of thumbnail

        thumb_version (``int`` ``32-bit``, *optional*):
            Thumbnail version

        thumb_document_id (``int`` ``64-bit``, *optional*):
            Document ID of custom emoji thumbnail, fetch the document using messages.getCustomEmojiDocuments

    """

    __slots__: List[str] = ["id", "access_hash", "title", "short_name", "count", "hash", "archived", "official", "masks", "emojis", "text_color", "channel_emoji_status", "creator", "installed_date", "thumbs", "thumb_dc_id", "thumb_version", "thumb_document_id"]

    ID = 0x2dd14edc
    QUALNAME = "types.StickerSet"

    def __init__(self, *, id: int, access_hash: int, title: str, short_name: str, count: int, hash: int, archived: Optional[bool] = None, official: Optional[bool] = None, masks: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, channel_emoji_status: Optional[bool] = None, creator: Optional[bool] = None, installed_date: Optional[int] = None, thumbs: Optional[List["raw.base.PhotoSize"]] = None, thumb_dc_id: Optional[int] = None, thumb_version: Optional[int] = None, thumb_document_id: Optional[int] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.title = title  # string
        self.short_name = short_name  # string
        self.count = count  # int
        self.hash = hash  # int
        self.archived = archived  # flags.1?true
        self.official = official  # flags.2?true
        self.masks = masks  # flags.3?true
        self.emojis = emojis  # flags.7?true
        self.text_color = text_color  # flags.9?true
        self.channel_emoji_status = channel_emoji_status  # flags.10?true
        self.creator = creator  # flags.11?true
        self.installed_date = installed_date  # flags.0?int
        self.thumbs = thumbs  # flags.4?Vector<PhotoSize>
        self.thumb_dc_id = thumb_dc_id  # flags.4?int
        self.thumb_version = thumb_version  # flags.4?int
        self.thumb_document_id = thumb_document_id  # flags.8?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSet":

        flags = Int.read(b)

        archived = True if flags & (1 << 1) else False
        official = True if flags & (1 << 2) else False
        masks = True if flags & (1 << 3) else False
        emojis = True if flags & (1 << 7) else False
        text_color = True if flags & (1 << 9) else False
        channel_emoji_status = True if flags & (1 << 10) else False
        creator = True if flags & (1 << 11) else False
        installed_date = Int.read(b) if flags & (1 << 0) else None
        id = Long.read(b)

        access_hash = Long.read(b)

        title = String.read(b)

        short_name = String.read(b)

        thumbs = TLObject.read(b) if flags & (1 << 4) else []

        thumb_dc_id = Int.read(b) if flags & (1 << 4) else None
        thumb_version = Int.read(b) if flags & (1 << 4) else None
        thumb_document_id = Long.read(b) if flags & (1 << 8) else None
        count = Int.read(b)

        hash = Int.read(b)

        return StickerSet(id=id, access_hash=access_hash, title=title, short_name=short_name, count=count, hash=hash, archived=archived, official=official, masks=masks, emojis=emojis, text_color=text_color, channel_emoji_status=channel_emoji_status, creator=creator, installed_date=installed_date, thumbs=thumbs, thumb_dc_id=thumb_dc_id, thumb_version=thumb_version, thumb_document_id=thumb_document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.archived else 0
        flags |= (1 << 2) if self.official else 0
        flags |= (1 << 3) if self.masks else 0
        flags |= (1 << 7) if self.emojis else 0
        flags |= (1 << 9) if self.text_color else 0
        flags |= (1 << 10) if self.channel_emoji_status else 0
        flags |= (1 << 11) if self.creator else 0
        flags |= (1 << 0) if self.installed_date is not None else 0
        flags |= (1 << 4) if self.thumbs else 0
        flags |= (1 << 4) if self.thumb_dc_id is not None else 0
        flags |= (1 << 4) if self.thumb_version is not None else 0
        flags |= (1 << 8) if self.thumb_document_id is not None else 0
        b.write(Int(flags))

        if self.installed_date is not None:
            b.write(Int(self.installed_date))

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        b.write(String(self.title))

        b.write(String(self.short_name))

        if self.thumbs is not None:
            b.write(Vector(self.thumbs))

        if self.thumb_dc_id is not None:
            b.write(Int(self.thumb_dc_id))

        if self.thumb_version is not None:
            b.write(Int(self.thumb_version))

        if self.thumb_document_id is not None:
            b.write(Long(self.thumb_document_id))

        b.write(Int(self.count))

        b.write(Int(self.hash))

        return b.getvalue()
