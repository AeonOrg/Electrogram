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


class MessageEmpty(TLObject):  # type: ignore
    """Empty constructor, non-existent message.

    Constructor of :obj:`~pyrogram.raw.base.Message`.

    Details:
        - Layer: ``224``
        - ID: ``90A6CA84``

    Parameters:
        id (``int`` ``32-bit``):
            Message identifier

        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            Peer ID, the chat where this message was sent

    """

    __slots__: List[str] = ["id", "peer_id"]

    ID = 0x90a6ca84
    QUALNAME = "types.MessageEmpty"

    def __init__(self, *, id: int, peer_id: "raw.base.Peer" = None) -> None:
        self.id = id  # int
        self.peer_id = peer_id  # flags.0?Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEmpty":

        flags = Int.read(b)

        id = Int.read(b)

        peer_id = TLObject.read(b) if flags & (1 << 0) else None

        return MessageEmpty(id=id, peer_id=peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.peer_id is not None else 0
        b.write(Int(flags))

        b.write(Int(self.id))

        if self.peer_id is not None:
            b.write(self.peer_id.write())

        return b.getvalue()
