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


class SponsoredMessageReportResultChooseOption(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.channels.SponsoredMessageReportResult`.

    Details:
        - Layer: ``224``
        - ID: ``846F9E42``

    Parameters:
        title (``str``):


        options (List of :obj:`SponsoredMessageReportOption <pyrogram.raw.base.SponsoredMessageReportOption>`):


    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReportSponsoredMessage
    """

    __slots__: List[str] = ["title", "options"]

    ID = 0x846f9e42
    QUALNAME = "types.channels.SponsoredMessageReportResultChooseOption"

    def __init__(self, *, title: str, options: List["raw.base.SponsoredMessageReportOption"]) -> None:
        self.title = title  # string
        self.options = options  # Vector<SponsoredMessageReportOption>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessageReportResultChooseOption":
        # No flags

        title = String.read(b)

        options = TLObject.read(b)

        return SponsoredMessageReportResultChooseOption(title=title, options=options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.title))

        b.write(Vector(self.options))

        return b.getvalue()
