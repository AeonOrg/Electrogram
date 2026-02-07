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


class InputStorePaymentStarsTopup(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``F9A2A6CB``

    Parameters:
        stars (``int`` ``64-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        spend_purpose_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["stars", "currency", "amount", "spend_purpose_peer"]

    ID = 0xf9a2a6cb
    QUALNAME = "types.InputStorePaymentStarsTopup"

    def __init__(self, *, stars: int, currency: str, amount: int, spend_purpose_peer: "raw.base.InputPeer" = None) -> None:
        self.stars = stars  # long
        self.currency = currency  # string
        self.amount = amount  # long
        self.spend_purpose_peer = spend_purpose_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentStarsTopup":

        flags = Int.read(b)

        stars = Long.read(b)

        currency = String.read(b)

        amount = Long.read(b)

        spend_purpose_peer = TLObject.read(b) if flags & (1 << 0) else None

        return InputStorePaymentStarsTopup(stars=stars, currency=currency, amount=amount, spend_purpose_peer=spend_purpose_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.spend_purpose_peer is not None else 0
        b.write(Int(flags))

        b.write(Long(self.stars))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        if self.spend_purpose_peer is not None:
            b.write(self.spend_purpose_peer.write())

        return b.getvalue()
