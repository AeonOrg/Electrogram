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


class SetCustomVerification(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8B89DFBD``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        enabled (``bool``, *optional*):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

        custom_description (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "enabled", "bot", "custom_description"]

    ID = 0x8b89dfbd
    QUALNAME = "functions.bots.SetCustomVerification"

    def __init__(self, *, peer: "raw.base.InputPeer", enabled: Optional[bool] = None, bot: "raw.base.InputUser" = None, custom_description: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.enabled = enabled  # flags.1?true
        self.bot = bot  # flags.0?InputUser
        self.custom_description = custom_description  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetCustomVerification":

        flags = Int.read(b)

        enabled = True if flags & (1 << 1) else False
        bot = TLObject.read(b) if flags & (1 << 0) else None

        peer = TLObject.read(b)

        custom_description = String.read(b) if flags & (1 << 2) else None
        return SetCustomVerification(peer=peer, enabled=enabled, bot=bot, custom_description=custom_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.enabled else 0
        flags |= (1 << 0) if self.bot is not None else 0
        flags |= (1 << 2) if self.custom_description is not None else 0
        b.write(Int(flags))

        if self.bot is not None:
            b.write(self.bot.write())

        b.write(self.peer.write())

        if self.custom_description is not None:
            b.write(String(self.custom_description))

        return b.getvalue()
