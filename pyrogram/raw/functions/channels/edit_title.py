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


class EditTitle(TLObject):  # type: ignore
    """Edit the name of a channel/supergroup


    Details:
        - Layer: ``224``
        - ID: ``566DECD0``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel/supergroup

        title (``str``):
            New name

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "title"]

    ID = 0x566decd0
    QUALNAME = "functions.channels.EditTitle"

    def __init__(self, *, channel: "raw.base.InputChannel", title: str) -> None:
        self.channel = channel  # InputChannel
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditTitle":
        # No flags

        channel = TLObject.read(b)

        title = String.read(b)

        return EditTitle(channel=channel, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(String(self.title))

        return b.getvalue()
