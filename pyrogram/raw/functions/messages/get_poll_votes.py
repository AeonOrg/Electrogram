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


class GetPollVotes(TLObject):  # type: ignore
    """Get poll results for non-anonymous polls


    Details:
        - Layer: ``224``
        - ID: ``B86E380E``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Chat where the poll was sent

        id (``int`` ``32-bit``):
            Message ID

        limit (``int`` ``32-bit``):
            Number of results to return

        option (``bytes``, *optional*):
            Get only results for the specified poll option

        offset (``str``, *optional*):
            Offset for results, taken from the next_offset field of messages.votesList, initially an empty string. Note: if no more results are available, the method call will return an empty next_offset; thus, avoid providing the next_offset returned in messages.votesList if it is empty, to avoid an infinite loop.

    Returns:
        :obj:`messages.VotesList <pyrogram.raw.base.messages.VotesList>`
    """

    __slots__: List[str] = ["peer", "id", "limit", "option", "offset"]

    ID = 0xb86e380e
    QUALNAME = "functions.messages.GetPollVotes"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, limit: int, option: Optional[bytes] = None, offset: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.limit = limit  # int
        self.option = option  # flags.0?bytes
        self.offset = offset  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPollVotes":

        flags = Int.read(b)

        peer = TLObject.read(b)

        id = Int.read(b)

        option = Bytes.read(b) if flags & (1 << 0) else None
        offset = String.read(b) if flags & (1 << 1) else None
        limit = Int.read(b)

        return GetPollVotes(peer=peer, id=id, limit=limit, option=option, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.option is not None else 0
        flags |= (1 << 1) if self.offset is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.id))

        if self.option is not None:
            b.write(Bytes(self.option))

        if self.offset is not None:
            b.write(String(self.offset))

        b.write(Int(self.limit))

        return b.getvalue()
