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


class InputInvoiceStarGift(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``E8625E92``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        gift_id (``int`` ``64-bit``):
            N/A

        hide_name (``bool``, *optional*):
            N/A

        include_upgrade (``bool``, *optional*):
            N/A

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "gift_id", "hide_name", "include_upgrade", "message"]

    ID = 0xe8625e92
    QUALNAME = "types.InputInvoiceStarGift"

    def __init__(self, *, peer: "raw.base.InputPeer", gift_id: int, hide_name: Optional[bool] = None, include_upgrade: Optional[bool] = None, message: "raw.base.TextWithEntities" = None) -> None:
        self.peer = peer  # InputPeer
        self.gift_id = gift_id  # long
        self.hide_name = hide_name  # flags.0?true
        self.include_upgrade = include_upgrade  # flags.2?true
        self.message = message  # flags.1?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGift":

        flags = Int.read(b)

        hide_name = True if flags & (1 << 0) else False
        include_upgrade = True if flags & (1 << 2) else False
        peer = TLObject.read(b)

        gift_id = Long.read(b)

        message = TLObject.read(b) if flags & (1 << 1) else None

        return InputInvoiceStarGift(peer=peer, gift_id=gift_id, hide_name=hide_name, include_upgrade=include_upgrade, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.hide_name else 0
        flags |= (1 << 2) if self.include_upgrade else 0
        flags |= (1 << 1) if self.message is not None else 0
        b.write(Int(flags))

        b.write(self.peer.write())

        b.write(Long(self.gift_id))

        if self.message is not None:
            b.write(self.message.write())

        return b.getvalue()
