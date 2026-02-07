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


class GetDiscussionMessage(TLObject):  # type: ignore
    """Get discussion message from the associated discussion group of a channel to show it on top of the comment section, without actually joining the group


    Details:
        - Layer: ``224``
        - ID: ``446972FD``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Channel ID

        msg_id (``int`` ``32-bit``):
            Message ID

    Returns:
        :obj:`messages.DiscussionMessage <pyrogram.raw.base.messages.DiscussionMessage>`
    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0x446972fd
    QUALNAME = "functions.messages.GetDiscussionMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDiscussionMessage":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        return GetDiscussionMessage(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        return b.getvalue()
