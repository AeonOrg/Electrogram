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


class PingDelayDisconnect(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F3427B8C``

    Parameters:
        ping_id (``int`` ``64-bit``):
            N/A

        disconnect_delay (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`Pong <pyrogram.raw.base.Pong>`
    """

    __slots__: List[str] = ["ping_id", "disconnect_delay"]

    ID = 0xf3427b8c
    QUALNAME = "functions.PingDelayDisconnect"

    def __init__(self, *, ping_id: int, disconnect_delay: int) -> None:
        self.ping_id = ping_id  # long
        self.disconnect_delay = disconnect_delay  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PingDelayDisconnect":
        # No flags

        ping_id = Long.read(b)

        disconnect_delay = Int.read(b)

        return PingDelayDisconnect(ping_id=ping_id, disconnect_delay=disconnect_delay)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.ping_id))

        b.write(Int(self.disconnect_delay))

        return b.getvalue()
