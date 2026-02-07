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


class GetStarsSubscriptions(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``32512C5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        offset (``str``):
            N/A

        missing_balance (``bool``, *optional*):
            N/A

    Returns:
        :obj:`payments.StarsStatus <pyrogram.raw.base.payments.StarsStatus>`
    """

    __slots__: List[str] = ["peer", "offset", "missing_balance"]

    ID = 0x32512c5
    QUALNAME = "functions.payments.GetStarsSubscriptions"

    def __init__(self, *, peer: "raw.base.InputPeer", offset: str, missing_balance: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset = offset  # string
        self.missing_balance = missing_balance  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsSubscriptions":

        flags = Int.read(b)

        missing_balance = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        offset = String.read(b)

        return GetStarsSubscriptions(peer=peer, offset=offset, missing_balance=missing_balance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.missing_balance else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(String(self.offset))

        return b.getvalue()
