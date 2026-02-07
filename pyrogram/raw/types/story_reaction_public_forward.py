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


class StoryReactionPublicForward(TLObject):  # type: ignore
    """A certain peer has forwarded the story as a message to a public chat or channel.

    Constructor of :obj:`~pyrogram.raw.base.StoryReaction`.

    Details:
        - Layer: ``224``
        - ID: ``BBAB2643``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            The message with the forwarded story.

    """

    __slots__: List[str] = ["message"]

    ID = 0xbbab2643
    QUALNAME = "types.StoryReactionPublicForward"

    def __init__(self, *, message: "raw.base.Message") -> None:
        self.message = message  # Message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryReactionPublicForward":
        # No flags

        message = TLObject.read(b)

        return StoryReactionPublicForward(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.message.write())

        return b.getvalue()
