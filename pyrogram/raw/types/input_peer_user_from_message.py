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


class InputPeerUserFromMessage(TLObject):  # type: ignore
    """Defines a min user that was seen in a certain message of a certain chat.

    Constructor of :obj:`~pyrogram.raw.base.InputPeer`.

    Details:
        - Layer: ``224``
        - ID: ``A87B0A1C``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The chat where the user was seen

        msg_id (``int`` ``32-bit``):
            The message ID

        user_id (``int`` ``64-bit``):
            The identifier of the user that was seen

    """

    __slots__: List[str] = ["peer", "msg_id", "user_id"]

    ID = 0xa87b0a1c
    QUALNAME = "types.InputPeerUserFromMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, user_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerUserFromMessage":
        # No flags

        peer = TLObject.read(b)

        msg_id = Int.read(b)

        user_id = Long.read(b)

        return InputPeerUserFromMessage(peer=peer, msg_id=msg_id, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.msg_id))

        b.write(Long(self.user_id))

        return b.getvalue()
