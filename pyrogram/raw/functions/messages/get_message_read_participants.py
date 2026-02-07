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


class GetMessageReadParticipants(TLObject):  # type: ignore
    """Get which users read a specific message: only available for groups and supergroups with less than chat_read_mark_size_threshold members, read receipts will be stored for chat_read_mark_expire_period seconds after the message was sent, see client configuration for more info ».


    Details:
        - Layer: ``224``
        - ID: ``31C1C44F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Dialog

        msg_id (``int`` ``32-bit``):
            Message ID

    Returns:
        List of :obj:`ReadParticipantDate <pyrogram.raw.base.ReadParticipantDate>`
    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0x31c1c44f
    QUALNAME = "functions.messages.GetMessageReadParticipants"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageReadParticipants":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        return GetMessageReadParticipants(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        return b.getvalue()
