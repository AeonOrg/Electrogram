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


class ReportSponsoredMessage(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``12CBF0C4``

    Parameters:
        random_id (``bytes``):
            N/A

        option (``bytes``):
            N/A

    Returns:
        :obj:`channels.SponsoredMessageReportResult <pyrogram.raw.base.channels.SponsoredMessageReportResult>`
    """

    __slots__: List[str] = ["random_id", "option"]

    ID = 0x12cbf0c4
    QUALNAME = "functions.messages.ReportSponsoredMessage"

    def __init__(self, *, random_id: bytes, option: bytes) -> None:
        self.random_id = random_id  # bytes
        self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportSponsoredMessage":
        # No flags

        random_id = Bytes.read(b)

        option = Bytes.read(b)

        return ReportSponsoredMessage(random_id=random_id, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.random_id))

        b.write(Bytes(self.option))

        return b.getvalue()
