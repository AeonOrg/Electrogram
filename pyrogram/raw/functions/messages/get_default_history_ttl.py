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


class GetDefaultHistoryTTL(TLObject):  # type: ignore
    """Gets the default value of the Time-To-Live setting, applied to all new chats.


    Details:
        - Layer: ``224``
        - ID: ``658B7188``

    Parameters:
        No parameters required.

    Returns:
        :obj:`DefaultHistoryTTL <pyrogram.raw.base.DefaultHistoryTTL>`
    """

    __slots__: List[str] = []

    ID = 0x658b7188
    QUALNAME = "functions.messages.GetDefaultHistoryTTL"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDefaultHistoryTTL":
        # No flags

        return GetDefaultHistoryTTL()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
