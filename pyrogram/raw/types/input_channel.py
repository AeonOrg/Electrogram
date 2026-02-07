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


class InputChannel(TLObject):  # type: ignore
    """Represents a channel

    Constructor of :obj:`~pyrogram.raw.base.InputChannel`.

    Details:
        - Layer: ``224``
        - ID: ``F35AEC28``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

        access_hash (``int`` ``64-bit``):
            Access hash taken from the channel constructor

    """

    __slots__: List[str] = ["channel_id", "access_hash"]

    ID = 0xf35aec28
    QUALNAME = "types.InputChannel"

    def __init__(self, *, channel_id: int, access_hash: int) -> None:
        self.channel_id = channel_id  # long
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChannel":
        # No flags

        channel_id = Long.read(b)

        access_hash = Long.read(b)

        return InputChannel(channel_id=channel_id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.channel_id))

        b.write(Long(self.access_hash))

        return b.getvalue()
