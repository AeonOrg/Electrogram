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


class GroupCallParticipantVideoSourceGroup(TLObject):  # type: ignore
    """Describes a group of video synchronization source identifiers

    Constructor of :obj:`~pyrogram.raw.base.GroupCallParticipantVideoSourceGroup`.

    Details:
        - Layer: ``224``
        - ID: ``DCB118B7``

    Parameters:
        semantics (``str``):
            SDP semantics

        sources (List of ``int`` ``32-bit``):
            Source IDs

    """

    __slots__: List[str] = ["semantics", "sources"]

    ID = 0xdcb118b7
    QUALNAME = "types.GroupCallParticipantVideoSourceGroup"

    def __init__(self, *, semantics: str, sources: List[int]) -> None:
        self.semantics = semantics  # string
        self.sources = sources  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallParticipantVideoSourceGroup":
        # No flags

        semantics = String.read(b)

        sources = TLObject.read(b, Int)

        return GroupCallParticipantVideoSourceGroup(semantics=semantics, sources=sources)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.semantics))

        b.write(Vector(self.sources, Int))

        return b.getvalue()
