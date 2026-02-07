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


class TogglePreHistoryHidden(TLObject):  # type: ignore
    """Hide/unhide message history for new channel/supergroup users


    Details:
        - Layer: ``224``
        - ID: ``EABBB94C``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Channel/supergroup

        enabled (``bool``):
            Hide/unhide

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0xeabbb94c
    QUALNAME = "functions.channels.TogglePreHistoryHidden"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool) -> None:
        self.channel = channel  # InputChannel
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TogglePreHistoryHidden":
        # No flags

        channel = TLObject.read(b)

        enabled = Bool.read(b)

        return TogglePreHistoryHidden(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Bool(self.enabled))

        return b.getvalue()
