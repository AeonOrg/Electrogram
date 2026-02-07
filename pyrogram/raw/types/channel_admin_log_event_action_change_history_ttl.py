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


class ChannelAdminLogEventActionChangeHistoryTTL(TLObject):  # type: ignore
    """The Time-To-Live of messages in this chat was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``6E941A38``

    Parameters:
        prev_value (``int`` ``32-bit``):
            Previous value

        new_value (``int`` ``32-bit``):
            New value

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x6e941a38
    QUALNAME = "types.ChannelAdminLogEventActionChangeHistoryTTL"

    def __init__(self, *, prev_value: int, new_value: int) -> None:
        self.prev_value = prev_value  # int
        self.new_value = new_value  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeHistoryTTL":
        # No flags

        prev_value = Int.read(b)

        new_value = Int.read(b)

        return ChannelAdminLogEventActionChangeHistoryTTL(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.prev_value))

        b.write(Int(self.new_value))

        return b.getvalue()
