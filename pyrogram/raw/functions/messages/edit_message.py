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


class EditMessage(TLObject):  # type: ignore
    """Edit message


    Details:
        - Layer: ``224``
        - ID: ``51E842E1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Where was the message sent

        id (``int`` ``32-bit``):
            ID of the message to edit

        no_webpage (``bool``, *optional*):
            Disable webpage preview

        invert_media (``bool``, *optional*):
            If set, any eventual webpage preview will be shown on top of the message instead of at the bottom.

        message (``str``, *optional*):
            New message

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            New attached media

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Reply markup for inline keyboards

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

        schedule_date (``int`` ``32-bit``, *optional*):
            Scheduled message date for scheduled messages

        schedule_repeat_period (``int`` ``32-bit``, *optional*):
            N/A

        quick_reply_shortcut_id (``int`` ``32-bit``, *optional*):


    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "no_webpage", "invert_media", "message", "media", "reply_markup", "entities", "schedule_date", "schedule_repeat_period", "quick_reply_shortcut_id"]

    ID = 0x51e842e1
    QUALNAME = "functions.messages.EditMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: "raw.base.InputMedia" = None, reply_markup: "raw.base.ReplyMarkup" = None, entities: Optional[List["raw.base.MessageEntity"]] = None, schedule_date: Optional[int] = None, schedule_repeat_period: Optional[int] = None, quick_reply_shortcut_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.no_webpage = no_webpage  # flags.1?true
        self.invert_media = invert_media  # flags.16?true
        self.message = message  # flags.11?string
        self.media = media  # flags.14?InputMedia
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>
        self.schedule_date = schedule_date  # flags.15?int
        self.schedule_repeat_period = schedule_repeat_period  # flags.18?int
        self.quick_reply_shortcut_id = quick_reply_shortcut_id  # flags.17?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditMessage":

        flags = Int.read(b)

        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 16) else False
        peer = TLObject.read(b)

        id = Int.read(b)

        message = String.read(b) if flags & (1 << 11) else None
        media = TLObject.read(b) if flags & (1 << 14) else None

        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        entities = TLObject.read(b) if flags & (1 << 3) else []

        schedule_date = Int.read(b) if flags & (1 << 15) else None
        schedule_repeat_period = Int.read(b) if flags & (1 << 18) else None
        quick_reply_shortcut_id = Int.read(b) if flags & (1 << 17) else None
        return EditMessage(peer=peer, id=id, no_webpage=no_webpage, invert_media=invert_media, message=message, media=media, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, schedule_repeat_period=schedule_repeat_period, quick_reply_shortcut_id=quick_reply_shortcut_id)

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
        flags |= (1 << 15) if self.schedule_date is not None else 0
        flags |= (1 << 18) if self.schedule_repeat_period is not None else 0
        flags |= (1 << 17) if self.quick_reply_shortcut_id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.id))

        if self.message is not None:
            b.write(String(self.message))

        if self.media is not None:
            b.write(self.media.write())

        if self.reply_markup is not None:
            b.write(self.reply_markup.write())

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))

        if self.schedule_repeat_period is not None:
            b.write(Int(self.schedule_repeat_period))

        if self.quick_reply_shortcut_id is not None:
            b.write(Int(self.quick_reply_shortcut_id))

        return b.getvalue()
