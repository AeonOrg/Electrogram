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


class SendAsPeer(TLObject):  # type: ignore
    """Indicates a peer that can be used to send messages

    Constructor of :obj:`~pyrogram.raw.base.SendAsPeer`.

    Details:
        - Layer: ``224``
        - ID: ``B81C7034``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Peer

        premium_required (``bool``, *optional*):
            Whether a Telegram Premium account is required to send messages as this peer

    """

    __slots__: List[str] = ["peer", "premium_required"]

    ID = 0xb81c7034
    QUALNAME = "types.SendAsPeer"

    def __init__(self, *, peer: "raw.base.Peer", premium_required: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.premium_required = premium_required  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendAsPeer":

        flags = Int.read(b)

        premium_required = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        return SendAsPeer(peer=peer, premium_required=premium_required)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.premium_required else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        return b.getvalue()
