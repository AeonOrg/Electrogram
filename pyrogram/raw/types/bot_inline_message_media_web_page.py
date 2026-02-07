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


class BotInlineMessageMediaWebPage(TLObject):  # type: ignore
    """Specifies options that must be used to generate the link preview for the message, or even a standalone link preview without an attached message.

    Constructor of :obj:`~pyrogram.raw.base.BotInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``809AD9A6``

    Parameters:
        message (``str``):
            The message, can be empty.

        url (``str``):
            The URL to use for the link preview.

        invert_media (``bool``, *optional*):
            If set, any eventual webpage preview will be shown on top of the message instead of at the bottom.

        force_large_media (``bool``, *optional*):
            If set, specifies that a large media preview should be used.

        force_small_media (``bool``, *optional*):
            If set, specifies that a small media preview should be used.

        manual (``bool``, *optional*):
            If set, indicates that the URL used for the webpage preview was specified manually using inputMediaWebPage, and may not be related to any of the URLs specified in the message.

        safe (``bool``, *optional*):
            If set, the link can be opened directly without user confirmation.

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Reply markup for sending bot buttons

    """

    __slots__: List[str] = ["message", "url", "invert_media", "force_large_media", "force_small_media", "manual", "safe", "entities", "reply_markup"]

    ID = 0x809ad9a6
    QUALNAME = "types.BotInlineMessageMediaWebPage"

    def __init__(self, *, message: str, url: str, invert_media: Optional[bool] = None, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, manual: Optional[bool] = None, safe: Optional[bool] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.message = message  # string
        self.url = url  # string
        self.invert_media = invert_media  # flags.3?true
        self.force_large_media = force_large_media  # flags.4?true
        self.force_small_media = force_small_media  # flags.5?true
        self.manual = manual  # flags.7?true
        self.safe = safe  # flags.8?true
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageMediaWebPage":

        flags = Int.read(b)

        invert_media = True if flags & (1 << 3) else False
        force_large_media = True if flags & (1 << 4) else False
        force_small_media = True if flags & (1 << 5) else False
        manual = True if flags & (1 << 7) else False
        safe = True if flags & (1 << 8) else False
        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 1) else []

        url = String.read(b)

        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        return BotInlineMessageMediaWebPage(message=message, url=url, invert_media=invert_media, force_large_media=force_large_media, force_small_media=force_small_media, manual=manual, safe=safe, entities=entities, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.invert_media else 0
        flags |= (1 << 4) if self.force_large_media else 0
        flags |= (1 << 5) if self.force_small_media else 0
        flags |= (1 << 7) if self.manual else 0
        flags |= (1 << 8) if self.safe else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))

        b.write(String(self.message))

        if self.entities is not None:
            b.write(Vector(self.entities))

        b.write(String(self.url))

        if self.reply_markup is not None:
            b.write(self.reply_markup.write())

        return b.getvalue()
