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


class FoundStickersNotModified(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.FoundStickers`.

    Details:
        - Layer: ``224``
        - ID: ``6010C534``

    Parameters:
        next_offset (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SearchStickers
    """

    __slots__: List[str] = ["next_offset"]

    ID = 0x6010c534
    QUALNAME = "types.messages.FoundStickersNotModified"

    def __init__(self, *, next_offset: Optional[int] = None) -> None:
        self.next_offset = next_offset  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FoundStickersNotModified":

        flags = Int.read(b)

        next_offset = Int.read(b) if flags & (1 << 0) else None
        return FoundStickersNotModified(next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))

        if self.next_offset is not None:
            b.write(Int(self.next_offset))

        return b.getvalue()
