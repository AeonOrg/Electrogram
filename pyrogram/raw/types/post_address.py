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


class PostAddress(TLObject):  # type: ignore
    """Shipping address

    Constructor of :obj:`~pyrogram.raw.base.PostAddress`.

    Details:
        - Layer: ``224``
        - ID: ``1E8CAAEB``

    Parameters:
        street_line1 (``str``):
            First line for the address

        street_line2 (``str``):
            Second line for the address

        city (``str``):
            City

        state (``str``):
            State, if applicable (empty otherwise)

        country_iso2 (``str``):
            ISO 3166-1 alpha-2 country code

        post_code (``str``):
            Address post code

    """

    __slots__: List[str] = ["street_line1", "street_line2", "city", "state", "country_iso2", "post_code"]

    ID = 0x1e8caaeb
    QUALNAME = "types.PostAddress"

    def __init__(self, *, street_line1: str, street_line2: str, city: str, state: str, country_iso2: str, post_code: str) -> None:
        self.street_line1 = street_line1  # string
        self.street_line2 = street_line2  # string
        self.city = city  # string
        self.state = state  # string
        self.country_iso2 = country_iso2  # string
        self.post_code = post_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PostAddress":
        # No flags

        street_line1 = String.read(b)

        street_line2 = String.read(b)

        city = String.read(b)

        state = String.read(b)

        country_iso2 = String.read(b)

        post_code = String.read(b)

        return PostAddress(street_line1=street_line1, street_line2=street_line2, city=city, state=state, country_iso2=country_iso2, post_code=post_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.street_line1))

        b.write(String(self.street_line2))

        b.write(String(self.city))

        b.write(String(self.state))

        b.write(String(self.country_iso2))

        b.write(String(self.post_code))

        return b.getvalue()
