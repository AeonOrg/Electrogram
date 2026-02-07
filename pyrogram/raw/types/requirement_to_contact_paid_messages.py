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


class RequirementToContactPaidMessages(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RequirementToContact`.

    Details:
        - Layer: ``224``
        - ID: ``B4F67E93``

    Parameters:
        stars_amount (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            users.GetRequirementsToContact
    """

    __slots__: List[str] = ["stars_amount"]

    ID = 0xb4f67e93
    QUALNAME = "types.RequirementToContactPaidMessages"

    def __init__(self, *, stars_amount: int) -> None:
        self.stars_amount = stars_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequirementToContactPaidMessages":
        # No flags

        stars_amount = Long.read(b)

        return RequirementToContactPaidMessages(stars_amount=stars_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.stars_amount))

        return b.getvalue()
