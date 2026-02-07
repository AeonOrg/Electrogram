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


class GetStarsTopupOptions(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``C00EC7D3``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`StarsTopupOption <pyrogram.raw.base.StarsTopupOption>`
    """

    __slots__: List[str] = []

    ID = 0xc00ec7d3
    QUALNAME = "functions.payments.GetStarsTopupOptions"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsTopupOptions":
        # No flags

        return GetStarsTopupOptions()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
