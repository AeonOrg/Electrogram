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


class TmpPassword(TLObject):  # type: ignore
    """Temporary payment password

    Constructor of :obj:`~pyrogram.raw.base.account.TmpPassword`.

    Details:
        - Layer: ``224``
        - ID: ``DB64FD34``

    Parameters:
        tmp_password (``bytes``):
            Temporary password

        valid_until (``int`` ``32-bit``):
            Validity period

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetTmpPassword
    """

    __slots__: List[str] = ["tmp_password", "valid_until"]

    ID = 0xdb64fd34
    QUALNAME = "types.account.TmpPassword"

    def __init__(self, *, tmp_password: bytes, valid_until: int) -> None:
        self.tmp_password = tmp_password  # bytes
        self.valid_until = valid_until  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TmpPassword":
        # No flags

        tmp_password = Bytes.read(b)

        valid_until = Int.read(b)

        return TmpPassword(tmp_password=tmp_password, valid_until=valid_until)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Bytes(self.tmp_password))

        b.write(Int(self.valid_until))

        return b.getvalue()
