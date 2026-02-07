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


class ChannelAdminLogEventActionCreateTopic(TLObject):  # type: ignore
    """A forum topic was created

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``58707D28``

    Parameters:
        topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            The forum topic that was created

    """

    __slots__: List[str] = ["topic"]

    ID = 0x58707d28
    QUALNAME = "types.ChannelAdminLogEventActionCreateTopic"

    def __init__(self, *, topic: "raw.base.ForumTopic") -> None:
        self.topic = topic  # ForumTopic

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionCreateTopic":
        # No flags

        topic = TLObject.read(b)

        return ChannelAdminLogEventActionCreateTopic(topic=topic)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.topic.write())

        return b.getvalue()
