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


class StarGiftUpgradeAttributes(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.StarGiftUpgradeAttributes`.

    Details:
        - Layer: ``224``
        - ID: ``46C6E36F``

    Parameters:
        attributes (List of :obj:`StarGiftAttribute <pyrogram.raw.base.StarGiftAttribute>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftUpgradeAttributes
    """

    __slots__: List[str] = ["attributes"]

    ID = 0x46c6e36f
    QUALNAME = "types.payments.StarGiftUpgradeAttributes"

    def __init__(self, *, attributes: List["raw.base.StarGiftAttribute"]) -> None:
        self.attributes = attributes  # Vector<StarGiftAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftUpgradeAttributes":
        # No flags

        attributes = TLObject.read(b)

        return StarGiftUpgradeAttributes(attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Vector(self.attributes))

        return b.getvalue()
