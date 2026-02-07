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


class CheckUsername(TLObject):  # type: ignore
    """Check if a username is free and can be assigned to a channel/supergroup


    Details:
        - Layer: ``224``
        - ID: ``10E6BD2C``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            The channel/supergroup that will assigned the specified username

        username (``str``):
            The username to check

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "username"]

    ID = 0x10e6bd2c
    QUALNAME = "functions.channels.CheckUsername"

    def __init__(self, *, channel: "raw.base.InputChannel", username: str) -> None:
        self.channel = channel  # InputChannel
        self.username = username  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckUsername":
        # No flags

        channel = TLObject.read(b)

        username = String.read(b)

        return CheckUsername(channel=channel, username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(String(self.username))

        return b.getvalue()
