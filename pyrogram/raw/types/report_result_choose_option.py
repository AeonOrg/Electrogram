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


class ReportResultChooseOption(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReportResult`.

    Details:
        - Layer: ``224``
        - ID: ``F0E4E0B6``

    Parameters:
        title (``str``):
            N/A

        options (List of :obj:`MessageReportOption <pyrogram.raw.base.MessageReportOption>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.Report
            stories.Report
    """

    __slots__: List[str] = ["title", "options"]

    ID = 0xf0e4e0b6
    QUALNAME = "types.ReportResultChooseOption"

    def __init__(self, *, title: str, options: List["raw.base.MessageReportOption"]) -> None:
        self.title = title  # string
        self.options = options  # Vector<MessageReportOption>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportResultChooseOption":
        # No flags

        title = String.read(b)

        options = TLObject.read(b)

        return ReportResultChooseOption(title=title, options=options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.title))

        b.write(Vector(self.options))

        return b.getvalue()
