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


class StoriesStealthMode(TLObject):  # type: ignore
    """Information about the current stealth mode session.

    Constructor of :obj:`~pyrogram.raw.base.StoriesStealthMode`.

    Details:
        - Layer: ``224``
        - ID: ``712E27FD``

    Parameters:
        active_until_date (``int`` ``32-bit``, *optional*):
            The date up to which stealth mode will be active.

        cooldown_until_date (``int`` ``32-bit``, *optional*):
            The date starting from which the user will be allowed to re-enable stealth mode again.

    """

    __slots__: List[str] = ["active_until_date", "cooldown_until_date"]

    ID = 0x712e27fd
    QUALNAME = "types.StoriesStealthMode"

    def __init__(self, *, active_until_date: Optional[int] = None, cooldown_until_date: Optional[int] = None) -> None:
        self.active_until_date = active_until_date  # flags.0?int
        self.cooldown_until_date = cooldown_until_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoriesStealthMode":

        flags = Int.read(b)

        active_until_date = Int.read(b) if flags & (1 << 0) else None
        cooldown_until_date = Int.read(b) if flags & (1 << 1) else None
        return StoriesStealthMode(active_until_date=active_until_date, cooldown_until_date=cooldown_until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.active_until_date is not None else 0
        flags |= (1 << 1) if self.cooldown_until_date is not None else 0
        b.write(Int(flags))

        if self.active_until_date is not None:
            b.write(Int(self.active_until_date))

        if self.cooldown_until_date is not None:
            b.write(Int(self.cooldown_until_date))

        return b.getvalue()
