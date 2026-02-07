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


class InputStorePaymentAuthCode(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``224``
        - ID: ``9BB2636D``

    Parameters:
        phone_number (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        restore (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "currency", "amount", "restore"]

    ID = 0x9bb2636d
    QUALNAME = "types.InputStorePaymentAuthCode"

    def __init__(self, *, phone_number: str, phone_code_hash: str, currency: str, amount: int, restore: Optional[bool] = None) -> None:
        self.phone_number = phone_number  # string
        self.phone_code_hash = phone_code_hash  # string
        self.currency = currency  # string
        self.amount = amount  # long
        self.restore = restore  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentAuthCode":

        flags = Int.read(b)

        restore = True if flags & (1 << 0) else False
        phone_number = String.read(b)

        phone_code_hash = String.read(b)

        currency = String.read(b)

        amount = Long.read(b)

        return InputStorePaymentAuthCode(phone_number=phone_number, phone_code_hash=phone_code_hash, currency=currency, amount=amount, restore=restore)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.restore else 0
        b.write(Int(flags))

        b.write(String(self.phone_number))

        b.write(String(self.phone_code_hash))

        b.write(String(self.currency))

        b.write(Long(self.amount))

        return b.getvalue()
