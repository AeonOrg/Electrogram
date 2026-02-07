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


class MessageActionPaidMessagesRefunded(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``AC1F1FCD``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        stars (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["count", "stars"]

    ID = 0xac1f1fcd
    QUALNAME = "types.MessageActionPaidMessagesRefunded"

    def __init__(self, *, count: int, stars: int) -> None:
        self.count = count  # int
        self.stars = stars  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaidMessagesRefunded":
        # No flags

        count = Int.read(b)

        stars = Long.read(b)

        return MessageActionPaidMessagesRefunded(count=count, stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.count))

        b.write(Long(self.stars))

        return b.getvalue()
