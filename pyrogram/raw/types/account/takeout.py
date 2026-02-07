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


class Takeout(TLObject):  # type: ignore
    """Takeout info

    Constructor of :obj:`~pyrogram.raw.base.account.Takeout`.

    Details:
        - Layer: ``224``
        - ID: ``4DBA4501``

    Parameters:
        id (``int`` ``64-bit``):
            Takeout ID

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.InitTakeoutSession
    """

    __slots__: List[str] = ["id"]

    ID = 0x4dba4501
    QUALNAME = "types.account.Takeout"

    def __init__(self, *, id: int) -> None:
        self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Takeout":
        # No flags

        id = Long.read(b)

        return Takeout(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.id))

        return b.getvalue()
