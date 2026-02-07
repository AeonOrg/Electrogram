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


class SponsoredMessageReportOption(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.SponsoredMessageReportOption`.

    Details:
        - Layer: ``224``
        - ID: ``430D3150``

    Parameters:
        text (``str``):


        option (``bytes``):


    """

    __slots__: List[str] = ["text", "option"]

    ID = 0x430d3150
    QUALNAME = "types.SponsoredMessageReportOption"

    def __init__(self, *, text: str, option: bytes) -> None:
        self.text = text  # string
        self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessageReportOption":
        # No flags

        text = String.read(b)

        option = Bytes.read(b)

        return SponsoredMessageReportOption(text=text, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.text))

        b.write(Bytes(self.option))

        return b.getvalue()
