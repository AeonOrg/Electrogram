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


class MessageReactions(TLObject):  # type: ignore
    """Message reactions »

    Constructor of :obj:`~pyrogram.raw.base.MessageReactions`.

    Details:
        - Layer: ``224``
        - ID: ``A339F0B``

    Parameters:
        results (List of :obj:`ReactionCount <pyrogram.raw.base.ReactionCount>`):
            Reactions

        min (``bool``, *optional*):
            Similar to min objects, used for message reaction » constructors that are the same for all users so they don't have the reactions sent by the current user (you can use messages.getMessagesReactions to get the full reaction info).

        can_see_list (``bool``, *optional*):
            Whether messages.getMessageReactionsList can be used to see how each specific peer reacted to the message

        reactions_as_tags (``bool``, *optional*):


        recent_reactions (List of :obj:`MessagePeerReaction <pyrogram.raw.base.MessagePeerReaction>`, *optional*):
            List of recent peers and their reactions

        top_reactors (List of :obj:`MessageReactor <pyrogram.raw.base.MessageReactor>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["results", "min", "can_see_list", "reactions_as_tags", "recent_reactions", "top_reactors"]

    ID = 0xa339f0b
    QUALNAME = "types.MessageReactions"

    def __init__(self, *, results: List["raw.base.ReactionCount"], min: Optional[bool] = None, can_see_list: Optional[bool] = None, reactions_as_tags: Optional[bool] = None, recent_reactions: Optional[List["raw.base.MessagePeerReaction"]] = None, top_reactors: Optional[List["raw.base.MessageReactor"]] = None) -> None:
        self.results = results  # Vector<ReactionCount>
        self.min = min  # flags.0?true
        self.can_see_list = can_see_list  # flags.2?true
        self.reactions_as_tags = reactions_as_tags  # flags.3?true
        self.recent_reactions = recent_reactions  # flags.1?Vector<MessagePeerReaction>
        self.top_reactors = top_reactors  # flags.4?Vector<MessageReactor>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReactions":

        flags = Int.read(b)

        min = True if flags & (1 << 0) else False
        can_see_list = True if flags & (1 << 2) else False
        reactions_as_tags = True if flags & (1 << 3) else False
        results = TLObject.read(b)

        recent_reactions = TLObject.read(b) if flags & (1 << 1) else []

        top_reactors = TLObject.read(b) if flags & (1 << 4) else []

        return MessageReactions(results=results, min=min, can_see_list=can_see_list, reactions_as_tags=reactions_as_tags, recent_reactions=recent_reactions, top_reactors=top_reactors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min else 0
        flags |= (1 << 2) if self.can_see_list else 0
        flags |= (1 << 3) if self.reactions_as_tags else 0
        flags |= (1 << 1) if self.recent_reactions else 0
        flags |= (1 << 4) if self.top_reactors else 0
        b.write(Int(flags))

        b.write(Vector(self.results))

        if self.recent_reactions is not None:
            b.write(Vector(self.recent_reactions))

        if self.top_reactors is not None:
            b.write(Vector(self.top_reactors))

        return b.getvalue()
