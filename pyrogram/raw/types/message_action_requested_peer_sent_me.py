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


class MessageActionRequestedPeerSentMe(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``93B31848``

    Parameters:
        button_id (``int`` ``32-bit``):


        peers (List of :obj:`RequestedPeer <pyrogram.raw.base.RequestedPeer>`):


    """

    __slots__: List[str] = ["button_id", "peers"]

    ID = 0x93b31848
    QUALNAME = "types.MessageActionRequestedPeerSentMe"

    def __init__(self, *, button_id: int, peers: List["raw.base.RequestedPeer"]) -> None:
        self.button_id = button_id  # int
        self.peers = peers  # Vector<RequestedPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionRequestedPeerSentMe":
        # No flags

        button_id = Int.read(b)

        peers = TLObject.read(b)

        return MessageActionRequestedPeerSentMe(button_id=button_id, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.button_id))

        b.write(Vector(self.peers))

        return b.getvalue()
