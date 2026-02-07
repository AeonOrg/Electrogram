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


class GetSupportName(TLObject):  # type: ignore
    """Get localized name of the telegram support user


    Details:
        - Layer: ``224``
        - ID: ``D360E72C``

    Parameters:
        No parameters required.

    Returns:
        :obj:`help.SupportName <pyrogram.raw.base.help.SupportName>`
    """

    __slots__: List[str] = []

    ID = 0xd360e72c
    QUALNAME = "functions.help.GetSupportName"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSupportName":
        # No flags

        return GetSupportName()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
