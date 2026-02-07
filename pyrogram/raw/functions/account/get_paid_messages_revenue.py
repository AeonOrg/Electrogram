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


class GetPaidMessagesRevenue(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``19BA4A67``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        parent_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`account.PaidMessagesRevenue <pyrogram.raw.base.account.PaidMessagesRevenue>`
    """

    __slots__: List[str] = ["user_id", "parent_peer"]

    ID = 0x19ba4a67
    QUALNAME = "functions.account.GetPaidMessagesRevenue"

    def __init__(self, *, user_id: "raw.base.InputUser", parent_peer: "raw.base.InputPeer" = None) -> None:
        self.user_id = user_id  # InputUser
        self.parent_peer = parent_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPaidMessagesRevenue":

        flags = Int.read(b)

        parent_peer = TLObject.read(b) if flags & (1 << 0) else None

        user_id = TLObject.read(b)

        return GetPaidMessagesRevenue(user_id=user_id, parent_peer=parent_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.parent_peer is not None else 0
        b.write(Int(flags))

        if self.parent_peer is not None:
            b.write(self.parent_peer.write())

        b.write(self.user_id.write())

        return b.getvalue()
