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


class GetConnectedBots(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``4EA4C80F``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.ConnectedBots <pyrogram.raw.base.account.ConnectedBots>`
    """

    __slots__: List[str] = []

    ID = 0x4ea4c80f
    QUALNAME = "functions.account.GetConnectedBots"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetConnectedBots":
        # No flags

        return GetConnectedBots()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
