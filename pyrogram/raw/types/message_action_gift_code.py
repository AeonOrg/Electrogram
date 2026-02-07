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


class MessageActionGiftCode(TLObject):  # type: ignore
    """Contains a Telegram Premium giftcode link.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``31C48347``

    Parameters:
        days (``int`` ``32-bit``):
            N/A

        slug (``str``):
            Slug of the Telegram Premium giftcode link

        via_giveaway (``bool``, *optional*):
            If set, this gift code was received from a giveaway » started by a channel we're subscribed to.

        unclaimed (``bool``, *optional*):
            If set, the link was not redeemed yet.

        boost_peer (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            Identifier of the channel that created the gift code either directly or through a giveaway: if we import this giftcode link, we will also automatically boost this channel.

        currency (``str``, *optional*):
            Three-letter ISO 4217 currency code

        amount (``int`` ``64-bit``, *optional*):
            Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        crypto_currency (``str``, *optional*):
            If set, the gift was made using the specified cryptocurrency.

        crypto_amount (``int`` ``64-bit``, *optional*):
            If crypto_currency is set, contains the paid amount, in the smallest units of the cryptocurrency.

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["days", "slug", "via_giveaway", "unclaimed", "boost_peer", "currency", "amount", "crypto_currency", "crypto_amount", "message"]

    ID = 0x31c48347
    QUALNAME = "types.MessageActionGiftCode"

    def __init__(self, *, days: int, slug: str, via_giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, boost_peer: "raw.base.Peer" = None, currency: Optional[str] = None, amount: Optional[int] = None, crypto_currency: Optional[str] = None, crypto_amount: Optional[int] = None, message: "raw.base.TextWithEntities" = None) -> None:
        self.days = days  # int
        self.slug = slug  # string
        self.via_giveaway = via_giveaway  # flags.0?true
        self.unclaimed = unclaimed  # flags.5?true
        self.boost_peer = boost_peer  # flags.1?Peer
        self.currency = currency  # flags.2?string
        self.amount = amount  # flags.2?long
        self.crypto_currency = crypto_currency  # flags.3?string
        self.crypto_amount = crypto_amount  # flags.3?long
        self.message = message  # flags.4?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiftCode":

        flags = Int.read(b)

        via_giveaway = True if flags & (1 << 0) else False
        unclaimed = True if flags & (1 << 5) else False
        boost_peer = TLObject.read(b) if flags & (1 << 1) else None

        days = Int.read(b)

        slug = String.read(b)

        currency = String.read(b) if flags & (1 << 2) else None
        amount = Long.read(b) if flags & (1 << 2) else None
        crypto_currency = String.read(b) if flags & (1 << 3) else None
        crypto_amount = Long.read(b) if flags & (1 << 3) else None
        message = TLObject.read(b) if flags & (1 << 4) else None

        return MessageActionGiftCode(days=days, slug=slug, via_giveaway=via_giveaway, unclaimed=unclaimed, boost_peer=boost_peer, currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.via_giveaway else 0
        flags |= (1 << 5) if self.unclaimed else 0
        flags |= (1 << 1) if self.boost_peer is not None else 0
        flags |= (1 << 2) if self.currency is not None else 0
        flags |= (1 << 2) if self.amount is not None else 0
        flags |= (1 << 3) if self.crypto_currency is not None else 0
        flags |= (1 << 3) if self.crypto_amount is not None else 0
        flags |= (1 << 4) if self.message is not None else 0
        b.write(Int(flags))

        if self.boost_peer is not None:
            b.write(self.boost_peer.write())

        b.write(Int(self.days))

        b.write(String(self.slug))

        if self.currency is not None:
            b.write(String(self.currency))

        if self.amount is not None:
            b.write(Long(self.amount))

        if self.crypto_currency is not None:
            b.write(String(self.crypto_currency))

        if self.crypto_amount is not None:
            b.write(Long(self.crypto_amount))

        if self.message is not None:
            b.write(self.message.write())

        return b.getvalue()
