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


class GetDialogFilters(TLObject):  # type: ignore
    """Get folders


    Details:
        - Layer: ``224``
        - ID: ``EFD48C89``

    Parameters:
        No parameters required.

    Returns:
        :obj:`messages.DialogFilters <pyrogram.raw.base.messages.DialogFilters>`
    """

    __slots__: List[str] = []

    ID = 0xefd48c89
    QUALNAME = "functions.messages.GetDialogFilters"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDialogFilters":
        # No flags

        return GetDialogFilters()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
