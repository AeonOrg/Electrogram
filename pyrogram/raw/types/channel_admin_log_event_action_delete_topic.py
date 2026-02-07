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


class ChannelAdminLogEventActionDeleteTopic(TLObject):  # type: ignore
    """A forum topic was deleted

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``AE168909``

    Parameters:
        topic (:obj:`ForumTopic <pyrogram.raw.base.ForumTopic>`):
            The forum topic that was deleted

    """

    __slots__: List[str] = ["topic"]

    ID = 0xae168909
    QUALNAME = "types.ChannelAdminLogEventActionDeleteTopic"

    def __init__(self, *, topic: "raw.base.ForumTopic") -> None:
        self.topic = topic  # ForumTopic

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionDeleteTopic":
        # No flags

        topic = TLObject.read(b)

        return ChannelAdminLogEventActionDeleteTopic(topic=topic)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.topic.write())

        return b.getvalue()
