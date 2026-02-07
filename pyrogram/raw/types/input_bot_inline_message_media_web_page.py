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


class InputBotInlineMessageMediaWebPage(TLObject):  # type: ignore
    """Specifies options that will be used to generate the link preview for the message, or even a standalone link preview without an attached message.

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``224``
        - ID: ``BDDCC510``

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

        optional (``bool``, *optional*):
            If not set, a WEBPAGE_NOT_FOUND RPC error will be emitted if a webpage preview cannot be generated for the specified url; otherwise, no error will be emitted (unless the provided message is also empty, in which case a MESSAGE_EMPTY will be emitted, instead).

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Inline keyboard

    """

    __slots__: List[str] = ["message", "url", "invert_media", "force_large_media", "force_small_media", "optional", "entities", "reply_markup"]

    ID = 0xbddcc510
    QUALNAME = "types.InputBotInlineMessageMediaWebPage"

    def __init__(self, *, message: str, url: str, invert_media: Optional[bool] = None, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, optional: Optional[bool] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.message = message  # string
        self.url = url  # string
        self.invert_media = invert_media  # flags.3?true
        self.force_large_media = force_large_media  # flags.4?true
        self.force_small_media = force_small_media  # flags.5?true
        self.optional = optional  # flags.6?true
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageMediaWebPage":

        flags = Int.read(b)

        invert_media = True if flags & (1 << 3) else False
        force_large_media = True if flags & (1 << 4) else False
        force_small_media = True if flags & (1 << 5) else False
        optional = True if flags & (1 << 6) else False
        message = String.read(b)

        entities = TLObject.read(b) if flags & (1 << 1) else []

        url = String.read(b)

        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        return InputBotInlineMessageMediaWebPage(message=message, url=url, invert_media=invert_media, force_large_media=force_large_media, force_small_media=force_small_media, optional=optional, entities=entities, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.invert_media else 0
        flags |= (1 << 4) if self.force_large_media else 0
        flags |= (1 << 5) if self.force_small_media else 0
        flags |= (1 << 6) if self.optional else 0
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
