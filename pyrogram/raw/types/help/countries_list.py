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


class CountriesList(TLObject):  # type: ignore
    """Name, ISO code, localized name and phone codes/patterns of all available countries

    Constructor of :obj:`~pyrogram.raw.base.help.CountriesList`.

    Details:
        - Layer: ``224``
        - ID: ``87D0759E``

    Parameters:
        countries (List of :obj:`help.Country <pyrogram.raw.base.help.Country>`):
            Name, ISO code, localized name and phone codes/patterns of all available countries

        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetCountriesList
    """

    __slots__: List[str] = ["countries", "hash"]

    ID = 0x87d0759e
    QUALNAME = "types.help.CountriesList"

    def __init__(self, *, countries: List["raw.base.help.Country"], hash: int) -> None:
        self.countries = countries  # Vector<help.Country>
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CountriesList":
        # No flags

        countries = TLObject.read(b)

        hash = Int.read(b)

        return CountriesList(countries=countries, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.countries))

        b.write(Int(self.hash))

        return b.getvalue()
