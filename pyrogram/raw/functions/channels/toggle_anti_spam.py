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


class ToggleAntiSpam(TLObject):  # type: ignore
    """Enable or disable the native antispam system.


    Details:
        - Layer: ``224``
        - ID: ``68F3E4EB``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Supergroup ID. The specified supergroup must have at least telegram_antispam_group_size_min members to enable antispam functionality, as specified by the client configuration parameters.

        enabled (``bool``):
            Enable or disable the native antispam system.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0x68f3e4eb
    QUALNAME = "functions.channels.ToggleAntiSpam"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool) -> None:
        self.channel = channel  # InputChannel
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleAntiSpam":
        # No flags

        channel = TLObject.read(b)

        enabled = Bool.read(b)

        return ToggleAntiSpam(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Bool(self.enabled))

        return b.getvalue()
