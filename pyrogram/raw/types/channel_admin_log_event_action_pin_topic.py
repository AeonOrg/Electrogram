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


class ChannelAdminLogEventActionPinTopic(TLObject):  # type: ignore
    """A forum topic was pinned or unpinned

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``5D8D353B``

    Parameters:
        prev_topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`, *optional*):
            Previous topic information

        new_topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`, *optional*):
            New topic information

    """

    __slots__: List[str] = ["prev_topic", "new_topic"]

    ID = 0x5d8d353b
    QUALNAME = "types.ChannelAdminLogEventActionPinTopic"

    def __init__(self, *, prev_topic: "raw.base.ForumTopic" = None, new_topic: "raw.base.ForumTopic" = None) -> None:
        self.prev_topic = prev_topic  # flags.0?ForumTopic
        self.new_topic = new_topic  # flags.1?ForumTopic

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionPinTopic":

        flags = Int.read(b)

        prev_topic = TLObject.read(b) if flags & (1 << 0) else None

        new_topic = TLObject.read(b) if flags & (1 << 1) else None

        return ChannelAdminLogEventActionPinTopic(prev_topic=prev_topic, new_topic=new_topic)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.prev_topic is not None else 0
        flags |= (1 << 1) if self.new_topic is not None else 0
        b.write(Int(flags))

        if self.prev_topic is not None:
            b.write(self.prev_topic.write())

        if self.new_topic is not None:
            b.write(self.new_topic.write())

        return b.getvalue()
