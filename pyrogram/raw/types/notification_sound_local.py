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


class NotificationSoundLocal(TLObject):  # type: ignore
    """Indicates a specific local notification sound should be used

    Constructor of :obj:`~pyrogram.raw.base.NotificationSound`.

    Details:
        - Layer: ``224``
        - ID: ``830B9AE4``

    Parameters:
        title (``str``):
            Notification sound title

        data (``str``):
            Notification sound identifier (arbitrary data used by the client to identify a specific local notification sound)

    """

    __slots__: List[str] = ["title", "data"]

    ID = 0x830b9ae4
    QUALNAME = "types.NotificationSoundLocal"

    def __init__(self, *, title: str, data: str) -> None:
        self.title = title  # string
        self.data = data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NotificationSoundLocal":
        # No flags

        title = String.read(b)

        data = String.read(b)

        return NotificationSoundLocal(title=title, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.title))

        b.write(String(self.data))

        return b.getvalue()
