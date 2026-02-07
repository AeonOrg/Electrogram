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


class UpdateDeviceLocked(TLObject):  # type: ignore
    """When client-side passcode lock feature is enabled, will not show message texts in incoming PUSH notifications.


    Details:
        - Layer: ``224``
        - ID: ``38DF3532``

    Parameters:
        period (``int`` ``32-bit``):
            Inactivity period after which to start hiding message texts in PUSH notifications.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["period"]

    ID = 0x38df3532
    QUALNAME = "functions.account.UpdateDeviceLocked"

    def __init__(self, *, period: int) -> None:
        self.period = period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeviceLocked":
        # No flags

        period = Int.read(b)

        return UpdateDeviceLocked(period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.period))

        return b.getvalue()
