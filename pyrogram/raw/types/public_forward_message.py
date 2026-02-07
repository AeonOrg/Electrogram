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


class PublicForwardMessage(TLObject):  # type: ignore
    """Contains info about a forward of a story as a message.

    Constructor of :obj:`~pyrogram.raw.base.PublicForward`.

    Details:
        - Layer: ``224``
        - ID: ``1F2BF4A``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            Info about the message with the reposted story.

    """

    __slots__: List[str] = ["message"]

    ID = 0x1f2bf4a
    QUALNAME = "types.PublicForwardMessage"

    def __init__(self, *, message: "raw.base.Message") -> None:
        self.message = message  # Message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PublicForwardMessage":
        # No flags

        message = TLObject.read(b)

        return PublicForwardMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.message.write())

        return b.getvalue()
