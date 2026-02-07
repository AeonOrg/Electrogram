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


class ChannelAdminLogEventActionTogglePreHistoryHidden(TLObject):  # type: ignore
    """The hidden prehistory setting was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``5F5C95F1``

    Parameters:
        new_value (``bool``):
            New value

    """

    __slots__: List[str] = ["new_value"]

    ID = 0x5f5c95f1
    QUALNAME = "types.ChannelAdminLogEventActionTogglePreHistoryHidden"

    def __init__(self, *, new_value: bool) -> None:
        self.new_value = new_value  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionTogglePreHistoryHidden":
        # No flags

        new_value = Bool.read(b)

        return ChannelAdminLogEventActionTogglePreHistoryHidden(new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bool(self.new_value))

        return b.getvalue()
