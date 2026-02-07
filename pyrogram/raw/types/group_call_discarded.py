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


class GroupCallDiscarded(TLObject):  # type: ignore
    """An ended group call

    Constructor of :obj:`~pyrogram.raw.base.GroupCall`.

    Details:
        - Layer: ``224``
        - ID: ``7780BCB4``

    Parameters:
        id (``int`` ``64-bit``):
            Group call ID

        access_hash (``int`` ``64-bit``):
            Group call access hash

        duration (``int`` ``32-bit``):
            Group call duration

    """

    __slots__: List[str] = ["id", "access_hash", "duration"]

    ID = 0x7780bcb4
    QUALNAME = "types.GroupCallDiscarded"

    def __init__(self, *, id: int, access_hash: int, duration: int) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.duration = duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallDiscarded":
        # No flags

        id = Long.read(b)

        access_hash = Long.read(b)

        duration = Int.read(b)

        return GroupCallDiscarded(id=id, access_hash=access_hash, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        b.write(Long(self.access_hash))

        b.write(Int(self.duration))

        return b.getvalue()
