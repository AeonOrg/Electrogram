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


class ReportAntiSpamFalsePositive(TLObject):  # type: ignore
    """Report a native antispam false positive


    Details:
        - Layer: ``224``
        - ID: ``A850A693``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            Supergroup ID

        msg_id (``int`` ``32-bit``):
            Message ID that was mistakenly deleted by the native antispam system, taken from the admin log

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "msg_id"]

    ID = 0xa850a693
    QUALNAME = "functions.channels.ReportAntiSpamFalsePositive"

    def __init__(self, *, channel: "raw.base.InputChannel", msg_id: int) -> None:
        self.channel = channel  # InputChannel
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportAntiSpamFalsePositive":
        # No flags

        channel = TLObject.read(b)

        msg_id = Int.read(b)

        return ReportAntiSpamFalsePositive(channel=channel, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.channel.write())

        b.write(Int(self.msg_id))

        return b.getvalue()
