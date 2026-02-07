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


class GetTermsOfServiceUpdate(TLObject):  # type: ignore
    """Look for updates of telegram's terms of service


    Details:
        - Layer: ``224``
        - ID: ``2CA51FD1``

    Parameters:
        No parameters required.

    Returns:
        :obj:`help.TermsOfServiceUpdate <pyrogram.raw.base.help.TermsOfServiceUpdate>`
    """

    __slots__: List[str] = []

    ID = 0x2ca51fd1
    QUALNAME = "functions.help.GetTermsOfServiceUpdate"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTermsOfServiceUpdate":
        # No flags

        return GetTermsOfServiceUpdate()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
