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


class Country(TLObject):  # type: ignore
    """Name, ISO code, localized name and phone codes/patterns of a specific country

    Constructor of :obj:`~pyrogram.raw.base.help.Country`.

    Details:
        - Layer: ``224``
        - ID: ``C3878E23``

    Parameters:
        iso2 (``str``):
            ISO code of country

        default_name (``str``):
            Name of the country in the country's language

        country_codes (List of :obj:`help.CountryCode <pyrogram.raw.base.help.CountryCode>`):
            Phone codes/patterns

        hidden (``bool``, *optional*):
            Whether this country should not be shown in the list

        name (``str``, *optional*):
            Name of the country in the user's language, if different from the original name

    """

    __slots__: List[str] = ["iso2", "default_name", "country_codes", "hidden", "name"]

    ID = 0xc3878e23
    QUALNAME = "types.help.Country"

    def __init__(self, *, iso2: str, default_name: str, country_codes: List["raw.base.help.CountryCode"], hidden: Optional[bool] = None, name: Optional[str] = None) -> None:
        self.iso2 = iso2  # string
        self.default_name = default_name  # string
        self.country_codes = country_codes  # Vector<help.CountryCode>
        self.hidden = hidden  # flags.0?true
        self.name = name  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Country":

        flags = Int.read(b)

        hidden = True if flags & (1 << 0) else False
        iso2 = String.read(b)

        default_name = String.read(b)

        name = String.read(b) if flags & (1 << 1) else None
        country_codes = TLObject.read(b)

        return Country(iso2=iso2, default_name=default_name, country_codes=country_codes, hidden=hidden, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.hidden else 0
        flags |= (1 << 1) if self.name is not None else 0
        b.write(Int(flags))

        b.write(String(self.iso2))

        b.write(String(self.default_name))

        if self.name is not None:
            b.write(String(self.name))

        b.write(Vector(self.country_codes))

        return b.getvalue()
