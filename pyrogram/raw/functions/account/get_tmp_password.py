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


class GetTmpPassword(TLObject):  # type: ignore
    """Get temporary payment password


    Details:
        - Layer: ``224``
        - ID: ``449E0B51``

    Parameters:
        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            SRP password parameters

        period (``int`` ``32-bit``):
            Time during which the temporary password will be valid, in seconds; should be between 60 and 86400

    Returns:
        :obj:`account.TmpPassword <pyrogram.raw.base.account.TmpPassword>`
    """

    __slots__: List[str] = ["password", "period"]

    ID = 0x449e0b51
    QUALNAME = "functions.account.GetTmpPassword"

    def __init__(self, *, password: "raw.base.InputCheckPasswordSRP", period: int) -> None:
        self.password = password  # InputCheckPasswordSRP
        self.period = period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTmpPassword":
        # No flags

        password = TLObject.read(b)

        period = Int.read(b)

        return GetTmpPassword(password=password, period=period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.password.write())

        b.write(Int(self.period))

        return b.getvalue()
