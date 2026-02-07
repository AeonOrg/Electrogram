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


class GetForumTopics(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3BA47BFF``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset_date (``int`` ``32-bit``):
            N/A

        offset_id (``int`` ``32-bit``):
            N/A

        offset_topic (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        q (``str``, *optional*):
            N/A

    Returns:
        :obj:`messages.ForumTopics <pyrogram.raw.base.messages.ForumTopics>`
    """

    __slots__: List[str] = ["peer", "offset_date", "offset_id", "offset_topic", "limit", "q"]

    ID = 0x3ba47bff
    QUALNAME = "functions.messages.GetForumTopics"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_date: int, offset_id: int, offset_topic: int, limit: int, q: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset_date = offset_date  # int
        self.offset_id = offset_id  # int
        self.offset_topic = offset_topic  # int
        self.limit = limit  # int
        self.q = q  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetForumTopics":

        flags = Int.read(b)

        peer = TLObject.read(b)

        q = String.read(b) if flags & (1 << 0) else None
        offset_date = Int.read(b)

        offset_id = Int.read(b)

        offset_topic = Int.read(b)

        limit = Int.read(b)

        return GetForumTopics(peer=peer, offset_date=offset_date, offset_id=offset_id, offset_topic=offset_topic, limit=limit, q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.q is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.q is not None:
            b.write(String(self.q))

        b.write(Int(self.offset_date))

        b.write(Int(self.offset_id))

        b.write(Int(self.offset_topic))

        b.write(Int(self.limit))

        return b.getvalue()
