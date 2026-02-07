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


class GetPremiumGiftCodeOptions(TLObject):  # type: ignore
    """Obtain a list of Telegram Premium giveaway/gift code » options.


    Details:
        - Layer: ``224``
        - ID: ``2757BA54``

    Parameters:
        boost_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            The channel that will start the giveaway

    Returns:
        List of :obj:`PremiumGiftCodeOption <pyrogram.raw.base.PremiumGiftCodeOption>`
    """

    __slots__: List[str] = ["boost_peer"]

    ID = 0x2757ba54
    QUALNAME = "functions.payments.GetPremiumGiftCodeOptions"

    def __init__(self, *, boost_peer: "raw.base.InputPeer" = None) -> None:
        self.boost_peer = boost_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPremiumGiftCodeOptions":

        flags = Int.read(b)

        boost_peer = TLObject.read(b) if flags & (1 << 0) else None

        return GetPremiumGiftCodeOptions(boost_peer=boost_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.boost_peer is not None else 0
        b.write(Int(flags))

        if self.boost_peer is not None:
            b.write(self.boost_peer.write())

        return b.getvalue()
