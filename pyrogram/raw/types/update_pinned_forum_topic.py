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


class UpdatePinnedForumTopic(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``683B2C52``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        topic_id (``int`` ``32-bit``):
            N/A

        pinned (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "topic_id", "pinned"]

    ID = 0x683b2c52
    QUALNAME = "types.UpdatePinnedForumTopic"

    def __init__(self, *, peer: "raw.base.Peer", topic_id: int, pinned: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.topic_id = topic_id  # int
        self.pinned = pinned  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedForumTopic":

        flags = Int.read(b)

        pinned = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        topic_id = Int.read(b)

        return UpdatePinnedForumTopic(peer=peer, topic_id=topic_id, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Int(self.topic_id))

        return b.getvalue()
