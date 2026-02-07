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


class PhoneCallDiscardReasonBusy(TLObject):  # type: ignore
    """The phone call was discarded because the user is busy in another call

    Constructor of :obj:`~pyrogram.raw.base.PhoneCallDiscardReason`.

    Details:
        - Layer: ``224``
        - ID: ``FAF7E8C9``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xfaf7e8c9
    QUALNAME = "types.PhoneCallDiscardReasonBusy"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallDiscardReasonBusy":
        # No flags

        return PhoneCallDiscardReasonBusy()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
