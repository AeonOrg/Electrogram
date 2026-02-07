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


class PromoDataEmpty(TLObject):  # type: ignore
    """No PSA/MTProxy info is available

    Constructor of :obj:`~pyrogram.raw.base.help.PromoData`.

    Details:
        - Layer: ``224``
        - ID: ``98F6AC75``

    Parameters:
        expires (``int`` ``32-bit``):
            Re-fetch PSA/MTProxy info after the specified number of seconds

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPromoData
    """

    __slots__: List[str] = ["expires"]

    ID = 0x98f6ac75
    QUALNAME = "types.help.PromoDataEmpty"

    def __init__(self, *, expires: int) -> None:
        self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PromoDataEmpty":
        # No flags

        expires = Int.read(b)

        return PromoDataEmpty(expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.expires))

        return b.getvalue()
