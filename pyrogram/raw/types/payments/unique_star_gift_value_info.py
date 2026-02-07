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


class UniqueStarGiftValueInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.UniqueStarGiftValueInfo`.

    Details:
        - Layer: ``224``
        - ID: ``512FE446``

    Parameters:
        currency (``str``):
            N/A

        value (``int`` ``64-bit``):
            N/A

        initial_sale_date (``int`` ``32-bit``):
            N/A

        initial_sale_stars (``int`` ``64-bit``):
            N/A

        initial_sale_price (``int`` ``64-bit``):
            N/A

        last_sale_on_fragment (``bool``, *optional*):
            N/A

        value_is_average (``bool``, *optional*):
            N/A

        last_sale_date (``int`` ``32-bit``, *optional*):
            N/A

        last_sale_price (``int`` ``64-bit``, *optional*):
            N/A

        floor_price (``int`` ``64-bit``, *optional*):
            N/A

        average_price (``int`` ``64-bit``, *optional*):
            N/A

        listed_count (``int`` ``32-bit``, *optional*):
            N/A

        fragment_listed_count (``int`` ``32-bit``, *optional*):
            N/A

        fragment_listed_url (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetUniqueStarGiftValueInfo
    """

    __slots__: List[str] = ["currency", "value", "initial_sale_date", "initial_sale_stars", "initial_sale_price", "last_sale_on_fragment", "value_is_average", "last_sale_date", "last_sale_price", "floor_price", "average_price", "listed_count", "fragment_listed_count", "fragment_listed_url"]

    ID = 0x512fe446
    QUALNAME = "types.payments.UniqueStarGiftValueInfo"

    def __init__(self, *, currency: str, value: int, initial_sale_date: int, initial_sale_stars: int, initial_sale_price: int, last_sale_on_fragment: Optional[bool] = None, value_is_average: Optional[bool] = None, last_sale_date: Optional[int] = None, last_sale_price: Optional[int] = None, floor_price: Optional[int] = None, average_price: Optional[int] = None, listed_count: Optional[int] = None, fragment_listed_count: Optional[int] = None, fragment_listed_url: Optional[str] = None) -> None:
        self.currency = currency  # string
        self.value = value  # long
        self.initial_sale_date = initial_sale_date  # int
        self.initial_sale_stars = initial_sale_stars  # long
        self.initial_sale_price = initial_sale_price  # long
        self.last_sale_on_fragment = last_sale_on_fragment  # flags.1?true
        self.value_is_average = value_is_average  # flags.6?true
        self.last_sale_date = last_sale_date  # flags.0?int
        self.last_sale_price = last_sale_price  # flags.0?long
        self.floor_price = floor_price  # flags.2?long
        self.average_price = average_price  # flags.3?long
        self.listed_count = listed_count  # flags.4?int
        self.fragment_listed_count = fragment_listed_count  # flags.5?int
        self.fragment_listed_url = fragment_listed_url  # flags.5?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UniqueStarGiftValueInfo":

        flags = Int.read(b)

        last_sale_on_fragment = True if flags & (1 << 1) else False
        value_is_average = True if flags & (1 << 6) else False
        currency = String.read(b)

        value = Long.read(b)

        initial_sale_date = Int.read(b)

        initial_sale_stars = Long.read(b)

        initial_sale_price = Long.read(b)

        last_sale_date = Int.read(b) if flags & (1 << 0) else None
        last_sale_price = Long.read(b) if flags & (1 << 0) else None
        floor_price = Long.read(b) if flags & (1 << 2) else None
        average_price = Long.read(b) if flags & (1 << 3) else None
        listed_count = Int.read(b) if flags & (1 << 4) else None
        fragment_listed_count = Int.read(b) if flags & (1 << 5) else None
        fragment_listed_url = String.read(b) if flags & (1 << 5) else None
        return UniqueStarGiftValueInfo(currency=currency, value=value, initial_sale_date=initial_sale_date, initial_sale_stars=initial_sale_stars, initial_sale_price=initial_sale_price, last_sale_on_fragment=last_sale_on_fragment, value_is_average=value_is_average, last_sale_date=last_sale_date, last_sale_price=last_sale_price, floor_price=floor_price, average_price=average_price, listed_count=listed_count, fragment_listed_count=fragment_listed_count, fragment_listed_url=fragment_listed_url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.last_sale_on_fragment else 0
        flags |= (1 << 6) if self.value_is_average else 0
        flags |= (1 << 0) if self.last_sale_date is not None else 0
        flags |= (1 << 0) if self.last_sale_price is not None else 0
        flags |= (1 << 2) if self.floor_price is not None else 0
        flags |= (1 << 3) if self.average_price is not None else 0
        flags |= (1 << 4) if self.listed_count is not None else 0
        flags |= (1 << 5) if self.fragment_listed_count is not None else 0
        flags |= (1 << 5) if self.fragment_listed_url is not None else 0
        b.write(Int(flags))

        b.write(String(self.currency))

        b.write(Long(self.value))

        b.write(Int(self.initial_sale_date))

        b.write(Long(self.initial_sale_stars))

        b.write(Long(self.initial_sale_price))

        if self.last_sale_date is not None:
            b.write(Int(self.last_sale_date))

        if self.last_sale_price is not None:
            b.write(Long(self.last_sale_price))

        if self.floor_price is not None:
            b.write(Long(self.floor_price))

        if self.average_price is not None:
            b.write(Long(self.average_price))

        if self.listed_count is not None:
            b.write(Int(self.listed_count))

        if self.fragment_listed_count is not None:
            b.write(Int(self.fragment_listed_count))

        if self.fragment_listed_url is not None:
            b.write(String(self.fragment_listed_url))

        return b.getvalue()
