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


class ChannelAdminLogEventActionChangeUsername(TLObject):  # type: ignore
    """Channel/supergroup username was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``6A4AFC38``

    Parameters:
        prev_value (``str``):
            Old username

        new_value (``str``):
            New username

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x6a4afc38
    QUALNAME = "types.ChannelAdminLogEventActionChangeUsername"

    def __init__(self, *, prev_value: str, new_value: str) -> None:
        self.prev_value = prev_value  # string
        self.new_value = new_value  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeUsername":
        # No flags

        prev_value = String.read(b)

        new_value = String.read(b)

        return ChannelAdminLogEventActionChangeUsername(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.prev_value))

        b.write(String(self.new_value))

        return b.getvalue()
