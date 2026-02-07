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


class NotificationSoundDefault(TLObject):  # type: ignore
    """Indicates the default notification sound should be used

    Constructor of :obj:`~pyrogram.raw.base.NotificationSound`.

    Details:
        - Layer: ``224``
        - ID: ``97E8BEBE``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x97e8bebe
    QUALNAME = "types.NotificationSoundDefault"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NotificationSoundDefault":
        # No flags

        return NotificationSoundDefault()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
