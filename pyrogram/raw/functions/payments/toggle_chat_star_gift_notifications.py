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


class ToggleChatStarGiftNotifications(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``60EAEFA1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        enabled (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "enabled"]

    ID = 0x60eaefa1
    QUALNAME = "functions.payments.ToggleChatStarGiftNotifications"

    def __init__(self, *, peer: "raw.base.InputPeer", enabled: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.enabled = enabled  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleChatStarGiftNotifications":

        flags = Int.read(b)

        enabled = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        return ToggleChatStarGiftNotifications(peer=peer, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.enabled else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        return b.getvalue()
