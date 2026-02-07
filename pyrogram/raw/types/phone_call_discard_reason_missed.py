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


class PhoneCallDiscardReasonMissed(TLObject):  # type: ignore
    """The phone call was missed

    Constructor of :obj:`~pyrogram.raw.base.PhoneCallDiscardReason`.

    Details:
        - Layer: ``224``
        - ID: ``85E42301``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x85e42301
    QUALNAME = "types.PhoneCallDiscardReasonMissed"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallDiscardReasonMissed":
        # No flags

        return PhoneCallDiscardReasonMissed()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
