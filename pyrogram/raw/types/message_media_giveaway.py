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


class MessageMediaGiveaway(TLObject):  # type: ignore
    """Contains info about a giveaway, see here » for more info.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``AA073BEB``

    Parameters:
        channels (List of ``int`` ``64-bit``):
            The channels that the user must join to participate in the giveaway.

        quantity (``int`` ``32-bit``):
            Number of Telegram Premium subscriptions given away.

        until_date (``int`` ``32-bit``):
            The end date of the giveaway.

        only_new_subscribers (``bool``, *optional*):
            If set, only new subscribers starting from the giveaway creation date will be able to participate to the giveaway.

        winners_are_visible (``bool``, *optional*):
            If set, giveaway winners are public and will be listed in a messageMediaGiveawayResults message that will be automatically sent to the channel once the giveaway ends.

        countries_iso2 (List of ``str``, *optional*):
            If set, only users residing in these countries can participate in the giveaway, (specified as a list of two-letter ISO 3166-1 alpha-2 country codes); otherwise there are no country-based limitations.

        prize_description (``str``, *optional*):
            Can contain a textual description of additional giveaway prizes.

        months (``int`` ``32-bit``, *optional*):
            Duration in months of each Telegram Premium subscription in the giveaway.

        stars (``int`` ``64-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["channels", "quantity", "until_date", "only_new_subscribers", "winners_are_visible", "countries_iso2", "prize_description", "months", "stars"]

    ID = 0xaa073beb
    QUALNAME = "types.MessageMediaGiveaway"

    def __init__(self, *, channels: List[int], quantity: int, until_date: int, only_new_subscribers: Optional[bool] = None, winners_are_visible: Optional[bool] = None, countries_iso2: Optional[List[str]] = None, prize_description: Optional[str] = None, months: Optional[int] = None, stars: Optional[int] = None) -> None:
        self.channels = channels  # Vector<long>
        self.quantity = quantity  # int
        self.until_date = until_date  # int
        self.only_new_subscribers = only_new_subscribers  # flags.0?true
        self.winners_are_visible = winners_are_visible  # flags.2?true
        self.countries_iso2 = countries_iso2  # flags.1?Vector<string>
        self.prize_description = prize_description  # flags.3?string
        self.months = months  # flags.4?int
        self.stars = stars  # flags.5?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGiveaway":

        flags = Int.read(b)

        only_new_subscribers = True if flags & (1 << 0) else False
        winners_are_visible = True if flags & (1 << 2) else False
        channels = TLObject.read(b, Long)

        countries_iso2 = TLObject.read(b, String) if flags & (1 << 1) else []

        prize_description = String.read(b) if flags & (1 << 3) else None
        quantity = Int.read(b)

        months = Int.read(b) if flags & (1 << 4) else None
        stars = Long.read(b) if flags & (1 << 5) else None
        until_date = Int.read(b)

        return MessageMediaGiveaway(channels=channels, quantity=quantity, until_date=until_date, only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, countries_iso2=countries_iso2, prize_description=prize_description, months=months, stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_new_subscribers else 0
        flags |= (1 << 2) if self.winners_are_visible else 0
        flags |= (1 << 1) if self.countries_iso2 else 0
        flags |= (1 << 3) if self.prize_description is not None else 0
        flags |= (1 << 4) if self.months is not None else 0
        flags |= (1 << 5) if self.stars is not None else 0
        b.write(Int(flags))

        b.write(Vector(self.channels, Long))

        if self.countries_iso2 is not None:
            b.write(Vector(self.countries_iso2, String))

        if self.prize_description is not None:
            b.write(String(self.prize_description))

        b.write(Int(self.quantity))

        if self.months is not None:
            b.write(Int(self.months))

        if self.stars is not None:
            b.write(Long(self.stars))

        b.write(Int(self.until_date))

        return b.getvalue()
