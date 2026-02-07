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


class ChannelAdminLogEventActionToggleInvites(TLObject):  # type: ignore
    """Invites were enabled/disabled

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``1B7907AE``

    Parameters:
        new_value (``bool``):
            New value

    """

    __slots__: List[str] = ["new_value"]

    ID = 0x1b7907ae
    QUALNAME = "types.ChannelAdminLogEventActionToggleInvites"

    def __init__(self, *, new_value: bool) -> None:
        self.new_value = new_value  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionToggleInvites":
        # No flags

        new_value = Bool.read(b)

        return ChannelAdminLogEventActionToggleInvites(new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bool(self.new_value))

        return b.getvalue()
