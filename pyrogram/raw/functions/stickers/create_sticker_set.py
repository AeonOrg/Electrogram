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


class CreateStickerSet(TLObject):  # type: ignore
    """Create a stickerset, bots only.


    Details:
        - Layer: ``224``
        - ID: ``9021AB67``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            Stickerset owner

        title (``str``):
            Stickerset name, 1-64 chars

        short_name (``str``):
            Short name of sticker set, to be used in sticker deep links ». Can contain only english letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and, if called by a bot, must end in "_by_<bot_username>". <bot_username> is case insensitive. 1-64 characters.

        stickers (List of :obj:`InputStickerSetItem <pyrogram.raw.base.InputStickerSetItem>`):
            Stickers

        masks (``bool``, *optional*):
            Whether this is a mask stickerset

        emojis (``bool``, *optional*):
            Whether this is a custom emoji stickerset.

        text_color (``bool``, *optional*):
            Whether the color of TGS custom emojis contained in this set should be changed to the text color when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context. For custom emoji stickersets only.

        thumb (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            Thumbnail

        software (``str``, *optional*):
            Used when importing stickers using the sticker import SDKs, specifies the name of the software that created the stickers

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["user_id", "title", "short_name", "stickers", "masks", "emojis", "text_color", "thumb", "software"]

    ID = 0x9021ab67
    QUALNAME = "functions.stickers.CreateStickerSet"

    def __init__(self, *, user_id: "raw.base.InputUser", title: str, short_name: str, stickers: List["raw.base.InputStickerSetItem"], masks: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, thumb: "raw.base.InputDocument" = None, software: Optional[str] = None) -> None:
        self.user_id = user_id  # InputUser
        self.title = title  # string
        self.short_name = short_name  # string
        self.stickers = stickers  # Vector<InputStickerSetItem>
        self.masks = masks  # flags.0?true
        self.emojis = emojis  # flags.5?true
        self.text_color = text_color  # flags.6?true
        self.thumb = thumb  # flags.2?InputDocument
        self.software = software  # flags.3?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateStickerSet":

        flags = Int.read(b)

        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 5) else False
        text_color = True if flags & (1 << 6) else False
        user_id = TLObject.read(b)

        title = String.read(b)

        short_name = String.read(b)

        thumb = TLObject.read(b) if flags & (1 << 2) else None

        stickers = TLObject.read(b)

        software = String.read(b) if flags & (1 << 3) else None
        return CreateStickerSet(user_id=user_id, title=title, short_name=short_name, stickers=stickers, masks=masks, emojis=emojis, text_color=text_color, thumb=thumb, software=software)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks else 0
        flags |= (1 << 5) if self.emojis else 0
        flags |= (1 << 6) if self.text_color else 0
        flags |= (1 << 2) if self.thumb is not None else 0
        flags |= (1 << 3) if self.software is not None else 0
        b.write(Int(flags))

        b.write(self.user_id.write())

        b.write(String(self.title))

        b.write(String(self.short_name))

        if self.thumb is not None:
            b.write(self.thumb.write())

        b.write(Vector(self.stickers))

        if self.software is not None:
            b.write(String(self.software))

        return b.getvalue()
