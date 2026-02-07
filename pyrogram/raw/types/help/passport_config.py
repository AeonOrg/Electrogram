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


class PassportConfig(TLObject):  # type: ignore
    """Telegram passport configuration

    Constructor of :obj:`~pyrogram.raw.base.help.PassportConfig`.

    Details:
        - Layer: ``224``
        - ID: ``A098D6AF``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

        countries_langs (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            Localization

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPassportConfig
    """

    __slots__: List[str] = ["hash", "countries_langs"]

    ID = 0xa098d6af
    QUALNAME = "types.help.PassportConfig"

    def __init__(self, *, hash: int, countries_langs: "raw.base.DataJSON") -> None:
        self.hash = hash  # int
        self.countries_langs = countries_langs  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PassportConfig":
        # No flags

        hash = Int.read(b)

        countries_langs = TLObject.read(b)

        return PassportConfig(hash=hash, countries_langs=countries_langs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.hash))

        b.write(self.countries_langs.write())

        return b.getvalue()
