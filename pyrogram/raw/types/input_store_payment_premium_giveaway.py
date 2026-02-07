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


class InputStorePaymentPremiumGiveaway(TLObject):  # type: ignore
    """Used to pay for a giveaway, see here » for more info.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``160544CA``

    Parameters:
        boost_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The channel starting the giveaway, that the user must join to participate, that will receive the giveaway boosts; see here » for more info on giveaways.

        random_id (``int`` ``64-bit``):
            Random ID to avoid resending the giveaway

        until_date (``int`` ``32-bit``):
            The end date of the giveaway, must be at most giveaway_period_max seconds in the future; see here » for more info on giveaways.

        currency (``str``):
            Three-letter ISO 4217 currency code

        amount (``int`` ``64-bit``):
            Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        only_new_subscribers (``bool``, *optional*):
            If set, only new subscribers starting from the giveaway creation date will be able to participate to the giveaway.

        winners_are_visible (``bool``, *optional*):
            If set, giveaway winners are public and will be listed in a messageMediaGiveawayResults message that will be automatically sent to the channel once the giveaway ends.

        additional_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Additional channels that the user must join to participate to the giveaway can be specified here.

        countries_iso2 (List of ``str``, *optional*):
            The set of users that can participate to the giveaway can be restricted by passing here an explicit whitelist of up to giveaway_countries_max countries, specified as two-letter ISO 3166-1 alpha-2 country codes.

        prize_description (``str``, *optional*):
            Can contain a textual description of additional giveaway prizes.

    """

    __slots__: List[str] = ["boost_peer", "random_id", "until_date", "currency", "amount", "only_new_subscribers", "winners_are_visible", "additional_peers", "countries_iso2", "prize_description"]

    ID = 0x160544ca
    QUALNAME = "types.InputStorePaymentPremiumGiveaway"

    def __init__(self, *, boost_peer: "raw.base.InputPeer", random_id: int, until_date: int, currency: str, amount: int, only_new_subscribers: Optional[bool] = None, winners_are_visible: Optional[bool] = None, additional_peers: Optional[List["raw.base.InputPeer"]] = None, countries_iso2: Optional[List[str]] = None, prize_description: Optional[str] = None) -> None:
        self.boost_peer = boost_peer  # InputPeer
        self.random_id = random_id  # long
        self.until_date = until_date  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.only_new_subscribers = only_new_subscribers  # flags.0?true
        self.winners_are_visible = winners_are_visible  # flags.3?true
        self.additional_peers = additional_peers  # flags.1?Vector<InputPeer>
        self.countries_iso2 = countries_iso2  # flags.2?Vector<string>
        self.prize_description = prize_description  # flags.4?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumGiveaway":

        flags = Int.read(b)

        only_new_subscribers = True if flags & (1 << 0) else False
        winners_are_visible = True if flags & (1 << 3) else False
        boost_peer = TLObject.read(b)

        additional_peers = TLObject.read(b) if flags & (1 << 1) else []

        countries_iso2 = TLObject.read(b, String) if flags & (1 << 2) else []

        prize_description = String.read(b) if flags & (1 << 4) else None
        random_id = Long.read(b)

        until_date = Int.read(b)

        currency = String.read(b)

        amount = Long.read(b)

        return InputStorePaymentPremiumGiveaway(boost_peer=boost_peer, random_id=random_id, until_date=until_date, currency=currency, amount=amount, only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, additional_peers=additional_peers, countries_iso2=countries_iso2, prize_description=prize_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_new_subscribers else 0
        flags |= (1 << 3) if self.winners_are_visible else 0
        flags |= (1 << 1) if self.additional_peers else 0
        flags |= (1 << 2) if self.countries_iso2 else 0
        flags |= (1 << 4) if self.prize_description is not None else 0
        b.write(Int(flags))

        b.write(self.boost_peer.write())

        if self.additional_peers is not None:
            b.write(Vector(self.additional_peers))

        if self.countries_iso2 is not None:
            b.write(Vector(self.countries_iso2, String))

        if self.prize_description is not None:
            b.write(String(self.prize_description))

        b.write(Long(self.random_id))

        b.write(Int(self.until_date))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        return b.getvalue()
