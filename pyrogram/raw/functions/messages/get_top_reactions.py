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


class GetTopReactions(TLObject):  # type: ignore
    """Got popular message reactions


    Details:
        - Layer: ``224``
        - ID: ``BB8125BA``

    Parameters:
        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.reactions.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`messages.Reactions <pyrogram.raw.base.messages.Reactions>`
    """

    __slots__: List[str] = ["limit", "hash"]

    ID = 0xbb8125ba
    QUALNAME = "functions.messages.GetTopReactions"

    def __init__(self, *, limit: int, hash: int) -> None:
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTopReactions":
        # No flags

        limit = Int.read(b)

        hash = Long.read(b)

        return GetTopReactions(limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.limit))

        b.write(Long(self.hash))

        return b.getvalue()
