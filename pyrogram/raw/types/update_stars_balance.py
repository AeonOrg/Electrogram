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


class UpdateStarsBalance(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``4E80A379``

    Parameters:
        balance (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):


    """

    __slots__: List[str] = ["balance"]

    ID = 0x4e80a379
    QUALNAME = "types.UpdateStarsBalance"

    def __init__(self, *, balance: "raw.base.StarsAmount") -> None:
        self.balance = balance  # StarsAmount

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarsBalance":
        # No flags

        balance = TLObject.read(b)

        return UpdateStarsBalance(balance=balance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.balance.write())

        return b.getvalue()
