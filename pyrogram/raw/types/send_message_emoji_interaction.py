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


class SendMessageEmojiInteraction(TLObject):  # type: ignore
    """User has clicked on an animated emoji triggering a reaction, click here for more info ».

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``25972BCB``

    Parameters:
        emoticon (``str``):
            Emoji

        msg_id (``int`` ``32-bit``):
            Message ID of the animated emoji that was clicked

        interaction (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            A JSON object with interaction info, click here for more info »

    """

    __slots__: List[str] = ["emoticon", "msg_id", "interaction"]

    ID = 0x25972bcb
    QUALNAME = "types.SendMessageEmojiInteraction"

    def __init__(self, *, emoticon: str, msg_id: int, interaction: "raw.base.DataJSON") -> None:
        self.emoticon = emoticon  # string
        self.msg_id = msg_id  # int
        self.interaction = interaction  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageEmojiInteraction":
        # No flags

        emoticon = String.read(b)

        msg_id = Int.read(b)

        interaction = TLObject.read(b)

        return SendMessageEmojiInteraction(emoticon=emoticon, msg_id=msg_id, interaction=interaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.emoticon))

        b.write(Int(self.msg_id))

        b.write(self.interaction.write())

        return b.getvalue()
