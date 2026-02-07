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


class ReadSavedHistory(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BA4A3B5B``

    Parameters:
        parent_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        max_id (``int`` ``32-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["parent_peer", "peer", "max_id"]

    ID = 0xba4a3b5b
    QUALNAME = "functions.messages.ReadSavedHistory"

    def __init__(self, *, parent_peer: "raw.base.InputPeer", peer: "raw.base.InputPeer", max_id: int) -> None:
        self.parent_peer = parent_peer  # InputPeer
        self.peer = peer  # InputPeer
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadSavedHistory":
        # No flags

        parent_peer = TLObject.read(b)

        peer = TLObject.read(b)

        max_id = Int.read(b)

        return ReadSavedHistory(parent_peer=parent_peer, peer=peer, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.parent_peer.write())

        b.write(self.peer.write())

        b.write(Int(self.max_id))

        return b.getvalue()
