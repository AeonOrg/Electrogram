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


class ReadDiscussion(TLObject):  # type: ignore
    """Mark a thread as read


    Details:
        - Layer: ``224``
        - ID: ``F731A9F4``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Group ID

        msg_id (``int`` ``32-bit``):
            ID of message that started the thread

        read_max_id (``int`` ``32-bit``):
            ID up to which thread messages were read

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "msg_id", "read_max_id"]

    ID = 0xf731a9f4
    QUALNAME = "functions.messages.ReadDiscussion"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, read_max_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.read_max_id = read_max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadDiscussion":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        read_max_id = Int.read(b)

        return ReadDiscussion(peer=peer, msg_id=msg_id, read_max_id=read_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Int(self.read_max_id))

        return b.getvalue()
