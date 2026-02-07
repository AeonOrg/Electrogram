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


class MessageActionGiveawayResults(TLObject):  # type: ignore
    """A giveaway has ended.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``87E2F155``

    Parameters:
        winners_count (``int`` ``32-bit``):
            Number of winners in the giveaway

        unclaimed_count (``int`` ``32-bit``):
            Number of undistributed prizes

        stars (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["winners_count", "unclaimed_count", "stars"]

    ID = 0x87e2f155
    QUALNAME = "types.MessageActionGiveawayResults"

    def __init__(self, *, winners_count: int, unclaimed_count: int, stars: Optional[bool] = None) -> None:
        self.winners_count = winners_count  # int
        self.unclaimed_count = unclaimed_count  # int
        self.stars = stars  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiveawayResults":

        flags = Int.read(b)

        stars = True if flags & (1 << 0) else False
        winners_count = Int.read(b)

        unclaimed_count = Int.read(b)

        return MessageActionGiveawayResults(winners_count=winners_count, unclaimed_count=unclaimed_count, stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.stars else 0
        b.write(Int(flags))

        b.write(Int(self.winners_count))

        b.write(Int(self.unclaimed_count))

        return b.getvalue()
