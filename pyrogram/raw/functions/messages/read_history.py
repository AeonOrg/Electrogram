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


class ReadHistory(TLObject):  # type: ignore
    """Marks message history as read.


    Details:
        - Layer: ``224``
        - ID: ``E306D3A``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Target user or group

        max_id (``int`` ``32-bit``):
            If a positive value is passed, only messages with identifiers less or equal than the given one will be read

    Returns:
        :obj:`messages.AffectedMessages <pyrogram.raw.base.messages.AffectedMessages>`
    """

    __slots__: List[str] = ["peer", "max_id"]

    ID = 0xe306d3a
    QUALNAME = "functions.messages.ReadHistory"

    def __init__(self, *, peer: "raw.base.InputPeer", max_id: int) -> None:
        self.peer = peer  # InputPeer
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadHistory":
        # No flags

        peer = TLObject.read(b)

        max_id = Int.read(b)

        return ReadHistory(peer=peer, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags

        b.write(self.peer.write())

        b.write(Int(self.max_id))

        return b.getvalue()
