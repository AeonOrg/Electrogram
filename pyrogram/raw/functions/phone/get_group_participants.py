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


class GetGroupParticipants(TLObject):  # type: ignore
    """Get group call participants


    Details:
        - Layer: ``224``
        - ID: ``C558D8AB``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Group call

        ids (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            If specified, will fetch group participant info about the specified peers

        sources (List of ``int`` ``32-bit``):
            If specified, will fetch group participant info about the specified WebRTC source IDs

        offset (``str``):
            Offset for results, taken from the next_offset field of phone.groupParticipants, initially an empty string. Note: if no more results are available, the method call will return an empty next_offset; thus, avoid providing the next_offset returned in phone.groupParticipants if it is empty, to avoid an infinite loop.

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

    Returns:
        :obj:`phone.GroupParticipants <pyrogram.raw.base.phone.GroupParticipants>`
    """

    __slots__: List[str] = ["call", "ids", "sources", "offset", "limit"]

    ID = 0xc558d8ab
    QUALNAME = "functions.phone.GetGroupParticipants"

    def __init__(self, *, call: "raw.base.InputGroupCall", ids: List["raw.base.InputPeer"], sources: List[int], offset: str, limit: int) -> None:
        self.call = call  # InputGroupCall
        self.ids = ids  # Vector<InputPeer>
        self.sources = sources  # Vector<int>
        self.offset = offset  # string
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupParticipants":
        # No flags

        call = TLObject.read(b)

        ids = TLObject.read(b)

        sources = TLObject.read(b, Int)

        offset = String.read(b)

        limit = Int.read(b)

        return GetGroupParticipants(call=call, ids=ids, sources=sources, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.call.write())

        b.write(Vector(self.ids))

        b.write(Vector(self.sources, Int))

        b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
