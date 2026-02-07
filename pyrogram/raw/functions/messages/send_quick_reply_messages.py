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


class SendQuickReplyMessages(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``6C750DE1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):


        shortcut_id (``int`` ``32-bit``):


        id (List of ``int`` ``32-bit``):


        random_id (List of ``int`` ``64-bit``):


    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "shortcut_id", "id", "random_id"]

    ID = 0x6c750de1
    QUALNAME = "functions.messages.SendQuickReplyMessages"

    def __init__(self, *, peer: "raw.base.InputPeer", shortcut_id: int, id: List[int], random_id: List[int]) -> None:
        self.peer = peer  # InputPeer
        self.shortcut_id = shortcut_id  # int
        self.id = id  # Vector<int>
        self.random_id = random_id  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendQuickReplyMessages":
        # No flags

        peer = TLObject.read(b)

        shortcut_id = Int.read(b)

        id = TLObject.read(b, Int)

        random_id = TLObject.read(b, Long)

        return SendQuickReplyMessages(peer=peer, shortcut_id=shortcut_id, id=id, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.shortcut_id))

        b.write(Vector(self.id, Int))

        b.write(Vector(self.random_id, Long))

        return b.getvalue()
