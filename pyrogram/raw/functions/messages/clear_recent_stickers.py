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


class ClearRecentStickers(TLObject):  # type: ignore
    """Clear recent stickers


    Details:
        - Layer: ``224``
        - ID: ``8999602D``

    Parameters:
        attached (``bool``, *optional*):
            Set this flag to clear the list of stickers recently attached to photo or video files

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["attached"]

    ID = 0x8999602d
    QUALNAME = "functions.messages.ClearRecentStickers"

    def __init__(self, *, attached: Optional[bool] = None) -> None:
        self.attached = attached  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ClearRecentStickers":

        flags = Int.read(b)

        attached = True if flags & (1 << 0) else False
        return ClearRecentStickers(attached=attached)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached else 0
        b.write(Int(flags))

        return b.getvalue()
