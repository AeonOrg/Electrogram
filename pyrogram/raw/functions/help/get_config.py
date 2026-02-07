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


class GetConfig(TLObject):  # type: ignore
    """Returns current configuration, including data center configuration.


    Details:
        - Layer: ``224``
        - ID: ``C4F9186B``

    Parameters:
        No parameters required.

    Returns:
        :obj:`Config <pyrogram.raw.base.Config>`
    """

    __slots__: List[str] = []

    ID = 0xc4f9186b
    QUALNAME = "functions.help.GetConfig"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetConfig":
        # No flags

        return GetConfig()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
