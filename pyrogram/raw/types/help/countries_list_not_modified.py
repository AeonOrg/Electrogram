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


class CountriesListNotModified(TLObject):  # type: ignore
    """The country list has not changed

    Constructor of :obj:`~pyrogram.raw.base.help.CountriesList`.

    Details:
        - Layer: ``224``
        - ID: ``93CC1F32``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetCountriesList
    """

    __slots__: List[str] = []

    ID = 0x93cc1f32
    QUALNAME = "types.help.CountriesListNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CountriesListNotModified":
        # No flags

        return CountriesListNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
