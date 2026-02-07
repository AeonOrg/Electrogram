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


class InputInvoicePremiumGiftStars(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``DABAB2EF``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        months (``int`` ``32-bit``):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "months", "message"]

    ID = 0xdabab2ef
    QUALNAME = "types.InputInvoicePremiumGiftStars"

    def __init__(self, *, user_id: "raw.base.InputUser", months: int, message: "raw.base.TextWithEntities" = None) -> None:
        self.user_id = user_id  # InputUser
        self.months = months  # int
        self.message = message  # flags.0?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoicePremiumGiftStars":

        flags = Int.read(b)

        user_id = TLObject.read(b)

        months = Int.read(b)

        message = TLObject.read(b) if flags & (1 << 0) else None

        return InputInvoicePremiumGiftStars(user_id=user_id, months=months, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.message is not None else 0
        b.write(Int(flags))

        b.write(self.user_id.write())

        b.write(Int(self.months))

        if self.message is not None:
            b.write(self.message.write())

        return b.getvalue()
