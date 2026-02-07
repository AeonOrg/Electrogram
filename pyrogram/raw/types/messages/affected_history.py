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


class AffectedHistory(TLObject):  # type: ignore
    """Affected part of communication history with the user or in a chat.

    Constructor of :obj:`~pyrogram.raw.base.messages.AffectedHistory`.

    Details:
        - Layer: ``224``
        - ID: ``B45C69D1``

    Parameters:
        pts (``int`` ``32-bit``):
            Number of events occurred in a text box

        pts_count (``int`` ``32-bit``):
            Number of affected events

        offset (``int`` ``32-bit``):
            If a parameter contains positive value, it is necessary to repeat the method call using the given value; during the proceeding of all the history the value itself shall gradually decrease

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.DeleteHistory
            messages.ReadMentions
            messages.UnpinAllMessages
            messages.ReadReactions
            messages.DeleteSavedHistory
            messages.DeleteTopicHistory
            channels.DeleteParticipantHistory
    """

    __slots__: List[str] = ["pts", "pts_count", "offset"]

    ID = 0xb45c69d1
    QUALNAME = "types.messages.AffectedHistory"

    def __init__(self, *, pts: int, pts_count: int, offset: int) -> None:
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.offset = offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AffectedHistory":
        # No flags

        pts = Int.read(b)

        pts_count = Int.read(b)

        offset = Int.read(b)

        return AffectedHistory(pts=pts, pts_count=pts_count, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.pts))

        b.write(Int(self.pts_count))

        b.write(Int(self.offset))

        return b.getvalue()
