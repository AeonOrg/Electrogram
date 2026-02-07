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


class InputStorePaymentPremiumGiftCode(TLObject):  # type: ignore
    """Used to gift Telegram Premium subscriptions only to some specific subscribers of a channel or to some of our contacts, see here » for more info on giveaways and gifts.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``FB790393``

    Parameters:
        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            The users that will receive the Telegram Premium subscriptions.

        currency (``str``):
            Three-letter ISO 4217 currency code

        amount (``int`` ``64-bit``):
            Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        boost_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            If set, the gifts will be sent on behalf of a channel we are an admin of, which will also assign some boosts to it. Otherwise, the gift will be sent directly from the currently logged in users, and we will gain some extra boost slots. See here » for more info on giveaways and gifts.

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["users", "currency", "amount", "boost_peer", "message"]

    ID = 0xfb790393
    QUALNAME = "types.InputStorePaymentPremiumGiftCode"

    def __init__(self, *, users: List["raw.base.InputUser"], currency: str, amount: int, boost_peer: "raw.base.InputPeer" = None, message: "raw.base.TextWithEntities" = None) -> None:
        self.users = users  # Vector<InputUser>
        self.currency = currency  # string
        self.amount = amount  # long
        self.boost_peer = boost_peer  # flags.0?InputPeer
        self.message = message  # flags.1?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumGiftCode":

        flags = Int.read(b)

        users = TLObject.read(b)

        boost_peer = TLObject.read(b) if flags & (1 << 0) else None

        currency = String.read(b)

        amount = Long.read(b)

        message = TLObject.read(b) if flags & (1 << 1) else None

        return InputStorePaymentPremiumGiftCode(users=users, currency=currency, amount=amount, boost_peer=boost_peer, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.boost_peer is not None else 0
        flags |= (1 << 1) if self.message is not None else 0
        b.write(Int(flags))

        b.write(Vector(self.users))

        if self.boost_peer is not None:
            b.write(self.boost_peer.write())

        b.write(String(self.currency))

        b.write(Long(self.amount))

        if self.message is not None:
            b.write(self.message.write())

        return b.getvalue()
