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


class Invoice(TLObject):  # type: ignore
    """Invoice

    Constructor of :obj:`~pyrogram.raw.base.Invoice`.

    Details:
        - Layer: ``224``
        - ID: ``49EE584``

    Parameters:
        currency (``str``):
            Three-letter ISO 4217 currency code

        prices (List of :obj:`LabeledPrice <pyrogram.raw.base.LabeledPrice>`):
            Price breakdown, a list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)

        test (``bool``, *optional*):
            Test invoice

        name_requested (``bool``, *optional*):
            Set this flag if you require the user's full name to complete the order

        phone_requested (``bool``, *optional*):
            Set this flag if you require the user's phone number to complete the order

        email_requested (``bool``, *optional*):
            Set this flag if you require the user's email address to complete the order

        shipping_address_requested (``bool``, *optional*):
            Set this flag if you require the user's shipping address to complete the order

        flexible (``bool``, *optional*):
            Set this flag if the final price depends on the shipping method

        phone_to_provider (``bool``, *optional*):
            Set this flag if user's phone number should be sent to provider

        email_to_provider (``bool``, *optional*):
            Set this flag if user's email address should be sent to provider

        recurring (``bool``, *optional*):
            Whether this is a recurring payment

        max_tip_amount (``int`` ``64-bit``, *optional*):
            The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        suggested_tip_amounts (List of ``int`` ``64-bit``, *optional*):
            A vector of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.

        terms_url (``str``, *optional*):
            Terms of service URL

        subscription_period (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["currency", "prices", "test", "name_requested", "phone_requested", "email_requested", "shipping_address_requested", "flexible", "phone_to_provider", "email_to_provider", "recurring", "max_tip_amount", "suggested_tip_amounts", "terms_url", "subscription_period"]

    ID = 0x49ee584
    QUALNAME = "types.Invoice"

    def __init__(self, *, currency: str, prices: List["raw.base.LabeledPrice"], test: Optional[bool] = None, name_requested: Optional[bool] = None, phone_requested: Optional[bool] = None, email_requested: Optional[bool] = None, shipping_address_requested: Optional[bool] = None, flexible: Optional[bool] = None, phone_to_provider: Optional[bool] = None, email_to_provider: Optional[bool] = None, recurring: Optional[bool] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: Optional[List[int]] = None, terms_url: Optional[str] = None, subscription_period: Optional[int] = None) -> None:
        self.currency = currency  # string
        self.prices = prices  # Vector<LabeledPrice>
        self.test = test  # flags.0?true
        self.name_requested = name_requested  # flags.1?true
        self.phone_requested = phone_requested  # flags.2?true
        self.email_requested = email_requested  # flags.3?true
        self.shipping_address_requested = shipping_address_requested  # flags.4?true
        self.flexible = flexible  # flags.5?true
        self.phone_to_provider = phone_to_provider  # flags.6?true
        self.email_to_provider = email_to_provider  # flags.7?true
        self.recurring = recurring  # flags.9?true
        self.max_tip_amount = max_tip_amount  # flags.8?long
        self.suggested_tip_amounts = suggested_tip_amounts  # flags.8?Vector<long>
        self.terms_url = terms_url  # flags.10?string
        self.subscription_period = subscription_period  # flags.11?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Invoice":

        flags = Int.read(b)

        test = True if flags & (1 << 0) else False
        name_requested = True if flags & (1 << 1) else False
        phone_requested = True if flags & (1 << 2) else False
        email_requested = True if flags & (1 << 3) else False
        shipping_address_requested = True if flags & (1 << 4) else False
        flexible = True if flags & (1 << 5) else False
        phone_to_provider = True if flags & (1 << 6) else False
        email_to_provider = True if flags & (1 << 7) else False
        recurring = True if flags & (1 << 9) else False
        currency = String.read(b)

        prices = TLObject.read(b)

        max_tip_amount = Long.read(b) if flags & (1 << 8) else None
        suggested_tip_amounts = TLObject.read(b, Long) if flags & (1 << 8) else []

        terms_url = String.read(b) if flags & (1 << 10) else None
        subscription_period = Int.read(b) if flags & (1 << 11) else None
        return Invoice(currency=currency, prices=prices, test=test, name_requested=name_requested, phone_requested=phone_requested, email_requested=email_requested, shipping_address_requested=shipping_address_requested, flexible=flexible, phone_to_provider=phone_to_provider, email_to_provider=email_to_provider, recurring=recurring, max_tip_amount=max_tip_amount, suggested_tip_amounts=suggested_tip_amounts, terms_url=terms_url, subscription_period=subscription_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.test else 0
        flags |= (1 << 1) if self.name_requested else 0
        flags |= (1 << 2) if self.phone_requested else 0
        flags |= (1 << 3) if self.email_requested else 0
        flags |= (1 << 4) if self.shipping_address_requested else 0
        flags |= (1 << 5) if self.flexible else 0
        flags |= (1 << 6) if self.phone_to_provider else 0
        flags |= (1 << 7) if self.email_to_provider else 0
        flags |= (1 << 9) if self.recurring else 0
        flags |= (1 << 8) if self.max_tip_amount is not None else 0
        flags |= (1 << 8) if self.suggested_tip_amounts else 0
        flags |= (1 << 10) if self.terms_url is not None else 0
        flags |= (1 << 11) if self.subscription_period is not None else 0
        b.write(Int(flags))

        b.write(String(self.currency))

        b.write(Vector(self.prices))

        if self.max_tip_amount is not None:
            b.write(Long(self.max_tip_amount))

        if self.suggested_tip_amounts is not None:
            b.write(Vector(self.suggested_tip_amounts, Long))

        if self.terms_url is not None:
            b.write(String(self.terms_url))

        if self.subscription_period is not None:
            b.write(Int(self.subscription_period))

        return b.getvalue()
