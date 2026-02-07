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


class DeleteTopicHistory(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D2816F10``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        top_msg_id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.AffectedHistory <pyrogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["peer", "top_msg_id"]

    ID = 0xd2816f10
    QUALNAME = "functions.messages.DeleteTopicHistory"

    def __init__(self, *, peer: "raw.base.InputPeer", top_msg_id: int) -> None:
        self.peer = peer  # InputPeer
        self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteTopicHistory":
        # No flags

        peer = TLObject.read(b)

        top_msg_id = Int.read(b)

        return DeleteTopicHistory(peer=peer, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.top_msg_id))

        return b.getvalue()
