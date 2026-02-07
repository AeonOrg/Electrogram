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


class InputStarsTransaction(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStarsTransaction`.

    Details:
        - Layer: ``224``
        - ID: ``206AE6D1``

    Parameters:
        id (``str``):
            N/A

        refund (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "refund"]

    ID = 0x206ae6d1
    QUALNAME = "types.InputStarsTransaction"

    def __init__(self, *, id: str, refund: Optional[bool] = None) -> None:
        self.id = id  # string
        self.refund = refund  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStarsTransaction":

        flags = Int.read(b)

        refund = True if flags & (1 << 0) else False
        id = String.read(b)

        return InputStarsTransaction(id=id, refund=refund)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.refund else 0
        b.write(Int(flags))

        b.write(String(self.id))

        return b.getvalue()
