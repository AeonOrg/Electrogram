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


class GetStarsTransactionsByID(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2DCA16B8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (List of :obj:`InputStarsTransaction <pyrogram.raw.base.InputStarsTransaction>`):
            N/A

        ton (``bool``, *optional*):
            N/A

    Returns:
        :obj:`payments.StarsStatus <pyrogram.raw.base.payments.StarsStatus>`
    """

    __slots__: List[str] = ["peer", "id", "ton"]

    ID = 0x2dca16b8
    QUALNAME = "functions.payments.GetStarsTransactionsByID"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List["raw.base.InputStarsTransaction"], ton: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<InputStarsTransaction>
        self.ton = ton  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStarsTransactionsByID":

        flags = Int.read(b)

        ton = True if flags & (1 << 0) else False
        peer = TLObject.read(b)

        id = TLObject.read(b)

        return GetStarsTransactionsByID(peer=peer, id=id, ton=ton)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Vector(self.id))

        return b.getvalue()
