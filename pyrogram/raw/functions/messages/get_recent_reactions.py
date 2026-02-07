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


class GetRecentReactions(TLObject):  # type: ignore
    """Get recently used message reactions


    Details:
        - Layer: ``224``
        - ID: ``39461DB2``

    Parameters:
        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.reactions.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`messages.Reactions <pyrogram.raw.base.messages.Reactions>`
    """

    __slots__: List[str] = ["limit", "hash"]

    ID = 0x39461db2
    QUALNAME = "functions.messages.GetRecentReactions"

    def __init__(self, *, limit: int, hash: int) -> None:
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentReactions":
        # No flags

        limit = Int.read(b)

        hash = Long.read(b)

        return GetRecentReactions(limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.limit))

        b.write(Long(self.hash))

        return b.getvalue()
