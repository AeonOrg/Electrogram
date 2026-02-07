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


class MessageActionGiveawayLaunch(TLObject):  # type: ignore
    """A giveaway was started.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``A80F51E4``

    Parameters:
        stars (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["stars"]

    ID = 0xa80f51e4
    QUALNAME = "types.MessageActionGiveawayLaunch"

    def __init__(self, *, stars: Optional[int] = None) -> None:
        self.stars = stars  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiveawayLaunch":

        flags = Int.read(b)

        stars = Long.read(b) if flags & (1 << 0) else None
        return MessageActionGiveawayLaunch(stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.stars is not None else 0
        b.write(Int(flags))

        if self.stars is not None:
            b.write(Long(self.stars))

        return b.getvalue()
