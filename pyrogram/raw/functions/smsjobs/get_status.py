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


class GetStatus(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``10A698E8``

    Parameters:
        No parameters required.

    Returns:
        :obj:`smsjobs.Status <pyrogram.raw.base.smsjobs.Status>`
    """

    __slots__: List[str] = []

    ID = 0x10a698e8
    QUALNAME = "functions.smsjobs.GetStatus"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStatus":
        # No flags

        return GetStatus()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
