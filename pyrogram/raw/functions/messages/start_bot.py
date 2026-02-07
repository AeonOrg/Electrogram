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


class StartBot(TLObject):  # type: ignore
    """Start a conversation with a bot using a deep linking parameter


    Details:
        - Layer: ``224``
        - ID: ``E6DF7378``

    Parameters:
        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            The bot

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The chat where to start the bot, can be the bot's private chat or a group

        random_id (``int`` ``64-bit``):
            Random ID to avoid resending the same message

        start_param (``str``):
            Deep linking parameter

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["bot", "peer", "random_id", "start_param"]

    ID = 0xe6df7378
    QUALNAME = "functions.messages.StartBot"

    def __init__(self, *, bot: "raw.base.InputUser", peer: "raw.base.InputPeer", random_id: int, start_param: str) -> None:
        self.bot = bot  # InputUser
        self.peer = peer  # InputPeer
        self.random_id = random_id  # long
        self.start_param = start_param  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartBot":
        # No flags

        bot = TLObject.read(b)

        peer = TLObject.read(b)

        random_id = Long.read(b)

        start_param = String.read(b)

        return StartBot(bot=bot, peer=peer, random_id=random_id, start_param=start_param)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.bot.write())

        b.write(self.peer.write())

        b.write(Long(self.random_id))

        b.write(String(self.start_param))

        return b.getvalue()
