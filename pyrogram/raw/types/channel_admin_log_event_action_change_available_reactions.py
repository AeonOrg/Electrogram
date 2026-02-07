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


class ChannelAdminLogEventActionChangeAvailableReactions(TLObject):  # type: ignore
    """The set of allowed message reactions » for this channel has changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``BE4E0EF8``

    Parameters:
        prev_value (:obj:`ChatReactions <pyrogram.raw.base.ChatReactions>`):
            Previously allowed reaction emojis

        new_value (:obj:`ChatReactions <pyrogram.raw.base.ChatReactions>`):
            New allowed reaction emojis

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0xbe4e0ef8
    QUALNAME = "types.ChannelAdminLogEventActionChangeAvailableReactions"

    def __init__(self, *, prev_value: "raw.base.ChatReactions", new_value: "raw.base.ChatReactions") -> None:
        self.prev_value = prev_value  # ChatReactions
        self.new_value = new_value  # ChatReactions

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeAvailableReactions":
        # No flags

        prev_value = TLObject.read(b)

        new_value = TLObject.read(b)

        return ChannelAdminLogEventActionChangeAvailableReactions(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.prev_value.write())

        b.write(self.new_value.write())

        return b.getvalue()
