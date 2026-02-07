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


class BusinessAwayMessageScheduleOutsideWorkHours(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.BusinessAwayMessageSchedule`.

    Details:
        - Layer: ``224``
        - ID: ``C3F2F501``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xc3f2f501
    QUALNAME = "types.BusinessAwayMessageScheduleOutsideWorkHours"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessAwayMessageScheduleOutsideWorkHours":
        # No flags

        return BusinessAwayMessageScheduleOutsideWorkHours()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
