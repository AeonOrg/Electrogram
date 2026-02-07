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


class ChannelMessagesFilter(TLObject):  # type: ignore
    """Filter for getting only certain types of channel messages

    Constructor of :obj:`~pyrogram.raw.base.ChannelMessagesFilter`.

    Details:
        - Layer: ``224``
        - ID: ``CD77D957``

    Parameters:
        ranges (List of :obj:`MessageRange <pyrogram.raw.base.MessageRange>`):
            A range of messages to fetch

        exclude_new_messages (``bool``, *optional*):
            Whether to exclude new messages from the search

    """

    __slots__: List[str] = ["ranges", "exclude_new_messages"]

    ID = 0xcd77d957
    QUALNAME = "types.ChannelMessagesFilter"

    def __init__(self, *, ranges: List["raw.base.MessageRange"], exclude_new_messages: Optional[bool] = None) -> None:
        self.ranges = ranges  # Vector<MessageRange>
        self.exclude_new_messages = exclude_new_messages  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelMessagesFilter":

        flags = Int.read(b)

        exclude_new_messages = True if flags & (1 << 1) else False
        ranges = TLObject.read(b)

        return ChannelMessagesFilter(ranges=ranges, exclude_new_messages=exclude_new_messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.exclude_new_messages else 0
        b.write(Int(flags))

        b.write(Vector(self.ranges))

        return b.getvalue()
