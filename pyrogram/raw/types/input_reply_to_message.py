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


class InputReplyToMessage(TLObject):  # type: ignore
    """Reply to a message.

    Constructor of :obj:`~pyrogram.raw.base.InputReplyTo`.

    Details:
        - Layer: ``224``
        - ID: ``869FBE10``

    Parameters:
        reply_to_msg_id (``int`` ``32-bit``):
            The message ID to reply to.

        top_msg_id (``int`` ``32-bit``, *optional*):
            This field must contain the topic ID only when replying to messages in forum topics different from the "General" topic (i.e. reply_to_msg_id is set and reply_to_msg_id != topicID and topicID != 1).  If the replied-to message is deleted before the method finishes execution, the value in this field will be used to send the message to the correct topic, instead of the "General" topic.

        reply_to_peer_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Used to reply to messages sent to another chat (specified here), can only be used for non-protected chats and messages.

        quote_text (``str``, *optional*):
            Used to quote-reply to only a certain section (specified here) of the original message. The maximum UTF-8 length for quotes is specified in the quote_length_max config key.

        quote_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text from the quote_text field.

        quote_offset (``int`` ``32-bit``, *optional*):
            Offset of the message quote_text within the original message (in UTF-16 code units).

        monoforum_peer_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        todo_item_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["reply_to_msg_id", "top_msg_id", "reply_to_peer_id", "quote_text", "quote_entities", "quote_offset", "monoforum_peer_id", "todo_item_id"]

    ID = 0x869fbe10
    QUALNAME = "types.InputReplyToMessage"

    def __init__(self, *, reply_to_msg_id: int, top_msg_id: Optional[int] = None, reply_to_peer_id: "raw.base.InputPeer" = None, quote_text: Optional[str] = None, quote_entities: Optional[List["raw.base.MessageEntity"]] = None, quote_offset: Optional[int] = None, monoforum_peer_id: "raw.base.InputPeer" = None, todo_item_id: Optional[int] = None) -> None:
        self.reply_to_msg_id = reply_to_msg_id  # int
        self.top_msg_id = top_msg_id  # flags.0?int
        self.reply_to_peer_id = reply_to_peer_id  # flags.1?InputPeer
        self.quote_text = quote_text  # flags.2?string
        self.quote_entities = quote_entities  # flags.3?Vector<MessageEntity>
        self.quote_offset = quote_offset  # flags.4?int
        self.monoforum_peer_id = monoforum_peer_id  # flags.5?InputPeer
        self.todo_item_id = todo_item_id  # flags.6?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReplyToMessage":

        flags = Int.read(b)

        reply_to_msg_id = Int.read(b)

        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        reply_to_peer_id = TLObject.read(b) if flags & (1 << 1) else None

        quote_text = String.read(b) if flags & (1 << 2) else None
        quote_entities = TLObject.read(b) if flags & (1 << 3) else []

        quote_offset = Int.read(b) if flags & (1 << 4) else None
        monoforum_peer_id = TLObject.read(b) if flags & (1 << 5) else None

        todo_item_id = Int.read(b) if flags & (1 << 6) else None
        return InputReplyToMessage(reply_to_msg_id=reply_to_msg_id, top_msg_id=top_msg_id, reply_to_peer_id=reply_to_peer_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset, monoforum_peer_id=monoforum_peer_id, todo_item_id=todo_item_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        flags |= (1 << 1) if self.reply_to_peer_id is not None else 0
        flags |= (1 << 2) if self.quote_text is not None else 0
        flags |= (1 << 3) if self.quote_entities else 0
        flags |= (1 << 4) if self.quote_offset is not None else 0
        flags |= (1 << 5) if self.monoforum_peer_id is not None else 0
        flags |= (1 << 6) if self.todo_item_id is not None else 0
        b.write(Int(flags))

        b.write(Int(self.reply_to_msg_id))

        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))

        if self.reply_to_peer_id is not None:
            b.write(self.reply_to_peer_id.write())

        if self.quote_text is not None:
            b.write(String(self.quote_text))

        if self.quote_entities is not None:
            b.write(Vector(self.quote_entities))

        if self.quote_offset is not None:
            b.write(Int(self.quote_offset))

        if self.monoforum_peer_id is not None:
            b.write(self.monoforum_peer_id.write())

        if self.todo_item_id is not None:
            b.write(Int(self.todo_item_id))

        return b.getvalue()
