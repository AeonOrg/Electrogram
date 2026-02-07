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


class ForwardMessages(TLObject):  # type: ignore
    """Forwards messages by their IDs.


    Details:
        - Layer: ``224``
        - ID: ``13704A7C``

    Parameters:
        from_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Source of messages

        id (List of ``int`` ``32-bit``):
            IDs of messages

        random_id (List of ``int`` ``64-bit``):
            Random ID to prevent resending of messages

        to_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Destination peer

        silent (``bool``, *optional*):
            Whether to send messages silently (no notification will be triggered on the destination clients)

        background (``bool``, *optional*):
            Whether to send the message in background

        with_my_score (``bool``, *optional*):
            When forwarding games, whether to include your score in the game

        drop_author (``bool``, *optional*):
            Whether to forward messages without quoting the original author

        drop_media_captions (``bool``, *optional*):
            Whether to strip captions from media

        noforwards (``bool``, *optional*):
            Only for bots, disallows further re-forwarding and saving of the messages, even if the destination chat doesn't have content protection enabled

        allow_paid_floodskip (``bool``, *optional*):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            Destination forum topic

        reply_to (:obj:`InputReplyTo <pyrogram.raw.base.InputReplyTo>`, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            Scheduled message date for scheduled messages

        schedule_repeat_period (``int`` ``32-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Forward the messages as the specified peer

        quick_reply_shortcut (:obj:`InputQuickReplyShortcut <pyrogram.raw.base.InputQuickReplyShortcut>`, *optional*):


        effect (``int`` ``64-bit``, *optional*):
            N/A

        video_timestamp (``int`` ``32-bit``, *optional*):
            N/A

        allow_paid_stars (``int`` ``64-bit``, *optional*):
            N/A

        suggested_post (:obj:`SuggestedPost <pyrogram.raw.base.SuggestedPost>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["from_peer", "id", "random_id", "to_peer", "silent", "background", "with_my_score", "drop_author", "drop_media_captions", "noforwards", "allow_paid_floodskip", "top_msg_id", "reply_to", "schedule_date", "schedule_repeat_period", "send_as", "quick_reply_shortcut", "effect", "video_timestamp", "allow_paid_stars", "suggested_post"]

    ID = 0x13704a7c
    QUALNAME = "functions.messages.ForwardMessages"

    def __init__(self, *, from_peer: "raw.base.InputPeer", id: List[int], random_id: List[int], to_peer: "raw.base.InputPeer", silent: Optional[bool] = None, background: Optional[bool] = None, with_my_score: Optional[bool] = None, drop_author: Optional[bool] = None, drop_media_captions: Optional[bool] = None, noforwards: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, top_msg_id: Optional[int] = None, reply_to: "raw.base.InputReplyTo" = None, schedule_date: Optional[int] = None, schedule_repeat_period: Optional[int] = None, send_as: "raw.base.InputPeer" = None, quick_reply_shortcut: "raw.base.InputQuickReplyShortcut" = None, effect: Optional[int] = None, video_timestamp: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: "raw.base.SuggestedPost" = None) -> None:
        self.from_peer = from_peer  # InputPeer
        self.id = id  # Vector<int>
        self.random_id = random_id  # Vector<long>
        self.to_peer = to_peer  # InputPeer
        self.silent = silent  # flags.5?true
        self.background = background  # flags.6?true
        self.with_my_score = with_my_score  # flags.8?true
        self.drop_author = drop_author  # flags.11?true
        self.drop_media_captions = drop_media_captions  # flags.12?true
        self.noforwards = noforwards  # flags.14?true
        self.allow_paid_floodskip = allow_paid_floodskip  # flags.19?true
        self.top_msg_id = top_msg_id  # flags.9?int
        self.reply_to = reply_to  # flags.22?InputReplyTo
        self.schedule_date = schedule_date  # flags.10?int
        self.schedule_repeat_period = schedule_repeat_period  # flags.24?int
        self.send_as = send_as  # flags.13?InputPeer
        self.quick_reply_shortcut = quick_reply_shortcut  # flags.17?InputQuickReplyShortcut
        self.effect = effect  # flags.18?long
        self.video_timestamp = video_timestamp  # flags.20?int
        self.allow_paid_stars = allow_paid_stars  # flags.21?long
        self.suggested_post = suggested_post  # flags.23?SuggestedPost

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForwardMessages":

        flags = Int.read(b)

        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        with_my_score = True if flags & (1 << 8) else False
        drop_author = True if flags & (1 << 11) else False
        drop_media_captions = True if flags & (1 << 12) else False
        noforwards = True if flags & (1 << 14) else False
        allow_paid_floodskip = True if flags & (1 << 19) else False
        from_peer = TLObject.read(b)

        id = TLObject.read(b, Int)

        random_id = TLObject.read(b, Long)

        to_peer = TLObject.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 9) else None
        reply_to = TLObject.read(b) if flags & (1 << 22) else None

        schedule_date = Int.read(b) if flags & (1 << 10) else None
        schedule_repeat_period = Int.read(b) if flags & (1 << 24) else None
        send_as = TLObject.read(b) if flags & (1 << 13) else None

        quick_reply_shortcut = TLObject.read(b) if flags & (1 << 17) else None

        effect = Long.read(b) if flags & (1 << 18) else None
        video_timestamp = Int.read(b) if flags & (1 << 20) else None
        allow_paid_stars = Long.read(b) if flags & (1 << 21) else None
        suggested_post = TLObject.read(b) if flags & (1 << 23) else None

        return ForwardMessages(from_peer=from_peer, id=id, random_id=random_id, to_peer=to_peer, silent=silent, background=background, with_my_score=with_my_score, drop_author=drop_author, drop_media_captions=drop_media_captions, noforwards=noforwards, allow_paid_floodskip=allow_paid_floodskip, top_msg_id=top_msg_id, reply_to=reply_to, schedule_date=schedule_date, schedule_repeat_period=schedule_repeat_period, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, effect=effect, video_timestamp=video_timestamp, allow_paid_stars=allow_paid_stars, suggested_post=suggested_post)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 8) if self.with_my_score else 0
        flags |= (1 << 11) if self.drop_author else 0
        flags |= (1 << 12) if self.drop_media_captions else 0
        flags |= (1 << 14) if self.noforwards else 0
        flags |= (1 << 19) if self.allow_paid_floodskip else 0
        flags |= (1 << 9) if self.top_msg_id is not None else 0
        flags |= (1 << 22) if self.reply_to is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        flags |= (1 << 24) if self.schedule_repeat_period is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        flags |= (1 << 17) if self.quick_reply_shortcut is not None else 0
        flags |= (1 << 18) if self.effect is not None else 0
        flags |= (1 << 20) if self.video_timestamp is not None else 0
        flags |= (1 << 21) if self.allow_paid_stars is not None else 0
        flags |= (1 << 23) if self.suggested_post is not None else 0
        b.write(Int(flags))

        b.write(self.from_peer.write())

        b.write(Vector(self.id, Int))

        b.write(Vector(self.random_id, Long))

        b.write(self.to_peer.write())

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        if self.reply_to is not None:
            b.write(self.reply_to.write())

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

        if self.video_timestamp is not None:
            b.write(Int(self.video_timestamp))

        if self.allow_paid_stars is not None:
            b.write(Long(self.allow_paid_stars))

        if self.suggested_post is not None:
            b.write(self.suggested_post.write())

        return b.getvalue()
