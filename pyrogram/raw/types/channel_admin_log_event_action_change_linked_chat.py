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


class ChannelAdminLogEventActionChangeLinkedChat(TLObject):  # type: ignore
    """The linked chat was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``50C7AC8``

    Parameters:
        prev_value (``int`` ``64-bit``):
            Previous linked chat

        new_value (``int`` ``64-bit``):
            New linked chat

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x50c7ac8
    QUALNAME = "types.ChannelAdminLogEventActionChangeLinkedChat"

    def __init__(self, *, prev_value: int, new_value: int) -> None:
        self.prev_value = prev_value  # long
        self.new_value = new_value  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeLinkedChat":
        # No flags

        prev_value = Long.read(b)

        new_value = Long.read(b)

        return ChannelAdminLogEventActionChangeLinkedChat(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.prev_value))

        b.write(Long(self.new_value))

        return b.getvalue()
