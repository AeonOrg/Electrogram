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


class GetRecentStickers(TLObject):  # type: ignore
    """Get recent stickers


    Details:
        - Layer: ``224``
        - ID: ``9DA9403B``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.recentStickers.hash field returned by a previous call to the method, or pass 0 if this is the first call.

        attached (``bool``, *optional*):
            Get stickers recently attached to photo or video files

    Returns:
        :obj:`messages.RecentStickers <pyrogram.raw.base.messages.RecentStickers>`
    """

    __slots__: List[str] = ["hash", "attached"]

    ID = 0x9da9403b
    QUALNAME = "functions.messages.GetRecentStickers"

    def __init__(self, *, hash: int, attached: Optional[bool] = None) -> None:
        self.hash = hash  # long
        self.attached = attached  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentStickers":

        flags = Int.read(b)

        attached = True if flags & (1 << 0) else False
        hash = Long.read(b)

        return GetRecentStickers(hash=hash, attached=attached)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached else 0
        b.write(Int(flags))

        b.write(Long(self.hash))

        return b.getvalue()
