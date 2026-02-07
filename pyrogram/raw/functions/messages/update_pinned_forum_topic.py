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
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``175DF251``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        topic_id (``int`` ``32-bit``):
            N/A

        pinned (``bool``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "topic_id", "pinned"]

    ID = 0x175df251
    QUALNAME = "functions.messages.UpdatePinnedForumTopic"

    def __init__(self, *, peer: "raw.base.InputPeer", topic_id: int, pinned: bool) -> None:
        self.peer = peer  # InputPeer
        self.topic_id = topic_id  # int
        self.pinned = pinned  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedForumTopic":
        # No flags

        peer = TLObject.read(b)

        topic_id = Int.read(b)

        pinned = Bool.read(b)

        return UpdatePinnedForumTopic(peer=peer, topic_id=topic_id, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.topic_id))

        b.write(Bool(self.pinned))

        return b.getvalue()
