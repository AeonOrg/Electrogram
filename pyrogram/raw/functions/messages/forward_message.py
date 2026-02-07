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


class ForwardMessage(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``33963BF9``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "random_id"]

    ID = 0x33963bf9
    QUALNAME = "functions.messages.ForwardMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, random_id: int) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.random_id = random_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForwardMessage":
        # No flags

        peer = TLObject.read(b)

        id = Int.read(b)

        random_id = Long.read(b)

        return ForwardMessage(peer=peer, id=id, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.id))

        b.write(Long(self.random_id))

        return b.getvalue()
