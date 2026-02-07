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


class InputInvoiceStarGiftPrepaidUpgrade(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``9A0B48B8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        hash (``str``):
            N/A

    """

    __slots__: List[str] = ["peer", "hash"]

    ID = 0x9a0b48b8
    QUALNAME = "types.InputInvoiceStarGiftPrepaidUpgrade"

    def __init__(self, *, peer: "raw.base.InputPeer", hash: str) -> None:
        self.peer = peer  # InputPeer
        self.hash = hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftPrepaidUpgrade":
        # No flags

        peer = TLObject.read(b)

        hash = String.read(b)

        return InputInvoiceStarGiftPrepaidUpgrade(peer=peer, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(String(self.hash))

        return b.getvalue()
