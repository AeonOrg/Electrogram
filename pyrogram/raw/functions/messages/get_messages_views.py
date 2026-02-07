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


class GetMessagesViews(TLObject):  # type: ignore
    """Get and increase the view counter of a message sent or forwarded from a channel


    Details:
        - Layer: ``224``
        - ID: ``5784D3E1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer where the message was found

        id (List of ``int`` ``32-bit``):
            ID of message

        increment (``bool``):
            Whether to mark the message as viewed and increment the view counter

    Returns:
        :obj:`messages.MessageViews <pyrogram.raw.base.messages.MessageViews>`
    """

    __slots__: List[str] = ["peer", "id", "increment"]

    ID = 0x5784d3e1
    QUALNAME = "functions.messages.GetMessagesViews"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int], increment: bool) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>
        self.increment = increment  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessagesViews":
        # No flags

        peer = TLObject.read(b)

        id = TLObject.read(b, Int)

        increment = Bool.read(b)

        return GetMessagesViews(peer=peer, id=id, increment=increment)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Vector(self.id, Int))

        b.write(Bool(self.increment))

        return b.getvalue()
