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


class GetQuickReplies(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``D483F2A8``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

    Returns:
        :obj:`messages.QuickReplies <pyrogram.raw.base.messages.QuickReplies>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xd483f2a8
    QUALNAME = "functions.messages.GetQuickReplies"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetQuickReplies":
        # No flags

        hash = Long.read(b)

        return GetQuickReplies(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        return b.getvalue()
