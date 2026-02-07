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


class ChannelAdminLogEventActionToggleAntiSpam(TLObject):  # type: ignore
    """Native antispam functionality was enabled or disabled.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``64F36DFC``

    Parameters:
        new_value (``bool``):
            Whether antispam functionality was enabled or disabled.

    """

    __slots__: List[str] = ["new_value"]

    ID = 0x64f36dfc
    QUALNAME = "types.ChannelAdminLogEventActionToggleAntiSpam"

    def __init__(self, *, new_value: bool) -> None:
        self.new_value = new_value  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionToggleAntiSpam":
        # No flags

        new_value = Bool.read(b)

        return ChannelAdminLogEventActionToggleAntiSpam(new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bool(self.new_value))

        return b.getvalue()
