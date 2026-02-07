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


class MessageService(TLObject):  # type: ignore
    """Indicates a service message

    Constructor of :obj:`~pyrogram.raw.base.Message`.

    Details:
        - Layer: ``224``
        - ID: ``7A800E0A``

    Parameters:
        id (``int`` ``32-bit``):
            Message ID

        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Sender of service message

        date (``int`` ``32-bit``):
            Message date

        action (:obj:`MessageAction <pyrogram.raw.base.MessageAction>`):
            Event connected with the service message

        out (``bool``, *optional*):
            Whether the message is outgoing

        mentioned (``bool``, *optional*):
            Whether we were mentioned in the message

        media_unread (``bool``, *optional*):
            Whether the message contains unread media

        reactions_are_possible (``bool``, *optional*):
            N/A

        silent (``bool``, *optional*):
            Whether the message is silent

        post (``bool``, *optional*):
            Whether it's a channel post

        legacy (``bool``, *optional*):
            This is a legacy message: it has to be refetched with the new layer

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            ID of the sender of this message

        saved_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        reply_to (:obj:`MessageReplyHeader <pyrogram.raw.base.MessageReplyHeader>`, *optional*):
            Reply (thread) information

        reactions (:obj:`MessageReactions <pyrogram.raw.base.MessageReactions>`, *optional*):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            Time To Live of the message, once message.date+message.ttl_period === time(), the message will be deleted on the server, and must be deleted locally as well.

    """

    __slots__: List[str] = ["id", "peer_id", "date", "action", "out", "mentioned", "media_unread", "reactions_are_possible", "silent", "post", "legacy", "from_id", "saved_peer_id", "reply_to", "reactions", "ttl_period"]

    ID = 0x7a800e0a
    QUALNAME = "types.MessageService"

    def __init__(self, *, id: int, peer_id: "raw.base.Peer", date: int, action: "raw.base.MessageAction", out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, reactions_are_possible: Optional[bool] = None, silent: Optional[bool] = None, post: Optional[bool] = None, legacy: Optional[bool] = None, from_id: "raw.base.Peer" = None, saved_peer_id: "raw.base.Peer" = None, reply_to: "raw.base.MessageReplyHeader" = None, reactions: "raw.base.MessageReactions" = None, ttl_period: Optional[int] = None) -> None:
        self.id = id  # int
        self.peer_id = peer_id  # Peer
        self.date = date  # int
        self.action = action  # MessageAction
        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.reactions_are_possible = reactions_are_possible  # flags.9?true
        self.silent = silent  # flags.13?true
        self.post = post  # flags.14?true
        self.legacy = legacy  # flags.19?true
        self.from_id = from_id  # flags.8?Peer
        self.saved_peer_id = saved_peer_id  # flags.28?Peer
        self.reply_to = reply_to  # flags.3?MessageReplyHeader
        self.reactions = reactions  # flags.20?MessageReactions
        self.ttl_period = ttl_period  # flags.25?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageService":

        flags = Int.read(b)

        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        reactions_are_possible = True if flags & (1 << 9) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        legacy = True if flags & (1 << 19) else False
        id = Int.read(b)

        from_id = TLObject.read(b) if flags & (1 << 8) else None

        peer_id = TLObject.read(b)

        saved_peer_id = TLObject.read(b) if flags & (1 << 28) else None

        reply_to = TLObject.read(b) if flags & (1 << 3) else None

        date = Int.read(b)

        action = TLObject.read(b)

        reactions = TLObject.read(b) if flags & (1 << 20) else None

        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return MessageService(id=id, peer_id=peer_id, date=date, action=action, out=out, mentioned=mentioned, media_unread=media_unread, reactions_are_possible=reactions_are_possible, silent=silent, post=post, legacy=legacy, from_id=from_id, saved_peer_id=saved_peer_id, reply_to=reply_to, reactions=reactions, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out else 0
        flags |= (1 << 4) if self.mentioned else 0
        flags |= (1 << 5) if self.media_unread else 0
        flags |= (1 << 9) if self.reactions_are_possible else 0
        flags |= (1 << 13) if self.silent else 0
        flags |= (1 << 14) if self.post else 0
        flags |= (1 << 19) if self.legacy else 0
        flags |= (1 << 8) if self.from_id is not None else 0
        flags |= (1 << 28) if self.saved_peer_id is not None else 0
        flags |= (1 << 3) if self.reply_to is not None else 0
        flags |= (1 << 20) if self.reactions is not None else 0
        flags |= (1 << 25) if self.ttl_period is not None else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        if self.from_id is not None:
            b.write(self.from_id.write())

        b.write(self.peer_id.write())

        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())

        if self.reply_to is not None:
            b.write(self.reply_to.write())

        b.write(Int(self.date))

        b.write(self.action.write())

        if self.reactions is not None:
            b.write(self.reactions.write())

        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))

        return b.getvalue()
