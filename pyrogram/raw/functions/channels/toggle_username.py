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


class ToggleUsername(TLObject):  # type: ignore
    """Activate or deactivate a purchased fragment.com username associated to a supergroup or channel we own.


    Details:
        - Layer: ``224``
        - ID: ``50F24105``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Supergroup or channel

        username (``str``):
            Username

        active (``bool``):
            Whether to activate or deactivate the username

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "username", "active"]

    ID = 0x50f24105
    QUALNAME = "functions.channels.ToggleUsername"

    def __init__(self, *, channel: "raw.base.InputChannel", username: str, active: bool) -> None:
        self.channel = channel  # InputChannel
        self.username = username  # string
        self.active = active  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleUsername":
        # No flags

        channel = TLObject.read(b)

        username = String.read(b)

        active = Bool.read(b)

        return ToggleUsername(channel=channel, username=username, active=active)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(String(self.username))

        b.write(Bool(self.active))

        return b.getvalue()
