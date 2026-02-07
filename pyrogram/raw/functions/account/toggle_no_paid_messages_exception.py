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


class ToggleNoPaidMessagesException(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FE2EDA76``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        refund_charged (``bool``, *optional*):
            N/A

        require_payment (``bool``, *optional*):
            N/A

        parent_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["user_id", "refund_charged", "require_payment", "parent_peer"]

    ID = 0xfe2eda76
    QUALNAME = "functions.account.ToggleNoPaidMessagesException"

    def __init__(self, *, user_id: "raw.base.InputUser", refund_charged: Optional[bool] = None, require_payment: Optional[bool] = None, parent_peer: "raw.base.InputPeer" = None) -> None:
        self.user_id = user_id  # InputUser
        self.refund_charged = refund_charged  # flags.0?true
        self.require_payment = require_payment  # flags.2?true
        self.parent_peer = parent_peer  # flags.1?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleNoPaidMessagesException":

        flags = Int.read(b)

        refund_charged = True if flags & (1 << 0) else False
        require_payment = True if flags & (1 << 2) else False
        parent_peer = TLObject.read(b) if flags & (1 << 1) else None

        user_id = TLObject.read(b)

        return ToggleNoPaidMessagesException(user_id=user_id, refund_charged=refund_charged, require_payment=require_payment, parent_peer=parent_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.refund_charged else 0
        flags |= (1 << 2) if self.require_payment else 0
        flags |= (1 << 1) if self.parent_peer is not None else 0
        b.write(Int(flags))

        if self.parent_peer is not None:
            b.write(self.parent_peer.write())

        b.write(self.user_id.write())

        return b.getvalue()
