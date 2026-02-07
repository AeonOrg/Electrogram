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


class StarGiftUpgradePreview(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftUpgradePreview`.

    Details:
        - Layer: ``224``
        - ID: ``3DE1DFED``

    Parameters:
        sample_attributes (List of :obj:`StarGiftAttribute <pyrogram.raw.base.StarGiftAttribute>`):
            N/A

        prices (List of :obj:`StarGiftUpgradePrice <pyrogram.raw.base.StarGiftUpgradePrice>`):
            N/A

        next_prices (List of :obj:`StarGiftUpgradePrice <pyrogram.raw.base.StarGiftUpgradePrice>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftUpgradePreview
    """

    __slots__: List[str] = ["sample_attributes", "prices", "next_prices"]

    ID = 0x3de1dfed
    QUALNAME = "types.payments.StarGiftUpgradePreview"

    def __init__(self, *, sample_attributes: List["raw.base.StarGiftAttribute"], prices: List["raw.base.StarGiftUpgradePrice"], next_prices: List["raw.base.StarGiftUpgradePrice"]) -> None:
        self.sample_attributes = sample_attributes  # Vector<StarGiftAttribute>
        self.prices = prices  # Vector<StarGiftUpgradePrice>
        self.next_prices = next_prices  # Vector<StarGiftUpgradePrice>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftUpgradePreview":
        # No flags

        sample_attributes = TLObject.read(b)

        prices = TLObject.read(b)

        next_prices = TLObject.read(b)

        return StarGiftUpgradePreview(sample_attributes=sample_attributes, prices=prices, next_prices=next_prices)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.sample_attributes))

        b.write(Vector(self.prices))

        b.write(Vector(self.next_prices))

        return b.getvalue()
