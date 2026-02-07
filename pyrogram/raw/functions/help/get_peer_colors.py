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


class GetPeerColors(TLObject):  # type: ignore
    """Get the set of accent color palettes » that can be used for message accents.


    Details:
        - Layer: ``224``
        - ID: ``DA80F42F``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the help.peerColors.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`help.PeerColors <pyrogram.raw.base.help.PeerColors>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xda80f42f
    QUALNAME = "functions.help.GetPeerColors"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerColors":
        # No flags

        hash = Int.read(b)

        return GetPeerColors(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(Int(self.hash))

        return b.getvalue()
