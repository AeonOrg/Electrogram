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


class HistoryImport(TLObject):  # type: ignore
    """ID of a specific chat import session, click here for more info ».

    Constructor of :obj:`~pyrogram.raw.base.messages.HistoryImport`.

    Details:
        - Layer: ``224``
        - ID: ``1662AF0B``

    Parameters:
        id (``int`` ``64-bit``):
            History import ID

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.InitHistoryImport
    """

    __slots__: List[str] = ["id"]

    ID = 0x1662af0b
    QUALNAME = "types.messages.HistoryImport"

    def __init__(self, *, id: int) -> None:
        self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HistoryImport":
        # No flags

        id = Long.read(b)

        return HistoryImport(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        return b.getvalue()
