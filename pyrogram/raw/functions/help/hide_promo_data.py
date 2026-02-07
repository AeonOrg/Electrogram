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


class HidePromoData(TLObject):  # type: ignore
    """Hide MTProxy/Public Service Announcement information


    Details:
        - Layer: ``224``
        - ID: ``1E251C95``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Peer to hide

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer"]

    ID = 0x1e251c95
    QUALNAME = "functions.help.HidePromoData"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HidePromoData":
        # No flags

        peer = TLObject.read(b)

        return HidePromoData(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
