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


class RefundStarsCharge(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``25AE8F4A``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):


        charge_id (``str``):


    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["user_id", "charge_id"]

    ID = 0x25ae8f4a
    QUALNAME = "functions.payments.RefundStarsCharge"

    def __init__(self, *, user_id: "raw.base.InputUser", charge_id: str) -> None:
        self.user_id = user_id  # InputUser
        self.charge_id = charge_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RefundStarsCharge":
        # No flags

        user_id = TLObject.read(b)

        charge_id = String.read(b)

        return RefundStarsCharge(user_id=user_id, charge_id=charge_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.user_id.write())

        b.write(String(self.charge_id))

        return b.getvalue()
