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


class EditInlineBotMessage(TLObject):  # type: ignore
    """Edit an inline bot message


    Details:
        - Layer: ``224``
        - ID: ``83557DBA``

    Parameters:
        id (:obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`):
            Sent inline message ID

        no_webpage (``bool``, *optional*):
            Disable webpage preview

        invert_media (``bool``, *optional*):
            If set, any eventual webpage preview will be shown on top of the message instead of at the bottom.

        message (``str``, *optional*):
            Message

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            Media

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Reply markup for inline keyboards

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "no_webpage", "invert_media", "message", "media", "reply_markup", "entities"]

    ID = 0x83557dba
    QUALNAME = "functions.messages.EditInlineBotMessage"

    def __init__(self, *, id: "raw.base.InputBotInlineMessageID", no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: "raw.base.InputMedia" = None, reply_markup: "raw.base.ReplyMarkup" = None, entities: Optional[List["raw.base.MessageEntity"]] = None) -> None:
        self.id = id  # InputBotInlineMessageID
        self.no_webpage = no_webpage  # flags.1?true
        self.invert_media = invert_media  # flags.16?true
        self.message = message  # flags.11?string
        self.media = media  # flags.14?InputMedia
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditInlineBotMessage":

        flags = Int.read(b)

        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 16) else False
        id = TLObject.read(b)

        message = String.read(b) if flags & (1 << 11) else None
        media = TLObject.read(b) if flags & (1 << 14) else None

        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        entities = TLObject.read(b) if flags & (1 << 3) else []

        return EditInlineBotMessage(id=id, no_webpage=no_webpage, invert_media=invert_media, message=message, media=media, reply_markup=reply_markup, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage else 0
        flags |= (1 << 16) if self.invert_media else 0
        flags |= (1 << 11) if self.message is not None else 0
        flags |= (1 << 14) if self.media is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        flags |= (1 << 3) if self.entities else 0
        b.write(Int(flags))

        b.write(self.id.write())

        if self.message is not None:
            b.write(String(self.message))

        if self.media is not None:
            b.write(self.media.write())

        if self.reply_markup is not None:
            b.write(self.reply_markup.write())

        if self.entities is not None:
            b.write(Vector(self.entities))

        return b.getvalue()
