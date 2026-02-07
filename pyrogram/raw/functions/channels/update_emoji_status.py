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


class UpdateEmojiStatus(TLObject):  # type: ignore
    """Set an emoji status for a channel.


    Details:
        - Layer: ``224``
        - ID: ``F0D3E6A8``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            The channel, must have at least channel_emoji_status_level_min boosts.

        emoji_status (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`):
            Emoji status to set

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "emoji_status"]

    ID = 0xf0d3e6a8
    QUALNAME = "functions.channels.UpdateEmojiStatus"

    def __init__(self, *, channel: "raw.base.InputChannel", emoji_status: "raw.base.EmojiStatus") -> None:
        self.channel = channel  # InputChannel
        self.emoji_status = emoji_status  # EmojiStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEmojiStatus":
        # No flags

        channel = TLObject.read(b)

        emoji_status = TLObject.read(b)

        return UpdateEmojiStatus(channel=channel, emoji_status=emoji_status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(self.emoji_status.write())

        return b.getvalue()
