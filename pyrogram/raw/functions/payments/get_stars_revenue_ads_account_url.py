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


class GetStarsRevenueAdsAccountUrl(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D1D7EFC5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`payments.StarsRevenueAdsAccountUrl <pyrogram.raw.base.payments.StarsRevenueAdsAccountUrl>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0xd1d7efc5
    QUALNAME = "functions.payments.GetStarsRevenueAdsAccountUrl"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsRevenueAdsAccountUrl":
        # No flags

        peer = TLObject.read(b)

        return GetStarsRevenueAdsAccountUrl(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        return b.getvalue()
