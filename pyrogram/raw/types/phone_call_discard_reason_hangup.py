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


class PhoneCallDiscardReasonHangup(TLObject):  # type: ignore
    """The phone call was ended normally

    Constructor of :obj:`~pyrogram.raw.base.PhoneCallDiscardReason`.

    Details:
        - Layer: ``224``
        - ID: ``57ADC690``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x57adc690
    QUALNAME = "types.PhoneCallDiscardReasonHangup"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallDiscardReasonHangup":
        # No flags

        return PhoneCallDiscardReasonHangup()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
