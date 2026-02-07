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


class ToggleTodoCompleted(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D3E03124``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        completed (List of ``int`` ``32-bit``):
            N/A

        incompleted (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "completed", "incompleted"]

    ID = 0xd3e03124
    QUALNAME = "functions.messages.ToggleTodoCompleted"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, completed: List[int], incompleted: List[int]) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.completed = completed  # Vector<int>
        self.incompleted = incompleted  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleTodoCompleted":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        completed = TLObject.read(b, Int)

        incompleted = TLObject.read(b, Int)

        return ToggleTodoCompleted(peer=peer, msg_id=msg_id, completed=completed, incompleted=incompleted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Vector(self.completed, Int))

        b.write(Vector(self.incompleted, Int))

        return b.getvalue()
