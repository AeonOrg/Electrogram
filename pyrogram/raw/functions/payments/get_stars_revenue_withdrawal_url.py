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


class GetStarsRevenueWithdrawalUrl(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2433DC92``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            N/A

        ton (``bool``, *optional*):
            N/A

        amount (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`payments.StarsRevenueWithdrawalUrl <pyrogram.raw.base.payments.StarsRevenueWithdrawalUrl>`
    """

    __slots__: List[str] = ["peer", "password", "ton", "amount"]

    ID = 0x2433dc92
    QUALNAME = "functions.payments.GetStarsRevenueWithdrawalUrl"

    def __init__(self, *, peer: "raw.base.InputPeer", password: "raw.base.InputCheckPasswordSRP", ton: Optional[bool] = None, amount: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.password = password  # InputCheckPasswordSRP
        self.ton = ton  # flags.0?true
        self.amount = amount  # flags.1?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsRevenueWithdrawalUrl":

        flags = Int.read(b)

        ton = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        amount = Long.read(b) if flags & (1 << 1) else None
        password = TLObject.read(b)

        return GetStarsRevenueWithdrawalUrl(peer=peer, password=password, ton=ton, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        flags |= (1 << 1) if self.amount is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        if self.amount is not None:
            b.write(Long(self.amount))

        b.write(self.password.write())

        return b.getvalue()
