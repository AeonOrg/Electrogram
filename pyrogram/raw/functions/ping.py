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


class Ping(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7ABE77EC``

    Parameters:
        ping_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`Pong <pyrogram.raw.base.Pong>`
    """

    __slots__: List[str] = ["ping_id"]

    ID = 0x7abe77ec
    QUALNAME = "functions.Ping"

    def __init__(self, *, ping_id: int) -> None:
        self.ping_id = ping_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Ping":
        # No flags

        ping_id = Long.read(b)

        return Ping(ping_id=ping_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.ping_id))

        return b.getvalue()
