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


class GetStarsStatus(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``224``
        - ID: ``4EA9B3BF``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):


        ton (``bool``, *optional*):
            N/A

    Returns:
        :obj:`payments.StarsStatus <pyrogram.raw.base.payments.StarsStatus>`
    """

    __slots__: List[str] = ["peer", "ton"]

    ID = 0x4ea9b3bf
    QUALNAME = "functions.payments.GetStarsStatus"

    def __init__(self, *, peer: "raw.base.InputPeer", ton: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.ton = ton  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsStatus":

        flags = Int.read(b)

        ton = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        return GetStarsStatus(peer=peer, ton=ton)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        return b.getvalue()
