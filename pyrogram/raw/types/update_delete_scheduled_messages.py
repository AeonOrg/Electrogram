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


class UpdateDeleteScheduledMessages(TLObject):  # type: ignore
    """Some scheduled messages were deleted from the schedule queue of a chat

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F2A71983``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer

        messages (List of ``int`` ``32-bit``):
            Deleted scheduled messages

        sent_messages (List of ``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "messages", "sent_messages"]

    ID = 0xf2a71983
    QUALNAME = "types.UpdateDeleteScheduledMessages"

    def __init__(self, *, peer: "raw.base.Peer", messages: List[int], sent_messages: Optional[List[int]] = None) -> None:
        self.peer = peer  # Peer
        self.messages = messages  # Vector<int>
        self.sent_messages = sent_messages  # flags.0?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeleteScheduledMessages":

        flags = Int.read(b)

        peer = TLObject.read(b)

        messages = TLObject.read(b, Int)

        sent_messages = TLObject.read(b, Int) if flags & (1 << 0) else []

        return UpdateDeleteScheduledMessages(peer=peer, messages=messages, sent_messages=sent_messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sent_messages else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Vector(self.messages, Int))

        if self.sent_messages is not None:
            b.write(Vector(self.sent_messages, Int))

        return b.getvalue()
