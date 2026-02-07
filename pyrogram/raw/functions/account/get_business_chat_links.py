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


class GetBusinessChatLinks(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``6F70DDE1``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.BusinessChatLinks <pyrogram.raw.base.account.BusinessChatLinks>`
    """

    __slots__: List[str] = []

    ID = 0x6f70dde1
    QUALNAME = "functions.account.GetBusinessChatLinks"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBusinessChatLinks":
        # No flags

        return GetBusinessChatLinks()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        return b.getvalue()
