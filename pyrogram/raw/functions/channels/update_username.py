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


class UpdateUsername(TLObject):  # type: ignore
    """Change or remove the username of a supergroup/channel


    Details:
        - Layer: ``224``
        - ID: ``3514B3DE``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel

        username (``str``):
            New username, pass an empty string to remove the username

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "username"]

    ID = 0x3514b3de
    QUALNAME = "functions.channels.UpdateUsername"

    def __init__(self, *, channel: "raw.base.InputChannel", username: str) -> None:
        self.channel = channel  # InputChannel
        self.username = username  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUsername":
        # No flags

        channel = TLObject.read(b)

        username = String.read(b)

        return UpdateUsername(channel=channel, username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(String(self.username))

        return b.getvalue()
