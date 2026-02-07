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


class SentCodeTypeMissedCall(TLObject):  # type: ignore
    """The code will be sent via a flash phone call, that will be closed immediately. The last digits of the phone number that calls are the code that must be entered manually by the user.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``82006484``

    Parameters:
        prefix (``str``):
            Prefix of the phone number from which the call will be made

        length (``int`` ``32-bit``):
            Length of the verification code

    """

    __slots__: List[str] = ["prefix", "length"]

    ID = 0x82006484
    QUALNAME = "types.auth.SentCodeTypeMissedCall"

    def __init__(self, *, prefix: str, length: int) -> None:
        self.prefix = prefix  # string
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeMissedCall":
        # No flags

        prefix = String.read(b)

        length = Int.read(b)

        return SentCodeTypeMissedCall(prefix=prefix, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(String(self.prefix))

        b.write(Int(self.length))

        return b.getvalue()
