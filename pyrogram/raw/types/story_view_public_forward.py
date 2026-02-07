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


class StoryViewPublicForward(TLObject):  # type: ignore
    """A certain peer has forwarded the story as a message to a public chat or channel.

    Constructor of :obj:`~pyrogram.raw.base.StoryView`.

    Details:
        - Layer: ``224``
        - ID: ``9083670B``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            The message with the forwarded story.

        blocked (``bool``, *optional*):
            Whether we have completely blocked this user, including from viewing more of our stories.

        blocked_my_stories_from (``bool``, *optional*):
            Whether we have blocked this user from viewing more of our stories.

    """

    __slots__: List[str] = ["message", "blocked", "blocked_my_stories_from"]

    ID = 0x9083670b
    QUALNAME = "types.StoryViewPublicForward"

    def __init__(self, *, message: "raw.base.Message", blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None) -> None:
        self.message = message  # Message
        self.blocked = blocked  # flags.0?true
        self.blocked_my_stories_from = blocked_my_stories_from  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViewPublicForward":

        flags = Int.read(b)

        blocked = True if flags & (1 << 0) else False
        blocked_my_stories_from = True if flags & (1 << 1) else False
        message = TLObject.read(b)

        return StoryViewPublicForward(message=message, blocked=blocked, blocked_my_stories_from=blocked_my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 1) if self.blocked_my_stories_from else 0
        b.write(Int(flags))

        b.write(self.message.write())

        return b.getvalue()
