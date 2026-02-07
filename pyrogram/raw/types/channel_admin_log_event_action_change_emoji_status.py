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


class ChannelAdminLogEventActionChangeEmojiStatus(TLObject):  # type: ignore
    """The emoji status was changed

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``3EA9FEB1``

    Parameters:
        prev_value (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`):
            Previous emoji status

        new_value (:obj:`EmojiStatus <pyrogram.raw.base.EmojiStatus>`):
            New emoji status

    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x3ea9feb1
    QUALNAME = "types.ChannelAdminLogEventActionChangeEmojiStatus"

    def __init__(self, *, prev_value: "raw.base.EmojiStatus", new_value: "raw.base.EmojiStatus") -> None:
        self.prev_value = prev_value  # EmojiStatus
        self.new_value = new_value  # EmojiStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeEmojiStatus":
        # No flags

        prev_value = TLObject.read(b)

        new_value = TLObject.read(b)

        return ChannelAdminLogEventActionChangeEmojiStatus(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.prev_value.write())

        b.write(self.new_value.write())

        return b.getvalue()
