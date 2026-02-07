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


class ChannelAdminLogEventActionStopPoll(TLObject):  # type: ignore
    """A poll was stopped

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``8F079643``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            The poll that was stopped

    """

    __slots__: List[str] = ["message"]

    ID = 0x8f079643
    QUALNAME = "types.ChannelAdminLogEventActionStopPoll"

    def __init__(self, *, message: "raw.base.Message") -> None:
        self.message = message  # Message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionStopPoll":
        # No flags

        message = TLObject.read(b)

        return ChannelAdminLogEventActionStopPoll(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.message.write())

        return b.getvalue()
