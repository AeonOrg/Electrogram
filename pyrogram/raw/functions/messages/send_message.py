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


class SendMessage(TLObject):  # type: ignore
    """Sends a message to a chat


    Details:
        - Layer: ``224``
        - ID: ``545CD15A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The destination where the message will be sent

        message (``str``):
            The message

        random_id (``int`` ``64-bit``):
            Unique client message ID required to prevent message resending

        no_webpage (``bool``, *optional*):
            Set this flag to disable generation of the webpage preview

        silent (``bool``, *optional*):
            Send this message silently (no notifications for the receivers)

        background (``bool``, *optional*):
            Send this message as background message

        clear_draft (``bool``, *optional*):
            Clear the draft field

        noforwards (``bool``, *optional*):
            Only for bots, disallows forwarding and saving of the messages, even if the destination chat doesn't have content protection enabled

        update_stickersets_order (``bool``, *optional*):
            Whether to move used stickersets to top, see here for more info on this flag »

        invert_media (``bool``, *optional*):
            If set, any eventual webpage preview will be shown on top of the message instead of at the bottom.

        allow_paid_floodskip (``bool``, *optional*):
            N/A

        reply_to (:obj:`InputReplyTo <pyrogram.raw.base.InputReplyTo>`, *optional*):
            If set, indicates that the message should be sent in reply to the specified message or story. Also used to quote other messages.

        reply_markup (:obj:`ReplyMarkup <pyrogram.raw.base.ReplyMarkup>`, *optional*):
            Reply markup for sending bot buttons

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for sending styled text

        schedule_date (``int`` ``32-bit``, *optional*):
            Scheduled message date for scheduled messages

        schedule_repeat_period (``int`` ``32-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Send this message as the specified peer

        quick_reply_shortcut (:obj:`InputQuickReplyShortcut <pyrogram.raw.base.InputQuickReplyShortcut>`, *optional*):


        effect (``int`` ``64-bit``, *optional*):


        allow_paid_stars (``int`` ``64-bit``, *optional*):
            N/A

        suggested_post (:obj:`SuggestedPost <pyrogram.raw.base.SuggestedPost>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "message", "random_id", "no_webpage", "silent", "background", "clear_draft", "noforwards", "update_stickersets_order", "invert_media", "allow_paid_floodskip", "reply_to", "reply_markup", "entities", "schedule_date", "schedule_repeat_period", "send_as", "quick_reply_shortcut", "effect", "allow_paid_stars", "suggested_post"]

    ID = 0x545cd15a
    QUALNAME = "functions.messages.SendMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", message: str, random_id: int, no_webpage: Optional[bool] = None, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: "raw.base.InputReplyTo" = None, reply_markup: "raw.base.ReplyMarkup" = None, entities: Optional[List["raw.base.MessageEntity"]] = None, schedule_date: Optional[int] = None, schedule_repeat_period: Optional[int] = None, send_as: "raw.base.InputPeer" = None, quick_reply_shortcut: "raw.base.InputQuickReplyShortcut" = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: "raw.base.SuggestedPost" = None) -> None:
        self.peer = peer  # InputPeer
        self.message = message  # string
        self.random_id = random_id  # long
        self.no_webpage = no_webpage  # flags.1?true
        self.silent = silent  # flags.5?true
        self.background = background  # flags.6?true
        self.clear_draft = clear_draft  # flags.7?true
        self.noforwards = noforwards  # flags.14?true
        self.update_stickersets_order = update_stickersets_order  # flags.15?true
        self.invert_media = invert_media  # flags.16?true
        self.allow_paid_floodskip = allow_paid_floodskip  # flags.19?true
        self.reply_to = reply_to  # flags.0?InputReplyTo
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>
        self.schedule_date = schedule_date  # flags.10?int
        self.schedule_repeat_period = schedule_repeat_period  # flags.24?int
        self.send_as = send_as  # flags.13?InputPeer
        self.quick_reply_shortcut = quick_reply_shortcut  # flags.17?InputQuickReplyShortcut
        self.effect = effect  # flags.18?long
        self.allow_paid_stars = allow_paid_stars  # flags.21?long
        self.suggested_post = suggested_post  # flags.22?SuggestedPost

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessage":

        flags = Int.read(b)

        no_webpage = True if flags & (1 << 1) else False
        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        noforwards = True if flags & (1 << 14) else False
        update_stickersets_order = True if flags & (1 << 15) else False
        invert_media = True if flags & (1 << 16) else False
        allow_paid_floodskip = True if flags & (1 << 19) else False
        peer = TLObject.read(b)

        reply_to = TLObject.read(b) if flags & (1 << 0) else None

        message = String.read(b)

        random_id = Long.read(b)

        reply_markup = TLObject.read(b) if flags & (1 << 2) else None

        entities = TLObject.read(b) if flags & (1 << 3) else []

        schedule_date = Int.read(b) if flags & (1 << 10) else None
        schedule_repeat_period = Int.read(b) if flags & (1 << 24) else None
        send_as = TLObject.read(b) if flags & (1 << 13) else None

        quick_reply_shortcut = TLObject.read(b) if flags & (1 << 17) else None

        effect = Long.read(b) if flags & (1 << 18) else None
        allow_paid_stars = Long.read(b) if flags & (1 << 21) else None
        suggested_post = TLObject.read(b) if flags & (1 << 22) else None

        return SendMessage(peer=peer, message=message, random_id=random_id, no_webpage=no_webpage, silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, allow_paid_floodskip=allow_paid_floodskip, reply_to=reply_to, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, schedule_repeat_period=schedule_repeat_period, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, effect=effect, allow_paid_stars=allow_paid_stars, suggested_post=suggested_post)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage else 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 7) if self.clear_draft else 0
        flags |= (1 << 14) if self.noforwards else 0
        flags |= (1 << 15) if self.update_stickersets_order else 0
        flags |= (1 << 16) if self.invert_media else 0
        flags |= (1 << 19) if self.allow_paid_floodskip else 0
        flags |= (1 << 0) if self.reply_to is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        flags |= (1 << 3) if self.entities else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        flags |= (1 << 24) if self.schedule_repeat_period is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        flags |= (1 << 17) if self.quick_reply_shortcut is not None else 0
        flags |= (1 << 18) if self.effect is not None else 0
        flags |= (1 << 21) if self.allow_paid_stars is not None else 0
        flags |= (1 << 22) if self.suggested_post is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.reply_to is not None:
            b.write(self.reply_to.write())

        b.write(String(self.message))

        b.write(Long(self.random_id))

        if self.reply_markup is not None:
            b.write(self.reply_markup.write())

        if self.entities is not None:
            b.write(Vector(self.entities))

        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))

        if self.schedule_repeat_period is not None:
            b.write(Int(self.schedule_repeat_period))

        if self.send_as is not None:
            b.write(self.send_as.write())

        if self.quick_reply_shortcut is not None:
            b.write(self.quick_reply_shortcut.write())

        if self.effect is not None:
            b.write(Long(self.effect))

        if self.allow_paid_stars is not None:
            b.write(Long(self.allow_paid_stars))

        if self.suggested_post is not None:
            b.write(self.suggested_post.write())

        return b.getvalue()
