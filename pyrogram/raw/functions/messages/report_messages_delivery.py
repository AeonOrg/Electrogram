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


class ReportMessagesDelivery(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5A6D7395``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (List of ``int`` ``32-bit``):
            N/A

        push (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "id", "push"]

    ID = 0x5a6d7395
    QUALNAME = "functions.messages.ReportMessagesDelivery"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int], push: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>
        self.push = push  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportMessagesDelivery":

        flags = Int.read(b)

        push = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        id = TLObject.read(b, Int)

        return ReportMessagesDelivery(peer=peer, id=id, push=push)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.push else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Vector(self.id, Int))

        return b.getvalue()
