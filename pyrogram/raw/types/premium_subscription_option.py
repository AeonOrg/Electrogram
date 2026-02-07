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


class PremiumSubscriptionOption(TLObject):  # type: ignore
    """Describes a Telegram Premium subscription option

    Constructor of :obj:`~pyrogram.raw.base.PremiumSubscriptionOption`.

    Details:
        - Layer: ``224``
        - ID: ``5F2D1DF2``

    Parameters:
        months (``int`` ``32-bit``):
            Duration of subscription in months

        currency (``str``):
            Three-letter ISO 4217 currency code

        amount (``int`` ``64-bit``):
            Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        bot_url (``str``):
            Deep link used to initiate payment

        current (``bool``, *optional*):
            Whether this subscription option is currently in use.

        can_purchase_upgrade (``bool``, *optional*):
            Whether this subscription option can be used to upgrade the existing Telegram Premium subscription. When upgrading Telegram Premium subscriptions bought through stores, make sure that the store transaction ID is equal to transaction, to avoid upgrading someone else's account, if the client is currently logged into multiple accounts.

        transaction (``str``, *optional*):
            Identifier of the last in-store transaction for the currently used subscription on the current account.

        store_product (``str``, *optional*):
            Store product ID, only for official apps

    """

    __slots__: List[str] = ["months", "currency", "amount", "bot_url", "current", "can_purchase_upgrade", "transaction", "store_product"]

    ID = 0x5f2d1df2
    QUALNAME = "types.PremiumSubscriptionOption"

    def __init__(self, *, months: int, currency: str, amount: int, bot_url: str, current: Optional[bool] = None, can_purchase_upgrade: Optional[bool] = None, transaction: Optional[str] = None, store_product: Optional[str] = None) -> None:
        self.months = months  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.bot_url = bot_url  # string
        self.current = current  # flags.1?true
        self.can_purchase_upgrade = can_purchase_upgrade  # flags.2?true
        self.transaction = transaction  # flags.3?string
        self.store_product = store_product  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumSubscriptionOption":

        flags = Int.read(b)

        current = True if flags & (1 << 1) else False
        can_purchase_upgrade = True if flags & (1 << 2) else False
        transaction = String.read(b) if flags & (1 << 3) else None
        months = Int.read(b)

        currency = String.read(b)

        amount = Long.read(b)

        bot_url = String.read(b)

        store_product = String.read(b) if flags & (1 << 0) else None
        return PremiumSubscriptionOption(months=months, currency=currency, amount=amount, bot_url=bot_url, current=current, can_purchase_upgrade=can_purchase_upgrade, transaction=transaction, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.current else 0
        flags |= (1 << 2) if self.can_purchase_upgrade else 0
        flags |= (1 << 3) if self.transaction is not None else 0
        flags |= (1 << 0) if self.store_product is not None else 0
        b.write(Int(flags))

        if self.transaction is not None:
            b.write(String(self.transaction))

        b.write(Int(self.months))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        b.write(String(self.bot_url))

        if self.store_product is not None:
            b.write(String(self.store_product))

        return b.getvalue()
