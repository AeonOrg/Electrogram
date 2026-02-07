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


class GetPeerProfileColors(TLObject):  # type: ignore
    """Get the set of accent color palettes » that can be used in profile page backgrounds.


    Details:
        - Layer: ``224``
        - ID: ``ABCFA9FD``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the help.peerColors.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`help.PeerColors <pyrogram.raw.base.help.PeerColors>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xabcfa9fd
    QUALNAME = "functions.help.GetPeerProfileColors"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerProfileColors":
        # No flags

        hash = Int.read(b)

        return GetPeerProfileColors(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.hash))

        return b.getvalue()
