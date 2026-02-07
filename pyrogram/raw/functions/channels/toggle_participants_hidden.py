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


class ToggleParticipantsHidden(TLObject):  # type: ignore
    """Hide or display the participants list in a supergroup.


    Details:
        - Layer: ``224``
        - ID: ``6A6E7854``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Supergroup ID

        enabled (``bool``):
            If true, will hide the participants list; otherwise will unhide it.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0x6a6e7854
    QUALNAME = "functions.channels.ToggleParticipantsHidden"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool) -> None:
        self.channel = channel  # InputChannel
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleParticipantsHidden":
        # No flags

        channel = TLObject.read(b)

        enabled = Bool.read(b)

        return ToggleParticipantsHidden(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Bool(self.enabled))

        return b.getvalue()
