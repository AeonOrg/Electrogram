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


class ChannelAdminLogEventActionChangeUsernames(TLObject):  # type: ignore
    """The list of usernames associated with the channel was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``F04FB3A9``

    Parameters:
        prev_value (List of ``str``):
            Previous set of usernames

        new_value (List of ``str``):
            New set of usernames

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0xf04fb3a9
    QUALNAME = "types.ChannelAdminLogEventActionChangeUsernames"

    def __init__(self, *, prev_value: List[str], new_value: List[str]) -> None:
        self.prev_value = prev_value  # Vector<string>
        self.new_value = new_value  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeUsernames":
        # No flags

        prev_value = TLObject.read(b, String)

        new_value = TLObject.read(b, String)

        return ChannelAdminLogEventActionChangeUsernames(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.prev_value, String))

        b.write(Vector(self.new_value, String))

        return b.getvalue()
