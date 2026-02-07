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


class GetNearestDc(TLObject):  # type: ignore
    """Returns info on data center nearest to the user.


    Details:
        - Layer: ``224``
        - ID: ``1FB33026``

    Parameters:
        No parameters required.

    Returns:
        :obj:`NearestDc <pyrogram.raw.base.NearestDc>`
    """

    __slots__: List[str] = []

    ID = 0x1fb33026
    QUALNAME = "functions.help.GetNearestDc"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetNearestDc":
        # No flags

        return GetNearestDc()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
