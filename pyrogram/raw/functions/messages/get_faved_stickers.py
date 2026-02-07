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


class GetFavedStickers(TLObject):  # type: ignore
    """Get faved stickers


    Details:
        - Layer: ``224``
        - ID: ``4F1AAA9``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.favedStickers.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`messages.FavedStickers <pyrogram.raw.base.messages.FavedStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x4f1aaa9
    QUALNAME = "functions.messages.GetFavedStickers"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFavedStickers":
        # No flags

        hash = Long.read(b)

        return GetFavedStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Long(self.hash))

        return b.getvalue()
