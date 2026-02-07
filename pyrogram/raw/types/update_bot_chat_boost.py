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


class UpdateBotChatBoost(TLObject):  # type: ignore
    """A channel boost has changed (bots only)

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``904DD49C``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            Channel

        boost (:obj:`Boost <pyrogram.raw.base.Boost>`):
            New boost information

        qts (``int`` ``32-bit``):
            QTS event sequence identifier

    """

    __slots__: List[str] = ["peer", "boost", "qts"]

    ID = 0x904dd49c
    QUALNAME = "types.UpdateBotChatBoost"

    def __init__(self, *, peer: "raw.base.Peer", boost: "raw.base.Boost", qts: int) -> None:
        self.peer = peer  # Peer
        self.boost = boost  # Boost
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotChatBoost":
        # No flags

        peer = TLObject.read(b)

        boost = TLObject.read(b)

        qts = Int.read(b)

        return UpdateBotChatBoost(peer=peer, boost=boost, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(self.boost.write())

        b.write(Int(self.qts))

        return b.getvalue()
