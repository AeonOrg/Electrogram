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


class PaymentCharge(TLObject):  # type: ignore
    """Payment identifier

    Constructor of :obj:`~pyrogram.raw.base.PaymentCharge`.

    Details:
        - Layer: ``224``
        - ID: ``EA02C27E``

    Parameters:
        id (``str``):
            Telegram payment identifier

        provider_charge_id (``str``):
            Provider payment identifier

    """

    __slots__: List[str] = ["id", "provider_charge_id"]

    ID = 0xea02c27e
    QUALNAME = "types.PaymentCharge"

    def __init__(self, *, id: str, provider_charge_id: str) -> None:
        self.id = id  # string
        self.provider_charge_id = provider_charge_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentCharge":
        # No flags

        id = String.read(b)

        provider_charge_id = String.read(b)

        return PaymentCharge(id=id, provider_charge_id=provider_charge_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.id))

        b.write(String(self.provider_charge_id))

        return b.getvalue()
