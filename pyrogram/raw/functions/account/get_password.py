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


class GetPassword(TLObject):  # type: ignore
    """Obtain configuration for two-factor authorization with password


    Details:
        - Layer: ``224``
        - ID: ``548A30F5``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.Password <pyrogram.raw.base.account.Password>`
    """

    __slots__: List[str] = []

    ID = 0x548a30f5
    QUALNAME = "functions.account.GetPassword"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPassword":
        # No flags

        return GetPassword()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
