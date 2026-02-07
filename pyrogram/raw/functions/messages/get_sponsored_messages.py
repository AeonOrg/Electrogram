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


class GetSponsoredMessages(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3D6CE850``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`messages.SponsoredMessages <pyrogram.raw.base.messages.SponsoredMessages>`
    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0x3d6ce850
    QUALNAME = "functions.messages.GetSponsoredMessages"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSponsoredMessages":

        flags = Int.read(b)

        peer = TLObject.read(b)

        msg_id = Int.read(b) if flags & (1 << 0) else None
        return GetSponsoredMessages(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.msg_id is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.msg_id is not None:
            b.write(Int(self.msg_id))

        return b.getvalue()
