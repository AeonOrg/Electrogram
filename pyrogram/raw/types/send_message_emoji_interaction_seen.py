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


class SendMessageEmojiInteractionSeen(TLObject):  # type: ignore
    """User is watching an animated emoji reaction triggered by another user, click here for more info ».

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``B665902E``

    Parameters:
        emoticon (``str``):
            Emoji

    """

    __slots__: List[str] = ["emoticon"]

    ID = 0xb665902e
    QUALNAME = "types.SendMessageEmojiInteractionSeen"

    def __init__(self, *, emoticon: str) -> None:
        self.emoticon = emoticon  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageEmojiInteractionSeen":
        # No flags

        emoticon = String.read(b)

        return SendMessageEmojiInteractionSeen(emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.emoticon))

        return b.getvalue()
