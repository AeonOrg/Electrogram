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


class SetDefaultHistoryTTL(TLObject):  # type: ignore
    """Changes the default value of the Time-To-Live setting, applied to all new chats.


    Details:
        - Layer: ``224``
        - ID: ``9EB51445``

    Parameters:
        period (``int`` ``32-bit``):
            The new default Time-To-Live of all messages sent in new chats.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["period"]

    ID = 0x9eb51445
    QUALNAME = "functions.messages.SetDefaultHistoryTTL"

    def __init__(self, *, period: int) -> None:
        self.period = period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetDefaultHistoryTTL":
        # No flags

        period = Int.read(b)

        return SetDefaultHistoryTTL(period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.period))

        return b.getvalue()
