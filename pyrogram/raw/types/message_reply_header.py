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


class MessageReplyHeader(TLObject):  # type: ignore
    """Message replies and thread information

    Constructor of :obj:`~pyrogram.raw.base.MessageReplyHeader`.

    Details:
        - Layer: ``224``
        - ID: ``6917560B``

    Parameters:
        reply_to_scheduled (``bool``, *optional*):
            This is a reply to a scheduled message.

        forum_topic (``bool``, *optional*):
            Whether this message was sent in a forum topic (except for the General topic).

        quote (``bool``, *optional*):
            Whether this message is quoting a part of another message.

        reply_to_msg_id (``int`` ``32-bit``, *optional*):
            ID of message to which this message is replying

        reply_to_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            For replies sent in channel discussion threads of which the current user is not a member, the discussion group ID

        reply_from (:obj:`MessageFwdHeader <pyrogram.raw.base.MessageFwdHeader>`, *optional*):
            When replying to a message sent by a certain peer to another chat, contains info about the peer that originally sent the message to that other chat.

        reply_media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`, *optional*):
            When replying to a media sent by a certain peer to another chat, contains the media of the replied-to message.

        reply_to_top_id (``int`` ``32-bit``, *optional*):
            ID of the message that started this message thread

        quote_text (``str``, *optional*):
            Used to quote-reply to only a certain section (specified here) of the original message.

        quote_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text from the quote_text field.

        quote_offset (``int`` ``32-bit``, *optional*):
            Offset of the message quote_text within the original message (in UTF-16 code units).

        todo_item_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["reply_to_scheduled", "forum_topic", "quote", "reply_to_msg_id", "reply_to_peer_id", "reply_from", "reply_media", "reply_to_top_id", "quote_text", "quote_entities", "quote_offset", "todo_item_id"]

    ID = 0x6917560b
    QUALNAME = "types.MessageReplyHeader"

    def __init__(self, *, reply_to_scheduled: Optional[bool] = None, forum_topic: Optional[bool] = None, quote: Optional[bool] = None, reply_to_msg_id: Optional[int] = None, reply_to_peer_id: "raw.base.Peer" = None, reply_from: "raw.base.MessageFwdHeader" = None, reply_media: "raw.base.MessageMedia" = None, reply_to_top_id: Optional[int] = None, quote_text: Optional[str] = None, quote_entities: Optional[List["raw.base.MessageEntity"]] = None, quote_offset: Optional[int] = None, todo_item_id: Optional[int] = None) -> None:
        self.reply_to_scheduled = reply_to_scheduled  # flags.2?true
        self.forum_topic = forum_topic  # flags.3?true
        self.quote = quote  # flags.9?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.4?int
        self.reply_to_peer_id = reply_to_peer_id  # flags.0?Peer
        self.reply_from = reply_from  # flags.5?MessageFwdHeader
        self.reply_media = reply_media  # flags.8?MessageMedia
        self.reply_to_top_id = reply_to_top_id  # flags.1?int
        self.quote_text = quote_text  # flags.6?string
        self.quote_entities = quote_entities  # flags.7?Vector<MessageEntity>
        self.quote_offset = quote_offset  # flags.10?int
        self.todo_item_id = todo_item_id  # flags.11?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReplyHeader":

        flags = Int.read(b)

        reply_to_scheduled = True if flags & (1 << 2) else False
        forum_topic = True if flags & (1 << 3) else False
        quote = True if flags & (1 << 9) else False
        reply_to_msg_id = Int.read(b) if flags & (1 << 4) else None
        reply_to_peer_id = TLObject.read(b) if flags & (1 << 0) else None

        reply_from = TLObject.read(b) if flags & (1 << 5) else None

        reply_media = TLObject.read(b) if flags & (1 << 8) else None

        reply_to_top_id = Int.read(b) if flags & (1 << 1) else None
        quote_text = String.read(b) if flags & (1 << 6) else None
        quote_entities = TLObject.read(b) if flags & (1 << 7) else []

        quote_offset = Int.read(b) if flags & (1 << 10) else None
        todo_item_id = Int.read(b) if flags & (1 << 11) else None
        return MessageReplyHeader(reply_to_scheduled=reply_to_scheduled, forum_topic=forum_topic, quote=quote, reply_to_msg_id=reply_to_msg_id, reply_to_peer_id=reply_to_peer_id, reply_from=reply_from, reply_media=reply_media, reply_to_top_id=reply_to_top_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset, todo_item_id=todo_item_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_to_scheduled else 0
        flags |= (1 << 3) if self.forum_topic else 0
        flags |= (1 << 9) if self.quote else 0
        flags |= (1 << 4) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 0) if self.reply_to_peer_id is not None else 0
        flags |= (1 << 5) if self.reply_from is not None else 0
        flags |= (1 << 8) if self.reply_media is not None else 0
        flags |= (1 << 1) if self.reply_to_top_id is not None else 0
        flags |= (1 << 6) if self.quote_text is not None else 0
        flags |= (1 << 7) if self.quote_entities else 0
        flags |= (1 << 10) if self.quote_offset is not None else 0
        flags |= (1 << 11) if self.todo_item_id is not None else 0
        b.write(Int(flags))

        if self.reply_to_msg_id is not None:
            b.write(Int(self.reply_to_msg_id))

        if self.reply_to_peer_id is not None:
            b.write(self.reply_to_peer_id.write())

        if self.reply_from is not None:
            b.write(self.reply_from.write())

        if self.reply_media is not None:
            b.write(self.reply_media.write())

        if self.reply_to_top_id is not None:
            b.write(Int(self.reply_to_top_id))

        if self.quote_text is not None:
            b.write(String(self.quote_text))

        if self.quote_entities is not None:
            b.write(Vector(self.quote_entities))

        if self.quote_offset is not None:
            b.write(Int(self.quote_offset))

        if self.todo_item_id is not None:
            b.write(Int(self.todo_item_id))

        return b.getvalue()
