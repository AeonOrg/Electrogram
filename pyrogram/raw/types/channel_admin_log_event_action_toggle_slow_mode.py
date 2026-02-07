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


class ChannelAdminLogEventActionToggleSlowMode(TLObject):  # type: ignore
    """Slow mode setting for supergroups was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``53909779``

    Parameters:
        prev_value (``int`` ``32-bit``):
            Previous slow mode value

        new_value (``int`` ``32-bit``):
            New slow mode value

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x53909779
    QUALNAME = "types.ChannelAdminLogEventActionToggleSlowMode"

    def __init__(self, *, prev_value: int, new_value: int) -> None:
        self.prev_value = prev_value  # int
        self.new_value = new_value  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionToggleSlowMode":
        # No flags

        prev_value = Int.read(b)

        new_value = Int.read(b)

        return ChannelAdminLogEventActionToggleSlowMode(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.prev_value))

        b.write(Int(self.new_value))

        return b.getvalue()
