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


class MessageActionTTLChange(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``55555552``

    Parameters:
        ttl (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["ttl"]

    ID = 0x55555552
    QUALNAME = "types.MessageActionTTLChange"

    def __init__(self, *, ttl: int) -> None:
        self.ttl = ttl  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTTLChange":
        # No flags

        ttl = Int.read(b)

        return MessageActionTTLChange(ttl=ttl)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.ttl))

        return b.getvalue()
