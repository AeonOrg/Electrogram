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


class GetStarsGiveawayOptions(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BD1EFD3E``

    Parameters:
        No parameters required.

    Returns:
        List of :obj:`StarsGiveawayOption <pyrogram.raw.base.StarsGiveawayOption>`
    """

    __slots__: List[str] = []

    ID = 0xbd1efd3e
    QUALNAME = "functions.payments.GetStarsGiveawayOptions"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsGiveawayOptions":
        # No flags

        return GetStarsGiveawayOptions()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
