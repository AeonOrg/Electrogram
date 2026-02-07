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


class ExportAuthorization(TLObject):  # type: ignore
    """Returns data for copying authorization to another data-center.


    Details:
        - Layer: ``224``
        - ID: ``E5BFFFCD``

    Parameters:
        dc_id (``int`` ``32-bit``):
            Number of a target data-center

    Returns:
        :obj:`auth.ExportedAuthorization <pyrogram.raw.base.auth.ExportedAuthorization>`
    """

    __slots__: List[str] = ["dc_id"]

    ID = 0xe5bfffcd
    QUALNAME = "functions.auth.ExportAuthorization"

    def __init__(self, *, dc_id: int) -> None:
        self.dc_id = dc_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportAuthorization":
        # No flags

        dc_id = Int.read(b)

        return ExportAuthorization(dc_id=dc_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.dc_id))

        return b.getvalue()
