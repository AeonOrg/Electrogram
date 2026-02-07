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


class ChannelAdminLogEventActionDeleteMessage(TLObject):  # type: ignore
    """A message was deleted

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``42E047BB``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            The message that was deleted

    """

    __slots__: List[str] = ["message"]

    ID = 0x42e047bb
    QUALNAME = "types.ChannelAdminLogEventActionDeleteMessage"

    def __init__(self, *, message: "raw.base.Message") -> None:
        self.message = message  # Message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionDeleteMessage":
        # No flags

        message = TLObject.read(b)

        return ChannelAdminLogEventActionDeleteMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.message.write())

        return b.getvalue()
